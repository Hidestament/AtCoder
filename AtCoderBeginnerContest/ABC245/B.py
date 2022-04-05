"""
B - Mex
問題リンク: https://atcoder.jp/contests/abc245/tasks/abc245_b
"""

N = int(input())
A = set(list(map(int, input().split())))

for i in range(2002):
    if i not in A:
        print(i)
        break
