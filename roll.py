import numpy as np
import time
import datetime

#3秒間瞬間風速
syunkan = np.zeros(4*3)

#10分間平均風速
heikin = np.zeros(4*3*600)

#計測データ保存先
CSVfilename ="/home/harumiki/python/wind_meater_data.csv"


while(1):

    #計測開始時刻
    dt_from = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    for i in range(4*3):

        #現在風速
        fusoku =np.random.rand()*30

        #リストをシフト
        syunkan = np.roll(syunkan, 1)
        heikin = np.roll(heikin, 1)
 
        #リストに風速を追加
        syunkan[0] = fusoku
        heikin[0] = fusoku

        #0.25秒待機
        time.sleep(0.1)

    #計測終了時刻
    dt_end = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    #3秒毎に現在値を表示
    #print('瞬間風速= {0:.2f} 10分平均風速= {1:.2f} '.format( np.mean(syunkan),np.mean(heikin)))
    send_msg='{0}〜{1}\n最大瞬間風速= {2:.2f}m/s \n10分平均風速= {3:.2f} m/s'.format(dt_from ,dt_end, np.mean(syunkan),np.mean(heikin))
    print(send_msg)

    #計測データをCSV保存
    csv_data = dt_from + ',' + dt_end + ',' +  str(np.mean(syunkan)) + ',' + str(np.mean(heikin)) + '\n'
    #書き込みファイルを開く
    writer = open(CSVfilename, 'a')  
    #書き込み
    writer.write(csv_data)
    #ファイルを閉じる
    writer.close()

