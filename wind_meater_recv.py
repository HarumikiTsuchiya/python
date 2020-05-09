#! /usr/bin/env python3
"""
風光風速計のデータを受信して
3秒毎の瞬間最大風速と10分間平均風速を算出する
10分毎にアラートレベルと比較し
警報メールを送信する。
2020/3/29　
東京測器研究所　土屋
"""

import serial
import numpy as np

import subprocess
import datetime

# アラートレベル　瞬間最大風速(m/s)
ALERT_LEVEL_WIND_MAX = 20

# アラートレベル　平均風速(m/s)
ALERT_LEVEL_WIND_10MIN_AVERAGE = 20

# send_wind_alary.pyの位置
sendmail_path = '/home/harumiki/python/sendmail_wind_alert.py'

# 計測データ保存先
CSVfilename = "/home/harumiki/python/wind_meater_data.csv"


def main():

    # シリアルポートを開く
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=None)

    # 3秒間瞬間風速  リストを準備
    wind_syunkan = np.zeros(4*3)

    # 10分間平均風速　リストを準備
    wind_heikin = np.zeros(4*3*200)

    # 風光風速計設定
    ser.write(b"*\r\n")  # 設定モード
    ser.write(b"P20\r\n")  # 1/4秒出力
    ser.write(b"D3\r\n")  # 設定確認
    recv_data = ser.readline()
    print(recv_data)
    ser.write(b"Q\r\n")  # 測定モード

    while True:

        # 最大瞬間風速
        wind_syunkan_max = 0

        recv_cout_10min = 0

        # 10分間平均風速　リセット
        wind_heikin = np.zeros(4*3*200)

        # 計測開始時刻
        dt_from = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")

        # 10分ごとの処理　(600sec/3sec=200)
        while recv_cout_10min < 200:
            recv_cout_3sec = 0

            # 3秒間瞬間風速  リセット
            wind_syunkan = np.zeros(4*3)

            # 3秒ごとの処理
            while recv_cout_3sec < 4*3:

                try:
                    # 1行データを読み込み
                    recv_data = ser.readline()
                    # print(recv_data)

                    # 受信データ(バイナリ)を文字列にデコードする。
                    recv_data_str = recv_data.decode()

                    # 制御文字削除ルーチン

                    # 初期化する
                    ret = ""

                    # 文字列を1文字ずつ読み込み処理をする
                    for c in recv_data_str:

                        # ordで10進数で ASCII コード（Unicode）を出力し、ord_num に代入する
                        ord_num = ord(c)
                        # print(ord_num)
                        # ASCII文字以外の制御コードがあるかチェックする
                        if(ord_num > 32) and (ord_num < 128):
                            ret = ret + c

                    # 特殊記号削除後の文字列
                    # print(ret)

                    recv_data_str_conv = ret

                    # 先頭データをNodeAddressとして読み込む(CSV要素1個目)
                    # wind_node_address=recv_data.decode('utf-8').split(',')[0]
                    wind_node_address = recv_data_str_conv.split(',')[0]

                    # NodeAddressが’Q’かどうか判別（文字化け・データ途中受信等対策）
                    if wind_node_address in 'Q':
                        # 風向データ取得(CSV要素2個目)
                        # wind_direction=int(recv_data.decode('utf-8').split(',')[1])
                        wind_direction = int(recv_data_str_conv.split(',')[1])
                        # 風速データ取得(CSV要素3個目)
                        # wind_speed=float(recv_data.decode('utf-8').split(',')[2])
                        wind_speed = float(recv_data_str_conv.split(',')[2])
                        #print(wind_node_address,  wind_direction, wind_speed)

                        # リストをシフト
                        wind_syunkan = np.roll(wind_syunkan, 1)
                        wind_heikin = np.roll(wind_heikin, 1)

                        # リストに風速を追加
                        wind_syunkan[0] = wind_speed
                        wind_heikin[0] = wind_speed

                        recv_cout_3sec += 1

                # 受信エラーや変換エラー時にはエラー文を出力して続行
                except Exception as e:
                    print(e)
            # 最大瞬間風速を比較
            if np.mean(wind_syunkan) > wind_syunkan_max:
                wind_syunkan_max = np.mean(wind_syunkan)

            # 3秒毎の瞬間風速・最大瞬間風速を出力
            #print('{0}  瞬間風速= {1:.2f} 最大瞬間風速= {2:.2f} '.format(recv_cout_10min , np.mean(wind_syunkan), wind_syunkan_max))

            recv_cout_10min += 1

        # 計測終了時刻
        dt_end = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")

        # print(dt_from)
        # print(dt_end)

        # 10分毎の最大瞬間風速・10分平均風速を出力
        wind_heikin_10min = np.mean(wind_heikin)
        #print('最大瞬間風速= {0:.2f} 10分平均風速= {1:.2f} '.format( wind_syunkan_max,wind_heikin_10min))
        send_msg = '{0}〜{1}\n最大瞬間風速= {2:.2f}m/s \n平均風速= {3:.2f} m/s'.format(
            dt_from, dt_end, wind_syunkan_max, wind_heikin_10min)
        print(send_msg)

        # 計測データをCSV保存
        csv_data = dt_from + ',' + dt_end + ',' + \
            wind_syunkan_max + ',' + wind_heikin_10min + '\n'
        # 書き込みファイルを開く
        writer = open(self.CSVfilename, 'a')
        # 書き込み
        writer.write(csv_data)
        # ファイルを閉じる
        writer.close()

        # 最大瞬間風速・平均風速のアラートレベルとの比較
        if wind_syunkan_max >= ALERT_LEVEL_WIND_MAX or wind_heikin_10min >= ALERT_LEVEL_WIND_10MIN_AVERAGE:
            # 警報時の処理
            print("警報発生")
            command = ['python3', sendmail_path, send_msg]
            subprocess.Popen(command)

    ser.close()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Program STOP")
        sys.exit(1)
