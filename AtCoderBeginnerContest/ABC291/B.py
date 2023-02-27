"""
B - Trimmed Mean
https://atcoder.jp/contests/abc291/tasks/abc291_b
"""

N = int(input())
X = list(map(int, input().split()))

X = sorted(X)[N:]
X = sorted(X, reverse=True)[N:]

print(sum(X) / len(X))
