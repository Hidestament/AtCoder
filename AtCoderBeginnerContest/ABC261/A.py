"""
A - Intersection
https://atcoder.jp/contests/abc261/tasks/abc261_a
"""

L1, R1, L2, R2 = map(int, input().split())

# 区間の重なりがある場合
ans = min(R1, R2) - max(L1, L2)
print(max(0, ans))
