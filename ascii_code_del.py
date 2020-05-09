#1行データを読み込み
recv_data = b"\x00Q,223,10.00"
print(recv_data)

recv_data=recv_data.decode()

# 初期化する
ret = ""

# 文字列を1文字ずつ読み込み処理をする
for c in recv_data:

    # ordで10進数で ASCII コード（Unicode）を出力し、ord_num に代入する
    ord_num = ord(c)
    #print(ord_num)
    # ascii文字の制御コードがあるかチェックする
    if(ord_num < 128) and (ord_num > 32):
        ret = ret + c

# 特殊記号削除後の文字列
print(ret)

recv_data=ret

#先頭データをNodeAddressとして読み込む(CSV要素1個目)
#wind_node_address=recv_data.decode('utf-8').split(',')[0]
wind_node_address=recv_data.split(',')[0]
print(wind_node_address)

#NodeAddressが’Q’かどうか判別（文字化け等対策）
if wind_node_address in 'Q':
    #風向データ取得(CSV要素2個目)
    wind_direction=int(recv_data.split(',')[1])
    #風速データ取得(CSV要素3個目)
    wind_speed=float(recv_data.split(',')[2])
    #print(wind_node_address,  wind_direction, wind_speed) 
    print(wind_direction)
    print(wind_speed)
