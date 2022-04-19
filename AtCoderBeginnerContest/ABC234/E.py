"""
E - Arithmetic Number
https://atcoder.jp/contests/abc234/tasks/abc234_e
等差数列の個数はそんなに多くない -> 全列挙する
"""

from collections import deque


X = int(input())

# Xが一桁のときは, 別で処理した方が楽
if X <= 10:
    print(X)
    exit()

dq = deque()
for i in range(10, 100):
    dq.append(str(i))

while dq:
    now = dq.popleft()
    if int(now) >= X:
        print(now)
        break

    d = int(now[-1]) - int(now[-2])
    last = str(int(now[-1]) + d)
    if 0 <= int(last) <= 9:
        dq.append(now + last)
