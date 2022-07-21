"""
B - Smartphone Addiction
https://atcoder.jp/contests/abc185/tasks/abc185_b
"""

N, M, T = map(int, input().split())
query = [list(map(int, input().split())) for _ in range(M)] + [[T, T]]

now_battery = N
now_time = 0
ans = True
for a, b in query:
    now_battery -= a - now_time

    if now_battery <= 0:
        ans = False

    now_battery += b - a
    now_battery = min(N, now_battery)
    now_time = b


print("Yes" if ans else "No")
