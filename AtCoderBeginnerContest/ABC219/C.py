"""
C - Neo-lexicographic Ordering
https://atcoder.jp/contests/abc219/tasks/abc219_c
"""
X = str(input())
N = int(input())

zipped = {chr(ord("a") + i): X[i] for i in range(26)}
unzipped = {X[i]: chr(ord("a") + i) for i in range(26)}

S = []
for _ in range(N):
    s = str(input())
    zipped_s = ""
    for x in s:
        zipped_s += unzipped[x]
    S.append(zipped_s)

S.sort()
for s in S:
    ans = ""
    for x in s:
        ans += zipped[x]
    print(ans)
