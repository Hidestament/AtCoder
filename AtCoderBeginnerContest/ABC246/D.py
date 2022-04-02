N = int(input())


def x(a, b):
    return pow(a, 3) + (b * pow(a, 2)) + (pow(b, 2) * a) + pow(b, 3)


best = 10**18
for a in range(10**6):
    left, right = 0, 10**7
    while right - left > 1:
        mid = (left + right) // 2
        if x(a, mid) < N:
            left = mid
        else:
            right = mid

    if x(a, left) >= N:
        best = min(x(a, left), best)
    else:
        best = min(x(a, right), best)

print(best)
