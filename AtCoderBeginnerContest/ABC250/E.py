"""
E - Prefix Equality
https://atcoder.jp/contests/abc250/tasks/abc250_e
"""
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
Q = int(input())


def hash_solve():
    """hash値を利用する解法
    参考:
        https://atcoder.jp/contests/abc250/editorial/3940
    """

    def to_hash(x):
        return x * (x + 1346) * (x + 9185)

    def make_hash_list(X):
        hash_list = []
        s = set()
        now_hash = 0
        for x in X:
            if x not in s:
                now_hash += to_hash(x)
                s.add(x)
            hash_list.append(now_hash)
        return hash_list

    a_hash = make_hash_list(A)
    b_hash = make_hash_list(B)

    for _ in range(Q):
        x, y = map(int, input().split())
        print("Yes" if a_hash[x - 1] == b_hash[y - 1] else "No")


def size_solve():
    """集合のサイズを用いる解法
    参考:
        https://atcoder.jp/contests/abc250/editorial/3906
    """

    def make_size(A):
        size, s, new_elements = [], set(), []
        for a in A:
            if a not in s:
                new_elements.append(a)
            s.add(a)
            size.append(len(s))
        return size, new_elements

    a_size, ak = make_size(A)
    b_size, bk = make_size(B)

    s, S = set(), {}
    for k in range(min(len(ak), len(bk))):
        size = k + 1
        a, b = ak[k], bk[k]
        if a in s:
            s.remove(a)
        else:
            s.add(a)
        if b in s:
            s.remove(b)
        else:
            s.add(b)

        S[size] = len(s)

    for _ in range(Q):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        if a_size[x] != b_size[y]:
            print("No")
            continue
        print("Yes" if S[a_size[x]] == 0 else "No")


def renumber_solve():
    """値を振り直して, 種類数と最大値で解く方法
    参考:
        https://atcoder.jp/contests/abc250/editorial/3948
    """
    table = {}
    for i in range(N):
        a = A[i]
        if a not in table:
            table[a] = len(table)
        A[i] = table[a]

    base = 10**8
    for i in range(N):
        b = B[i]
        if b in table:
            B[i] = table[b]
        else:
            B[i] = base

    def make_size_maxnum(A):
        max_nums, size = [], []
        s = set()
        max_num = -(10**9)
        for a in A:
            s.add(a)
            max_num = max(max_num, a)
            max_nums.append(max_num)
            size.append(len(s))
        return max_nums, size

    A_max, A_size = make_size_maxnum(A)
    B_max, B_size = make_size_maxnum(B)

    for _ in range(Q):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        if (A_max[x] == B_max[y]) and (A_size[x] == B_size[y]):
            print("Yes")
        else:
            print("No")


# hash_solve()
# size_solve()
renumber_solve()
