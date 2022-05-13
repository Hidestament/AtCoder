"""
B - Maritozzo
https://atcoder.jp/contests/abc219/tasks/abc219_b
"""
S = [str(input()) for _ in range(3)]
T = str(input())

ans = ""
for t in T:
    ans += S[int(t) - 1]
print(ans)
