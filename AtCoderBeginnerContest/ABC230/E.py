"""
E - Fraction Floor Sum
https://atcoder.jp/contests/abc230/tasks/abc230_e
N/xの格子点の数が答え
参考: https://math.nakaken88.com/problem/atcoder-abc-230-e/
"""

N = int(input())
ans = 0

# y = x の 上側の格子点の数（直線上は含まない）
for i in range(1, int(N**0.5) + 1):
    ans += (N // i) - i

# y = x の 下側
ans *= 2

# y = x の 個数
ans += int(N ** 0.5)

print(ans)
