"""
001 - Yokan Party（★4）
https://atcoder.jp/contests/typical90/tasks/typical90_a
最小値（ピースのうち最小のもの）の最大化 -> Binary Search
"""

N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))


def check(x):
    """
    最小値がx以上となるように来れるか
    -> xごとに切っていき, ピースがK+1以上になればOK
    """
    cut = [0]  # 切れ目のリスト
    for a in A:
        if (a - cut[-1]) >= x:
            cut.append(a)

    # 全部の区間がx以上で 切れ目がK個以上あったら True
    if all((cut[i+1] - cut[i]) >= x for i in range(len(cut) - 1)):
        return len(cut) - 2 >= K
    else:
        return False


# opt = k 以上となるように切れるか?
# f(left): 常にTrue, f(right): 常にFalse
left, right = 0, 10**10
while (right - left) > 1:
    mid = (left + right) // 2
    if check(mid):
        left = mid
    else:
        right = mid

print(left)
