"""
C - Select Mul
https://atcoder.jp/contests/abc221/tasks/abc221_c
"""
N = str(input())
dig = len(N)


ans = 0
for bit in range(1, (1 << dig) - 1):
    left, right = [], []
    for i in range(dig):
        if bit & (1 << i):
            left.append(N[i])
        else:
            right.append(N[i])

    left = int("".join(sorted(left, reverse=True)))
    right = int("".join(sorted(right, reverse=True)))
    ans = max(ans, left * right)

print(ans)
