"""
E - White Pawn
https://atcoder.jp/contests/abc203/tasks/abc203_e
参考: https://note.com/momomo0214/n/na0801043bb76
"""
from collections import defaultdict


N, M = map(int, input().split())
black_pawn = defaultdict(list)
for _ in range(M):
    x, y = map(int, input().split())
    black_pawn[x].append(y)

now = set([N])
for x in sorted(black_pawn.keys()):
    del_pos = set()
    add_pos = set()
    for y in black_pawn[x]:
        if (y in now) and (y - 1 not in now) and (y + 1 not in now):
            del_pos.add(y)
        if (y not in now) and (y - 1 in now or y + 1 in now):
            add_pos.add(y)

    for y in del_pos:
        now.remove(y)
    for y in add_pos:
        now.add(y)

print(len(now))
