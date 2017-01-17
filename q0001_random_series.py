# -*- coding: utf-8 -*-

# 第 0001 题
# 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
# 使用 Python 如何生成 200 个激活码（或者优惠券）

import random

def random_series(len=10):
    str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    series = ''
    for i in range(len):
        series += random.choice(str)
    return series

def random_series_list(count=3):
    series_set = []
    for i in range(count):
        series = random_series()
        series_set.append(series)
    return series_set

if __name__ == "__main__":
    import sys
    series_list = []

    if len(sys.argv) > 1:
        series_list = random_series_list(int(sys.argv[1]))
    else:
        series_list = random_series_list()

    print(series_list)
