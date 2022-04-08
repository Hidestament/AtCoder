"""
D - AND and SUM
https://atcoder.jp/contests/abc238/tasks/abc238_d
xとyの対称性を除けば, [x, y]を一意に決められる
それを頑張って実装する. この際繰り上がりのみを持っておけば良い
"""

T = int(input())
for _ in range(T):
    a, s = map(int, input().split())

    flag = True
    kuriagari = 0
    for i in range(61):
        # a[i] = 1 なら, x = y = 1 しかない
        if a & (1 << i):
            if s & (1 << i):
                if kuriagari:
                    kuriagari = 1
                else:
                    flag = False
            else:
                if kuriagari == 0:
                    kuriagari = 1
                else:
                    flag = False
        # [x, y] = [1, 0], [0, 0]
        else:
            if s & (1 << i):
                if kuriagari:
                    kuriagari = 0
                else:
                    kuriagari = 0
            else:
                if kuriagari:
                    kuriagari = 1
                else:
                    kuriagari = 0

    if kuriagari:
        print("No")
    else:
        print("Yes" if flag else "No")
