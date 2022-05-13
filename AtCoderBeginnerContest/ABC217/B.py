"""
B - AtCoder Quiz
https://atcoder.jp/contests/abc217/tasks/abc217_b
"""
atcoder = ["ABC", "ARC", "AGC", "AHC"]
for _ in range(3):
    s = str(input())
    atcoder.pop(atcoder.index(s))
print(atcoder[0])
