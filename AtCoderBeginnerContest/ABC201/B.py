"""
B - Do you know the second highest mountain?
https://atcoder.jp/contests/abc201/tasks/abc201_b
"""

N = int(input())
mountain = [list(map(str, input().split())) for _ in range(N)]
mountain.sort(key=lambda x: int(x[1]), reverse=True)

print(mountain[1][0])
