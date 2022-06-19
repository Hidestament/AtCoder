"""
A - Health M DeathA - Health M Death
https://atcoder.jp/contests/abc195/tasks/abc195_a
"""

M, H = map(int, input().split())
print("Yes" if H % M == 0 else "No")
