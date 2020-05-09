#! /usr/bin/env python3
"""
風光風速計のデータCSVを
グラフに変換しPNGで保存する。
2020/3/29　
東京測器研究所　土屋
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime

#
filename = 'wind_meater_data.csv'

def main():

    df = pd.read_csv(filename, names=['FROM','TO','MAX','10MIN'])

    #print(df)

    fig = plt.figure(figsize = (8,6))

    plt.xlabel('Time')
    plt.ylabel('wind speed(m/s)')

    plt.plot(pd.to_datetime(df['TO']),df['MAX'], label="Maximum instantaneous wind speed")
    plt.plot(pd.to_datetime(df['TO']),df['10MIN'], label="Average wind speed")

    #x軸の時間表記
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%m/%d\n%H:%M"))

    #x軸の時間範囲
    dt_now=datetime.datetime.now()
    sxmax=dt_now.strftime("%Y-%m-%d %H:%M:%S")
    dt_now_before=dt_now - datetime.timedelta(hours=6)
    sxmin=dt_now_before.strftime("%Y-%m-%d %H:%M:%S")
    #print(sxmax)
    #print(sxmin)

    xmin = datetime.datetime.strptime(sxmin, '%Y-%m-%d %H:%M:%S')
    xmax = datetime.datetime.strptime(sxmax, '%Y-%m-%d %H:%M:%S')
    plt.xlim([xmin,xmax])

    #グリッドを1時間単位
    #plt.gca().xaxis.set_major_locator(mdates.HourLocator())
    #グリッドを30分単位
    plt.gca().xaxis.set_major_locator(mdates.MinuteLocator(byminute=[0,30]))

    #タイトル
    plt.title("Wind Speed")
    #凡例表示
    plt.legend()
    #グリッド表示
    plt.grid()
    #45度回転
    #plt.xticks(rotation=45)

    #画像保存
    fig.savefig("wind_data.png")

if __name__ == '__main__':
    main()
