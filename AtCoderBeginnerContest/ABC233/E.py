"""
E - Σ[k=0..10^100]floor(X/10^k)
https://atcoder.jp/contests/abc233/tasks/abc233_e
"""

from collections import deque

X = deque(str(input()))
s = sum(int(x) for x in X)
kuriagari = 0

ans = []
while X:
    now_dig = (s + kuriagari) % 10
    ans.append(str(now_dig))

    kuriagari = (s + kuriagari) // 10
    # sの更新
    rm = int(X.pop())
    s -= rm

while kuriagari:
    now_dig = kuriagari % 10
    ans.append(str(now_dig))
    kuriagari //= 10

print("".join(ans[::-1]))
