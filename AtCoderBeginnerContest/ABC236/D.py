"""PypyでAC
D - Dance
https://atcoder.jp/contests/abc236/tasks/abc236_d
"""

import sys
sys.setrecursionlimit(10**7)


N = int(input())
# A = (2N, 2N)にしといた方が楽
A = []
for _ in range(2*N - 1):
    a = list(map(int, input().split()))
    a = [-1] * (2*N - len(a)) + a
    A.append(a)


def dfs(points, people):
    global ans
    if len(people) == 0:
        ans = max(ans, points)
        return

    # 一人目の人は一番前の人とする
    i = people[0]
    for j in people[1:]:
        next_people = [x for x in people if (x != i) and (x != j)]
        dfs(points ^ A[i][j], next_people)


ans = 0
people = [i for i in range(2*N)]
dfs(0, people)
print(ans)
