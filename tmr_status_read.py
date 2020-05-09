from telnetlib import Telnet
#import re
import numpy as np
import pandas as pd


with Telnet('192.168.1.60', 50000) as tn:

    tn.write(b"DIR\r\n")

    # 正規表現読み込み
    #allr = re.compile(b"END.*\r\n")
    # DIR_return=tn.expect([allr],timeout=5)

    DIR_return = tn.read_until(b"END", timeout=5)
    STA1_return = tn.read_until(b"\n", timeout=5)

    tn.write(b"FLN\r\n")
    FLN_return = tn.read_until(b"\n", timeout=5)

    tn.write(b"STA1\r\n")
    STA1_return = tn.read_until(b"\n", timeout=5)

    DIR = np.array(DIR_return.decode(encoding='utf-8'))
    FLN = np.array(FLN_return.decode(encoding='utf-8'))
    STA1 = np.array(STA1_return.decode(encoding='utf-8'))

    # print(DIR)
    # print(FLN)
    # print(STA1)

    DAT_return_byte = 1624
    DAT_return_byte_cout = 0
    DAT_return = b''

    tn.write(b"DAT S001.DAT\r\n")
    while DAT_return_byte_cout < DAT_return_byte:
        DAT_return_tmp = tn.read_some()
        print(DAT_return_tmp)
        DAT_return += DAT_return_tmp
        # print(len(DAT_return))
        DAT_return_byte_cout += len(DAT_return)

    print(DAT_return)
    # DAT_return_str=DAT_return.decode(encoding='utf-8')
    # print(DAT_return_str)

