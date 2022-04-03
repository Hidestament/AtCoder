"""尺取法で解く
"""

N = int(input())


def X(a, b):
    return pow(a, 3) + (b * pow(a, 2)) + (pow(b, 2) * a) + pow(b, 3)


b = 10**6
ans = 10**18
for a in range(10**6):
    while (b > 0) and (X(a, b-1) >= N):
        b -= 1

    if X(a, b) >= N:
        ans = min(ans, X(a, b))

    if (a > b) or (b == 0):
        break

print(ans)
