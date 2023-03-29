"""
A - Probably English
https://atcoder.jp/contests/abc295/tasks/abc295_a
"""
import sys

input = sys.stdin.readline

N = int(input())
W = list(map(str, input().split()))

for w in W:
    if w in ["and", "not", "that", "the", "you"]:
        print("Yes")
        exit()

print("No")
