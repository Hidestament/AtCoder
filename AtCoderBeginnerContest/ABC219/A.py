"""
A - AtCoder Quiz 2
https://atcoder.jp/contests/abc219/tasks/abc219_a
"""
X = int(input())
if X >= 90:
    print("expert")
elif X >= 70:
    print(90 - X)
elif X >= 40:
    print(70 - X)
else:
    print(40 - X)
