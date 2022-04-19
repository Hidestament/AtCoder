"""
A - 10yen Stamp
https://atcoder.jp/contests/abc233/tasks/abc233_a
"""

X, Y = map(int, input().split())
res = max(0, Y - X)

print(-(-res//10))
