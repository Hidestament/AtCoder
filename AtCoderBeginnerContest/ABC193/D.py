"""
D - Poker
https://atcoder.jp/contests/abc193/tasks/abc193_d
"""
from itertools import product
from collections import Counter

K = int(input())
S = str(input()).replace("#", "")
T = str(input()).replace("#", "")

win_prob = 0
all_prob = 0
for s, t in product(range(1, 10), range(1, 10)):
    s, t = str(s), str(t)
    S_cnt = Counter(S + s)
    T_cnt = Counter(T + t)

    s_score = sum(i * pow(10, S_cnt[str(i)]) for i in range(1, 10))
    t_score = sum(i * pow(10, T_cnt[str(i)]) for i in range(1, 10))

    cards = Counter(S + T)
    if s == t:
        prob = (K - cards[s]) * (K - cards[s] - 1)
    else:
        prob = (K - cards[s]) * (K - cards[t])

    all_prob += prob
    if s_score > t_score:
        win_prob += prob

print(win_prob / all_prob)
