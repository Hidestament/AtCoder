"""
E - Addition and Multiplication 2
https://atcoder.jp/contests/abc257/tasks/abc257_e
"""

N = int(input())
C = list(map(int, input().split()))

x = []
min_c = min(C)
cost = 0
while cost + min_c <= N:
    x.append("0")
    cost += min_c

C = [[i + 1, c] for i, c in enumerate(C)]
C.sort(reverse=True)
for dig in range(len(x)):
    s = int(x[dig])
    for i, c in C:
        if cost + (c - min_c) <= N:
            x[dig] = str(i)
            cost += c - min_c
            break

print("".join(x))
