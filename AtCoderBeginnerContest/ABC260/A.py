"""
A - A Unique Letter
https://atcoder.jp/contests/abc260/tasks/abc260_a
"""

S = str(input())
for s in S:
    if S.count(s) == 1:
        print(s)
        break
else:
    print(-1)
