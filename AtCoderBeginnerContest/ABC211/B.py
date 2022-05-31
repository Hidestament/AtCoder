"""
B - Cycle Hit
https://atcoder.jp/contests/abc211/tasks/abc211_b
"""
s = set()
for _ in range(4):
    s.add(str(input()))
print("Yes" if len(s) == 4 else "No")
