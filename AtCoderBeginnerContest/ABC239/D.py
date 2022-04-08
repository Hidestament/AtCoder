"""
D - Prime Sum Game
https://atcoder.jp/contests/abc239/tasks/abc239_d
高橋がaを選んだときに, a + b が素数となるようなbを選べない
そのようなaが存在するとき, 高橋の勝ち
"""

A, B, C, D = map(int, input().split())


def get_primes(N):
    primes = []
    is_prime = [True] * (N + 1)
    is_prime[0] = False
    is_prime[1] = False

    for p in range(0, N + 1):
        if not is_prime[p]:
            continue
        primes.append(p)
        for i in range(p*p, N + 1, p):
            is_prime[i] = False

    return primes


primes = get_primes(300)
for a in range(A, B+1):
    flag = True
    for b in range(C, D+1):
        if (a + b) in primes:
            flag = False
            break

    if flag:
        print("Takahashi")
        exit()

print("Aoki")
