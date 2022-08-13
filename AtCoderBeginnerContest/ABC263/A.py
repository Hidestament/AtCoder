"""
A - Full House
https://atcoder.jp/contests/abc263/tasks/abc263_a
"""

from collections import Counter

cards = list(map(int, input().split()))

cnt = Counter(cards)
if sorted(cnt.values()) == [2, 3]:
    print("Yes")
else:
    print("No")
