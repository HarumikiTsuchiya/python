#!/usr/bin/env python3
"""
風光風速計の警報メールを送信する。
2020/3/29　
東京測器研究所　土屋
"""

from email.mime.text import MIMEText
from email.utils import formatdate
import smtplib
import time
import datetime
import sys

# 実行時引数取得
args = sys.argv

# メールサーバのアカウント
account = "tmlnagoyafptem@gmail.com"
password = "drncjpzhhermivgn"

# メールの送信先
#to_email = "tmlnagoyafptem@gmail.com"
bcc_email = "harumiki.tsuchiya@gmail.com"
to_email = "tsuchiya@tml.jp"

# メールに付ける送信元
from_email = "tmlnagoyafptem@gmail.com"

# メールタイトル
subject = "風速警報"

# 引数がある場合には本文を入れ替える
if len(args) > 1:
    # メール本文
    data = args[1]
else:
    # メール本文
    data = "風速警報が発生しました。"


# メール作成
msg = MIMEText(data)
msg["Subject"] = subject
msg["To"] = to_email
msg["Bcc"] = bcc_email
msg["From"] = from_email
msg["Date"] = formatdate(None, True)

# print(msg)
try:
    # 送信サーバへのインスタンス作成
    server = smtplib.SMTP("smtp.gmail.com", 587)
    # デバッグコードを標準出力に表示する
    # server.set_debuglevel(True)
    # TLS接続開始
    server.starttls()
    # ログイン
    server.login(account, password)
    # メッセージ送信
    server.send_message(msg)
    # 接続クローズ
    server.quit()
except:
    data = ""
    print("Mail Send ERR!")
else:
    data = ""
    print("Mail Send OK!")

