def calc_tax(price, rate):
    tax = price * rate / 100
    # 整数化して値を返す
    return int(tax)


a = calc_tax(1249, 10)
print(a)
