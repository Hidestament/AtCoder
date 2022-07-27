"""
B - Quizzes
https://atcoder.jp/contests/abc184/tasks/abc184_b
"""

N, X = map(int, input().split())
S = str(input())

score = X
for s in S:
    if s == "o":
        score += 1
    else:
        score = max(0, score - 1)

print(score)
