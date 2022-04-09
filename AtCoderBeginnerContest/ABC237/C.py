"""
C - kasaka
https://atcoder.jp/contests/abc237/tasks/abc237_c
"""

from collections import deque


S = str(input())

# 先頭と末尾のaはいらないので消す
dq = deque(S)
last_num = 0
while (dq) and (dq[-1] == "a"):
    dq.pop()
    last_num += 1

front_num = 0
while (dq) and (dq[0] == "a"):
    dq.popleft()
    front_num += 1

S = "".join(dq)
if front_num <= last_num:
    print("Yes" if S == S[::-1] else "No")
else:
    print("No")
