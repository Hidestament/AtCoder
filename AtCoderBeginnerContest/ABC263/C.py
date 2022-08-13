"""
C - Monotonically Increasing
https://atcoder.jp/contests/abc263/tasks/abc263_c
"""


def solve_by_dfs():
    N, M = map(int, input().split())

    def dfs(sequence):
        if len(sequence) == N:
            sequence = list(map(int, sequence))
            if sequence[-1] == 0:
                sequence[-1] = 10
            print(*sequence)
            return

        last = int(sequence[-1])
        res = M - (N - len(sequence)) + 1
        for i in range(last + 1, res + 1):
            if i == 10:
                i = 0
            dfs(sequence + str(i))

    for i in range(1, M - N + 2):
        if i == 10:
            i = 0
        dfs(str(i))


def solve_by_itertools():
    from itertools import combinations

    N, M = map(int, input().split())
    for sequence in combinations(range(1, M + 1), N):
        print(*sequence)


solve_by_itertools()
