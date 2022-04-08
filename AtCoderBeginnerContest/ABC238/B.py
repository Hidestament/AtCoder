"""
B - Pizza
https://atcoder.jp/contests/abc238/tasks/abc238_b
"""

N = int(input())
A = list(map(int, input().split()))

cut = [0, 360]
for a in A:
    cut.append((cut[-1] + a) % 360)

cut.sort()
ans = max(cut[i+1] - cut[i] for i in range(len(cut) - 1))
print(ans)
