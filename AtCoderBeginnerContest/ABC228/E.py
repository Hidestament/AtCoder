"""
E - Integer Sequence Fair
https://atcoder.jp/contests/abc228/tasks/abc228_e
"""

N, K, M = map(int, input().split())
MOD = 998244353


def solve_simple():
    """愚直な解法. TLEする
    """
    num_A = pow(K, N)  # 数列の個数
    ans = pow(M, num_A, MOD)  # それぞれの数列に点数をつける場合の数
    print(ans)


def solve_efficient():
    """逆元を使う. M^(K^N)を効率的に求めれば良い
    -> M^(P-1) == 1 (mod P) が成り立つ
    -> M^(K^N) == M^(q(P-1) + r) == M^(q(P-1)) * M^r == 1 * M^r
    """
    if M % MOD == 0:  # ans = pow() の部分を見ると明らか
        print(0)
        exit()

    num_A = pow(K, N, MOD - 1)
    ans = pow(M, num_A, MOD)
    print(ans)


solve_efficient()
