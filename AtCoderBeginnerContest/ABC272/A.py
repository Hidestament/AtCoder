"""
A - Integer Sum
https://atcoder.jp/contests/abc272/tasks/abc272_a
"""
import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
print(sum(A))
