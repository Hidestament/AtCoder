"""
C - Changing Jewels
https://atcoder.jp/contests/abc260/tasks/abc260_c
"""

from collections import defaultdict


N, X, Y = map(int, input().split())

ans = 0
red_dict = defaultdict(int, {N: 1})
blue_dict = defaultdict(int, {1: 0})


# 一番レベルの高い石を変換し続ける
while True:
    red_max = max(red_dict.keys())
    blue_max = max(blue_dict.keys())

    if red_max == 1 and blue_max == 1:
        break

    if red_max >= blue_max:
        max_num = red_dict[red_max]
        red_dict[red_max - 1] += max_num
        blue_dict[red_max] += X * max_num
        red_dict.pop(red_max)
    else:
        max_num = blue_dict[blue_max]
        red_dict[blue_max - 1] += max_num
        blue_dict[blue_max - 1] += Y * max_num
        blue_dict.pop(blue_max)

print(blue_dict[1])
