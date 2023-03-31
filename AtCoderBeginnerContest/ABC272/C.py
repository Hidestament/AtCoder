"""
C - Max Even
https://atcoder.jp/contests/abc272/tasks/abc272_c
"""
import sys

input = sys.stdin.readline

N = int(input())
A = set(list(map(int, input().split())))

odd = sorted([a for a in A if a % 2 == 1], reverse=True)
even = sorted([a for a in A if a % 2 == 0], reverse=True)

if len(odd) < 2 and len(even) < 2:
    print(-1)
    exit()

odd = odd + [-1000000000, -1000000000]
even = even + [-100000000, -1000000000]

ans = max(odd[0] + odd[1], even[0] + even[1])
print(ans)
