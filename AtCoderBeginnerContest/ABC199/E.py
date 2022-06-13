"""
D - RGB Coloring 2
https://atcoder.jp/contests/abc199/tasks/abc199_d
参考: https://blog.hamayanhamayan.com/entry/2021/04/25/002423
"""
from collections import defaultdict

N, M = map(int, input().split())
condition = defaultdict(list)
for _ in range(M):
    x, y, z = map(int, input().split())
    condition[x].append([y, z])


# 新しくxを追加したときに条件を満たすかのcheck
def check(x: int):
    for i, yz in enumerate(condition[len(used_number) + 1]):
        y, z = yz
        if now_cond[i] + (x <= y) > z:
            return False
    return True


# DP[s]: 既に使用した数の集合がsであるときの答えの個数
DP = [0] * (1 << N)
DP[0] = 1

for s in range((1 << N) - 1):
    if DP[s] == 0:  # DP[s] = 0ならそれ以上考えても意味ない
        continue
    used_number = [i + 1 for i in range(N) if s & (1 << i)]

    now_cond = []
    for y, z in condition[len(used_number) + 1]:
        now_cond.append(sum(x <= y for x in used_number))

    # 次に来る数字
    for next_num in range(N):
        if s & (1 << next_num):  # 既に使っている数字だったら駄目
            continue

        if check(next_num + 1):
            DP[s | 1 << next_num] += DP[s]

print(DP[-1])
