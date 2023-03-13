"""
B - Playing Cards Validation
https://atcoder.jp/contests/abc277/tasks/abc277_b
"""

N = int(input())
S = [input() for _ in range(N)]

if len(set(S)) != N:
    print("No")
    exit()


condition1 = set(["H", "D", "C", "S"])
condition2 = set(["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "T", "J", "Q", "K"])


for s in S:
    if s[0] not in condition1:
        print("No")
        exit()
    if s[1] not in condition2:
        print("No")
        exit()

print("Yes")
