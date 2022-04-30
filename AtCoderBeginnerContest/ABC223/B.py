"""
B - String Shifting
https://atcoder.jp/contests/abc223/tasks/abc223_b
"""

S = str(input())

order = []
for i in range(len(S)):
    order.append(S[i:] + S[:i])

order.sort()
print(order[0])
print(order[-1])
