"""
C - XX to XXX
https://atcoder.jp/contests/abc259/tasks/abc259_c
"""
from itertools import groupby


def run_length_encode(S: str):
    grouped = groupby(S)
    res = [(k, len(list(v))) for k, v in grouped]
    return res


S = str(input())
T = str(input())

groupby_s = run_length_encode(S)
groupby_t = run_length_encode(T)

if len(groupby_s) != len(groupby_t):
    print("No")
    exit()


ans = True
for s, t in zip(groupby_s, groupby_t):
    char_s = s[0]
    char_t = t[0]

    if char_s != char_t:
        ans = False
        break

    len_s = s[1]
    len_t = t[1]

    if (len_s < len_t) and (len_s > 1):
        continue
    elif len_s == len_t:
        continue
    else:
        ans = False
        break

print("Yes" if ans else "No")
