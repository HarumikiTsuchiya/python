import csv
import numpy as np

class DadispConv:
    """
    Dadisp形式データ読み込み
    CSV変換プログラム
    2020/02/23
    土屋晴幹\n
    ・メソッド\n
    　convnp() : データをnumpy配列に変換する\n
    　convcsv() : データをCSV形式で保存する\n
    ・引数\n
    　dataname : ファイル名(拡張子なし)\n
    　COEF : 係数演算ON/OFF\n
    　OFFSET :　オフセット演算ON/OFF\n
    2020/4/4 メソッドをconvnpとconvcsvに分ける。
    """

    def __init__(self,detaname):

        self.dataname = detaname

    def convnp(self,COEF = True ,OFFSET = True):

        self.COEF = COEF
        self.OFFSET = OFFSET

        #読み込みデータファイル名
        #dataname = 'F001'
        dataname =self.dataname 

        #ヘッダ読み込み
        header=HeaderRead(dataname)

        #データ数
        #NUM_SAMPS = 359976
        NUM_SAMPS = header.conv('NUM_SAMPS')

        #ch数
        #NUM_SERIES = 29
        NUM_SERIES = header.conv('NUM_SERIES')

        #ヘッダ
        #SERIES = ['CH_1','CH_2','CH_3','CH_4','CH_5','CH_6','CH_7','CH_8','CH_9','CH_10','CH_11','CH_12','CH_13','CH_14','CH_15','CH_16','CH_17','CH_18','CH_19','CH_20','CH_21','CH_22','CH_23','CH_24','CH_25','CH_26','CH_27','CH_28','CH_33']
        SERIES = header.conv('SERIES')

        #係数
        #SLOPE=[1.00000000,1.00000000,1.00000000,1.00000000,1.00000000,1.00000000,1.00000000,1.00000000,1.00000000,1.00000000,1.00000000,1.00000000,1.00000000,1.00000000,1.00000000,1.00000000,1.00000000,1.00000000,1.00000000,1.00000000,1.00000000,1.00000000,1.00000000,1.00000000,1.00000000,1.00000000,1.00000000,1.00000000,0.10000000]
        SLOPE = header.conv('SLOPE')

        #オフセット値
        #Y_OFFSET=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        Y_OFFSET = header.conv('Y_OFFSET')


        print('File= {} DAT読み込み開始'.format(dataname))

        #DATファイル読み込み
        #list領域確保
        mylist = [[0 for i in range(NUM_SERIES)] for j in range(NUM_SAMPS)]

        myfile = open(dataname + '.dat', 'rb')

        for j in range(NUM_SAMPS):

            for i in range(NUM_SERIES):
                #バイナリファイルを配列に変換　2バイト　リトルエンディアン　符号付
                mylist[j][i] = int.from_bytes(myfile.read(2), 'little', signed=True)

        myfile.close()

        #listをnumpyに変換
        np_data = np.array(mylist)

        print('File= {} DAT読み込み完了'.format(dataname))

        if self.COEF == True:
            print('File= {} 係数演算開始'.format(dataname))

            #係数計算
            np_data=np_data * SLOPE

            print('File= {} 係数演算完了'.format(dataname))


        #オフセット計算
        if self.OFFSET == True:
            print('File= {} オフセット演算開始'.format(dataname))
            np_data=np_data + Y_OFFSET

            print('File= {} オフセット演算完了'.format(dataname))

        #list_data=np_data.tolist()
        #return list_data

        return np_data

    def convcsv(self,COEF = True ,OFFSET = True):

        #読み込みデータファイル名
        #dataname = 'F001'
        dataname =self.dataname 

        self.COEF = COEF
        self.OFFSET = OFFSET

        #ヘッダ読み込み
        header=HeaderRead(dataname)

        #ヘッダ
        #SERIES = ['CH_1','CH_2','CH_3','CH_4','CH_5','CH_6','CH_7','CH_8','CH_9','CH_10','CH_11','CH_12','CH_13','CH_14','CH_15','CH_16','CH_17','CH_18','CH_19','CH_20','CH_21','CH_22','CH_23','CH_24','CH_25','CH_26','CH_27','CH_28','CH_33']
        SERIES = header.conv('SERIES')

        np_data=self.convnp(COEF=self.COEF,OFFSET=self.OFFSET)

        print('File= {} CSV保存開始'.format(dataname))

        #CSVファイルへ書き出し
        with open(dataname + '.csv', 'w') as csvfile:
            writer = csv.writer(csvfile, lineterminator='\n')
            #チャンネル名出力
            writer.writerow(SERIES)
            #データ出力
            writer.writerows(np_data)

        print('File= {} CSV保存完了'.format(dataname))




class HeaderRead:
    """
    DC-204R、TMR等のDadisp形式のデータのうちHeaderファイルの各要素を抽出する\n
    dataname : ファイル名(拡張子なし)\n
    conv : 値の変換\n
    SERIES : ch名\n
    NUM_SERIES : ch数(INT)\n
    NUM_SAMPS : データ数(INT)\n
    SLOPE :　係数\n
    Y_OFFSET : オフセット値\n
    DATE : 測定開始日\n
    TIME : 測定開始時刻\n
    """

    def __init__(self,dataname):
        self.dataname  = dataname

    def conv(self,header):
        # ファイルをオープンする
        header_data = open(self.dataname + ".hed", "r")

        # 行ごとにすべて読み込んでリストデータにする
        lines = header_data.readlines()

        header_data.close()

        l=list([['1','2']])
        for line in lines:
            a=line.split()
            if len(a)==2:
                l.append(a)
            
        #辞書型に変換
        reader = dict(l)

        #各要素抽出
        SERIES=reader['SERIES'].split(',')
        NUM_SERIES=reader['NUM_SERIES'].split(',')
        NUM_SAMPS=reader['NUM_SAMPS'].split(',')
        SLOPE=reader['SLOPE'].split(',')
        Y_OFFSET=reader['Y_OFFSET'].split(',')
        DATE=reader['DATE'].split(',')
        TIME=reader['TIME'].split(',')

        #文字列から数値へ変換
        NUM_SERIES = int(NUM_SERIES[0])
        NUM_SAMPS = int(NUM_SAMPS[0]) 
        SLOPE = [float(i) for i in SLOPE] 
        Y_OFFSET = [float(i) for i in Y_OFFSET] 

        if header == 'NUM_SERIES' :
            #print(NUM_SERIES)
            return(NUM_SERIES)
        if header == 'NUM_SAMPS':
            #print(NUM_SAMPS)
            return(NUM_SAMPS)
        if header == 'SERIES':
            #print(SERIES)
            return(SERIES)
        if header == 'SLOPE':
            #print(SLOPE)
            return(SLOPE)
        if header == 'Y_OFFSET':
            #print(Y_OFFSET)
            return(Y_OFFSET)
        if header == 'DATE':
            #print(DATE)
            return(DATE)
        if header == 'TIME':
            #print(TIME)
            return(TIME)

#メイン処理
def main():
    #ファイル名を指定してインスタンス作成
    a=DadispConv('F001')

    #numpyリスト変換実行
    #b=a.convnp(COEF=False,OFFSET=False)

    #CSV変換実行
    c=a.convcsv(COEF=True,OFFSET=False)

    #print(b)
    #インスタンス削除
    del(a)


#プログラム実行
if __name__ == '__main__':
    main()
    

