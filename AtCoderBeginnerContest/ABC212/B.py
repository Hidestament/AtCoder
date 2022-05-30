"""
B - Weak Password
https://atcoder.jp/contests/abc212/tasks/abc212_b
"""

X = list(input())

flag = True
# Cond1: 全部同じ数字
if len(set(X)) == 1:
    flag = False

# Cond2: i -> i+1
if all((int(X[i - 1]) + 1) % 10 == int(X[i]) for i in range(1, 4)):
    flag = False

print("Strong" if flag else "Weak")
