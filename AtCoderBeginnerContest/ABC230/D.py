"""
D - Destroyer Takahashi
https://atcoder.jp/contests/abc230/tasks/abc230_d
区間スケジューリングのように解いていけば良い
"""

N, D = map(int, input().split())
block = [list(map(int, input().split())) for _ in range(N)]
block.sort(key=lambda x: (x[1], x[0]))

ans = 0
last = -D
for left, right in block:
    if last + (D - 1) < left:
        ans += 1
        last = right

print(ans)
