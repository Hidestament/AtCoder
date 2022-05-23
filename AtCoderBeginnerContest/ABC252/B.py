"""
B - Takahashi's Failure
https://atcoder.jp/contests/abc252/tasks/abc252_b
"""
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

taberu = set([i + 1 for i, a in enumerate(A) if a == max(A)])
print("Yes" if any(i in taberu for i in B) else "No")
