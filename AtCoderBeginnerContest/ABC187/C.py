"""
C - 1-SAT
https://atcoder.jp/contests/abc187/tasks/abc187_c
"""

N = int(input())

appear = set()
not_appear = set()
for _ in range(N):
    s = str(input())
    if s[0] == "!":
        not_appear.add(s[1:])
    else:
        appear.add(s)

for s in appear:
    if s in not_appear:
        print(s)
        exit()

print("satisfiable")
