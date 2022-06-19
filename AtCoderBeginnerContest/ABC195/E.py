"""
E - Lucky 7 Battle
https://atcoder.jp/contests/abc195/tasks/abc195_e
"""

N = int(input())
S = str(input())
X = str(input())

S = S[::-1]
X = X[::-1]

win_set = set([0])
for i in range(N):
    next_win_set = set()
    for r in range(7):
        if X[i] == "T":
            if ((10 * r) % 7) in win_set or ((10 * r + int(S[i])) % 7) in win_set:
                next_win_set.add(r)
        else:
            if ((10 * r) % 7) in win_set and ((10 * r + int(S[i])) % 7) in win_set:
                next_win_set.add(r)
    win_set = next_win_set

print("Takahashi" if 0 in win_set else "Aoki")
