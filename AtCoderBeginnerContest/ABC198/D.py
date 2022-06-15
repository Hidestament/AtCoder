"""
D - Send More Money
https://atcoder.jp/contests/abc198/tasks/abc198_d
"""
from itertools import permutations


S1 = str(input())
S2 = str(input())
S3 = str(input())

used = list(set(S1 + S2 + S3))
if len(used) > 10:
    print("UNSOLVABLE")
    exit()


def make_number(S):
    number = ""
    for s in S:
        number += table[s]
    return int(number)


for num in permutations(range(10), len(used)):
    table = {used[i]: str(s) for i, s in enumerate(num)}
    if table[S1[0]] == "0" or table[S2[0]] == "0" or table[S3[0]] == "0":
        continue

    N1 = make_number(S1)
    N2 = make_number(S2)
    N3 = make_number(S3)

    if N1 + N2 == N3:
        print(N1)
        print(N2)
        print(N3)
        exit()

print("UNSOLVABLE")
