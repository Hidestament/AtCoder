"""
B - Bouzu Mekuri
https://atcoder.jp/contests/abc210/tasks/abc210_b
"""
N = int(input())
S = str(input())

for i, s in enumerate(S):
    if s == "1":
        print("Takahashi" if i % 2 == 0 else "Aoki")
        break
