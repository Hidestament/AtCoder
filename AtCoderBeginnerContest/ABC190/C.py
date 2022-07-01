"""
C - Bowls and Dishes
https://atcoder.jp/contests/abc190/tasks/abc190_c
"""

N, M = map(int, input().split())
condition = [list(map(int, input().split())) for _ in range(M)]
K = int(input())
dishes = [list(map(int, input().split())) for _ in range(K)]

ans = 0
for bit in range(1 << K):
    dishes_flag = [0] * N
    for i in range(K):
        if bit & (1 << i):
            dishes_flag[dishes[i][0] - 1] = 1
        else:
            dishes_flag[dishes[i][1] - 1] = 1

    num_condition = 0
    for a, b in condition:
        if dishes_flag[a - 1] and dishes_flag[b - 1]:
            num_condition += 1
    ans = max(ans, num_condition)

print(ans)
