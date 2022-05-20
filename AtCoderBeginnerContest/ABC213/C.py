"""
C - Reorder Cards
https://atcoder.jp/contests/abc213/tasks/abc213_c
"""
H, W, N = map(int, input().split())
used_h, used_w = [0], [0]
cards = []
for _ in range(N):
    a, b = map(int, input().split())
    used_h.append(a)
    used_w.append(b)
    cards.append([a, b])


def compress(A):
    B = sorted(set(A))
    zipped = {}
    unzipped = {}
    for i, x in enumerate(B):
        zipped[x] = i
        unzipped[i] = x
    return zipped, unzipped


zipped_h, _ = compress(used_h)
zipped_w, _ = compress(used_w)
for a, b in cards:
    print(zipped_h[a], zipped_w[b])
