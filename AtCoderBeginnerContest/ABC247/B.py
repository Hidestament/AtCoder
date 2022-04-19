"""
B - Unique Nicknames
https://atcoder.jp/contests/abc247/tasks/abc247_b
"""

N = int(input())
names = []
for _ in range(N):
    s, t = map(str, input().split())
    names.append([s, t])


flag = True
for i in range(N):
    s, t = names[i]
    # ai = s にした場合
    if all(s != names[j][0] for j in range(N) if j != i) and all(s != names[j][1] for j in range(N) if j != i):
        continue
    # ai = t にした場合
    if all(t != names[j][0] for j in range(N) if j != i) and all(t != names[j][1] for j in range(N) if j != i):
        continue

    flag = False

print("Yes" if flag else "No")
