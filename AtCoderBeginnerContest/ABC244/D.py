"""
D - Swap Hat
問題リンク: https://atcoder.jp/contests/abc244/tasks/abc244_d
"""

S = list(map(str, input().split()))
T = list(map(str, input().split()))

table = {c: i for i, c in enumerate(S)}
T = [table[T[i]] for i in range(3)]


inversion = 0
for i in range(2):
    for j in range(i+1, 3):
        if T[i] > T[j]:
            inversion += 1

print("Yes" if inversion % 2 == 0 else "No")
