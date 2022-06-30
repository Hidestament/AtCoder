"""
A - A to Z String 2
https://atcoder.jp/contests/abc257/tasks/abc257_a
"""

N, X = map(int, input().split())
string = ""
for i in range(26):
    string += chr(ord("A") + i) * N

print(string[X - 1])
