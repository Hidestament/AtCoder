"""
B - Get Closer
問題リンク: https://atcoder.jp/contests/abc246/tasks/abc246_b
複素数でとく
"""

A, B = map(int, input().split())
z = A + B * 1j

ans = z / abs(z)
print(ans.real, ans.imag)
