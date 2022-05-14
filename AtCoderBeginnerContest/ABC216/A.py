"""
A - Signed Difficulty
https://atcoder.jp/contests/abc216/tasks/abc216_a
"""
X, Y = map(int, input().split("."))
if Y >= 7:
    print(str(X) + "+")
elif Y >= 3:
    print(str(X))
else:
    print(str(X) + "-")
