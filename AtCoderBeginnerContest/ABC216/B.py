"""
B - Same Name
https://atcoder.jp/contests/abc216/tasks/abc216_b
"""
N = int(input())
names = set()

flag = False
for _ in range(N):
    s, t = map(str, input().split())
    flag |= (s, t) in names
    names.add((s, t))

print("Yes" if flag else "No")
