"""
E - Count Descendants
https://atcoder.jp/contests/abc202/tasks/abc202_e
条件1: Uiの部分木内の頂点 -> オイラーツアーの[S[Ui], E[Ui]]区間内の頂点
条件2: Depth = Di
"""
import sys

sys.setrecursionlimit(10**7)


class BinaryIndexedTree:
    """
    A = [a0, a1, a2, ..., an-1]
    元のAの配列は0-indexだが, BIT上では1-indexで扱う
    """

    def __init__(self, n=10**6):
        self.size = n + 1
        self.tree = [0] * (n + 1)
        self.depth = n.bit_length()

    def update(self, i, x):
        """
        ai += x を する
        i: 0-index
        """
        # 1-indexに直す
        pos = i + 1
        while pos <= self.size:
            self.tree[pos] += x
            # 真上の位置は, iにiのLSBを加えたモノ
            pos += pos & -pos

    def sum(self, i):
        """
        a[0] + a[1] + ... + a[i] を 求める
        i は 0-index
        """
        pos = i + 1
        s = 0
        while pos > 0:
            s += self.tree[pos]
            # 左上は i に iのLSBを引いたモノ
            pos -= pos & -pos
        return s

    def sum_range(self, i, j):
        """
        a[i] + a[i+1] + ... + a[j] を 求める
        i, j は 0-index
        """
        return self.sum(j) - self.sum(i - 1)

    def lower_bound(self, x):
        """
        a0 + a1 + ... + ai >= x となる最小のiを取得.
        各項は非負である必要がある
        iは0 - index
        """
        if x <= 0:
            return -1

        k = 1 << (self.size.bit_length() - 1)
        pos = 0
        s = 0
        while k > 0:
            # (pos + kが配列の長さを超えない) and 和がxを超えない
            if (pos + k < self.size) and self.tree[pos + k] + s < x:
                s += self.tree[pos + k]
                pos += k
            # 1つ下の段に行く
            k //= 2
        return pos


N = int(input())
P = list(map(int, input().split()))
Q = int(input())
graph = [[] for _ in range(N)]
for child, par in enumerate(P, start=1):
    graph[par - 1].append(child)

euler_tour = []
start_time = [0] * N
end_time = [0] * N
depth = [0] * N


def dfs(now):
    start_time[now] = len(euler_tour)
    euler_tour.append(now)
    for to in graph[now]:
        depth[to] = depth[now] + 1
        dfs(to)
        euler_tour.append(now)
    end_time[now] = len(euler_tour) - 1


dfs(0)


def solve_binary_search():
    """depthごとに, 頂点の訪問時間をソートして持っておき, 二分探索"""
    from collections import defaultdict
    from bisect import bisect_left, bisect_right

    # time_depth[d]: depth=dとなる頂点の訪問時間（ソート）
    time_depth = defaultdict(list)
    for v in range(N):
        time_depth[depth[v]].append(start_time[v])
    for d in time_depth.keys():
        time_depth[d] = sorted(time_depth[d])

    for _ in range(Q):
        u, d = map(int, input().split())
        s_time = start_time[u - 1]
        e_time = end_time[u - 1]
        # time_depth[d]内で, [s_time, e_time]に含まれるモノの個数
        left = bisect_left(time_depth[d], s_time)
        right = bisect_right(time_depth[d], e_time)
        print(right - left)


def solve_BIT():
    """クエリを先読みして, depthの小さい順に処理する
    => [s_time, e_time]に含まれる頂点の差分をBITで計算する
    """
    from collections import defaultdict

    queries = defaultdict(list)
    for i in range(Q):
        u, d = map(int, input().split())
        queries[d].append([u - 1, i])

    time_depth = defaultdict(list)
    for v in range(N):
        time_depth[depth[v]].append(start_time[v])

    bit = BinaryIndexedTree()
    ans = [None] * Q
    for d in range(N):
        if not queries[d]:
            continue

        # 更新前のbitの値を計算
        before_change = []
        for u, _ in queries[d]:
            s_time = start_time[u]
            e_time = end_time[u]
            s = bit.sum_range(s_time, e_time)
            before_change.append(s)

        # 更新
        for t in time_depth[d]:
            bit.update(t, 1)

        # 差分を計算
        for i, s in enumerate(before_change):
            u, q = queries[d][i]
            s_time = start_time[u]
            e_time = end_time[u]
            ans[q] = bit.sum_range(s_time, e_time) - s

    print(*ans)


# solve_binary_search()
solve_BIT()
