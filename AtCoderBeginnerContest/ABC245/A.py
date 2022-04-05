"""
A - Good morning
問題リンク: https://atcoder.jp/contests/abc245/tasks/abc245_a
"""

A, B, C, D = map(int, input().split())
takahashi = A * 60 * 60 + B * 60
aoki = C * 60 * 60 + D * 60 + 1

print("Takahashi" if takahashi < aoki else "Aoki")
