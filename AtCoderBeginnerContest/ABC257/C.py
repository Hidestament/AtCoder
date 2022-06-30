"""
C - Robot Takahashi
https://atcoder.jp/contests/abc257/tasks/abc257_c
"""

from collections import defaultdict


N = int(input())
S = str(input())
W = list(map(int, input().split()))

weight = defaultdict(list)
for i in range(N):
    weight[W[i]].append(S[i])

all_children = S.count("0")

adult, children = 0, 0
ans = adult + (all_children - children)
for w in sorted(weight.keys(), reverse=True):
    for s in weight[w]:
        if s == "0":
            children += 1
        else:
            adult += 1
    num_correct = adult + (all_children - children)
    ans = max(ans, num_correct)

print(ans)
