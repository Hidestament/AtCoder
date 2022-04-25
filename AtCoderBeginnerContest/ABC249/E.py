"""
E - RLE
https://atcoder.jp/contests/abc249/tasks/abc249_e
"""

N, P = map(int, input().split())

# DP[i][j]: S[i]まで考えたときに, T[j]となるモノの個数
# len(T) > N のモノは明らかに条件を満たさないので, len(T) = Nまで考えれば十分.
DP = [[0] * (N + 10) for _ in range(N + 10)]
DP[0][0] = 1


def solve_brute_force():
    """O(N^3)かかる愚直なDP. TLEする
    """
    for i in range(N + 10):  # Sの文字数
        for j in range(N + 10):  # Tの文字数
            for num in range(1, N + 10):  # 繋げる文字の数. 0は駄目
                dig = len(str(num))
                if i + num > N + 5:
                    continue
                if j + dig + 1 > N + 5:
                    continue
                if i == 0:
                    DP[i + num][j + dig + 1] += 26*DP[i][j]
                else:
                    DP[i + num][j + dig + 1] += 25*DP[i][j]
                DP[i + num][j + dig + 1] %= P


solve_brute_force()
ans = sum(DP[N][k] for k in range(N)) % P
print(ans)
