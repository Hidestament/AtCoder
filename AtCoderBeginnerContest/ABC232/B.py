"""
B - Caesar Cipher
https://atcoder.jp/contests/abc232/tasks/abc232_b
"""

S = str(input())
T = str(input())

table = {chr(i + ord("a")): i for i in range(26)}
K = (table[T[0]] - table[S[0]]) % 26

new_s = ""
for s in S:
    sd = (table[s] + K) % 26
    new_s += chr(sd + ord("a"))

print("Yes" if new_s == T else "No")
