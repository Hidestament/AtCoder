"""
C - Yamanote Line Game
問題リンク: https://atcoder.jp/contests/abc244/tasks/abc244_c
"""

N = int(input())
used = set()

for i in range(1, 2*N+2):
    if i not in used:
        print(i)
        used.add(i)
    else:
        continue

    aoki = int(input())
    if aoki == 0:
        break
    else:
        used.add(aoki)
