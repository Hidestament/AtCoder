"""Binary Searchで解く
"""

N = int(input())


def X(a, b):
    return pow(a, 3) + (b * pow(a, 2)) + (pow(b, 2) * a) + pow(b, 3)


ans = 10**18
for a in range(10**6):
    left, right = 0, 10**6
    while (right - left) > 1:
        mid = (left + right) // 2
        if X(a, mid) >= N:
            right = mid
        else:
            left = mid

    if X(a, left) >= N:
        ans = min(ans, X(a, left))
    else:
        ans = min(ans, X(a, right))

print(ans)
