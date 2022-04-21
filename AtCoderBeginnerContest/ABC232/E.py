"""
E - Rook Path
https://atcoder.jp/contests/abc232/tasks/abc232_e
"""

H, W, K = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
MOD = 998244353

# g0: (x2, y2), g1: (x2, _), g2: (_, y2), g3: (_, _)
g0, g1, g2, g3 = [0], [0], [0], [0]

if (x1 == x2) and (y1 == y2):
    g0[0] = 1
elif (x1 == x2):
    g1[0] = 1
elif (y1 == y2):
    g2[0] = 1
else:
    g3[0] = 1

for _ in range(1, K + 1):
    next_g0 = g1[-1] + g2[-1]
    next_g1 = (W - 1)*g0[-1] + (W - 2)*g1[-1] + g3[-1]
    next_g2 = (H - 1)*g0[-1] + (H - 2)*g2[-1] + g3[-1]
    next_g3 = (H - 1)*g1[-1] + (W - 1)*g2[-1] + (H + W - 4)*g3[-1]
    g0.append(next_g0 % MOD)
    g1.append(next_g1 % MOD)
    g2.append(next_g2 % MOD)
    g3.append(next_g3 % MOD)

print(g0[-1])
