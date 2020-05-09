

class asc2csv:
    """ 
    TDS-150等で記録したASC形式のデータを
    CSV形式に変換する\n
    (入力値)inputfilename : 変換対象のASC形式のファイル名\n
    (出力値)putputfilename : 変換後のCSV形式のファイル名\n
    conv：変換実行\n
     """

    def __init__(self, inputfilename,outputfilename):
        self.inputfilename = inputfilename
        self.outputfilename = outputfilename
        #inputfilename = 'dat002.asc'
        #outputfilename = 'dat002.csv'

    def conv(self):

        #入力ファイルを開く
        inputfile = open(self.inputfilename, 'r')

        # すべて読み込んでリストデータにする
        lines = inputfile.readlines()

        #書き込みファイルを開く
        writer = open(self.outputfilename, 'a')  

        for line in lines:
            scandata=line.split()

            if scandata[0] == 'END':
                #行がENDの場合
                writer.write("\n")
            elif str(scandata[0])[:2] =='20':
                #行が日付の場合
                writer.write("{} {}".format(str(scandata[0]),str(scandata[1])))
            else:
                writer.write(",{}".format(scandata[1]))

        writer.close()

#メイン処理
def main():
    #ファイル名を指定してインスタンス作成
    a=asc2csv('dat003.asc','dat003.csv')
    #変換実行
    a.conv()
    #インスタンス削除
    del(a)

#プログラム実行
if __name__ == '__main__':
    main()


