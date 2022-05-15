"""
D - At Most 3 (Contestant ver.)
https://atcoder.jp/contests/abc251/tasks/abc251_d
参考: https://atcoder.jp/contests/abc251/editorial/3958
"""
W = int(input())

weights = set()
for i in range(1, 101):
    for d in range(3):
        weights.add(i * (100**d))

print(len(weights))
print(*weights)
