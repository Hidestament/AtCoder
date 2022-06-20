"""
C - Unexpressed
https://atcoder.jp/contests/abc193/tasks/abc193_c
"""

N = int(input())
ng = set()

for a in range(2, int(N**0.5) + 10):
    now = a
    while now * a <= N:
        now *= a
        ng.add(now)

print(N - len(ng))
