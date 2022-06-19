"""
C - Doubled
https://atcoder.jp/contests/abc196/tasks/abc196_c
"""

N = int(input())
ans = 0
x = 1
while True:
    double = int(str(x) + str(x))
    if double > N:
        break
    ans += 1
    x += 1

print(ans)
