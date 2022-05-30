"""
A - Median?
https://atcoder.jp/contests/abc253/tasks/abc253_a
"""
a, b, c = map(int, input().split())
abc = sorted([a, b, c])
print("Yes" if abc[1] == b else "No")
