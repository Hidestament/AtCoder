"""
D - ABC Transform
問題リンク: https://atcoder.jp/contests/abc242/tasks/abc242_d
"""

S = str(input())
Q = int(input())
char = ["A", "B", "C"]


def get_next(s):
    ind = char.index(s)
    return char[(ind + 1) % 3]


def dfs(t, k):
    """
    操作t回目のk番目（1-index）の文字を返す
    """
    if t == 0:
        return S[k]
    if k == 0:
        s = char.index(S[0])
        return char[(s + t) % 3]

    # 左の子: 親の次の文字
    if k % 2 == 0:
        return get_next(dfs(t-1, k//2))

    # 右の子: 親の次の次の文字
    if k % 2 == 1:
        return get_next(get_next(dfs(t-1, k//2)))


for _ in range(Q):
    t, k = map(int, input().split())
    print(dfs(t, k-1))
