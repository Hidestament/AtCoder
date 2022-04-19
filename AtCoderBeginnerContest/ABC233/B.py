"""
B - A Reverse
https://atcoder.jp/contests/abc233/tasks/abc233_b
"""

L, R = map(int, input().split())
S = str(input())

L -= 1
R -= 1

ans = S[:L] + S[L:R+1][::-1] + S[R+1:]
print(ans)
