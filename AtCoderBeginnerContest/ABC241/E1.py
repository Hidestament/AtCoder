"""
E - Putting Candies
https://atcoder.jp/contests/abc241/tasks/abc241_e
循環を検出して解く
"""


def solve_simple(N, K, A):
    X = 0
    while K > 0:
        X += A[X % N]
        K -= 1
    return X


def solve_cycle(N, K, A):
    seen = [0] * N
    cycle, path = [], []
    X, pos = 0, 0
    while True:
        pos = X % N
        X += A[pos]

        seen[pos] += 1
        if seen[pos] == 3:
            break

        if seen[pos] == 1:
            path.append(pos)

        if seen[pos] == 2:
            cycle.append(pos)

    ans = sum(A[x] for x in path)
    c = (K - len(path)) // len(cycle)
    res = (K - len(path)) % len(cycle)
    ans += c * sum(A[x] for x in cycle) + sum(A[x] for x in cycle[:res])
    return ans


if __name__ == "__main__":
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # Kが小さいと逆に色々めんどくさいので愚直に解く
    if K <= 10**6:
        ans = solve_simple(N, K, A)
    else:
        ans = solve_cycle(N, K, A)

    print(ans)
