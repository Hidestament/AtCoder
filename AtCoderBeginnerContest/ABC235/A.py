"""
A - Rotate
https://atcoder.jp/contests/abc235/tasks/abc235_a
"""

abc = str(input())
ans = sum(111 * int(num) for num in abc)
print(ans)
