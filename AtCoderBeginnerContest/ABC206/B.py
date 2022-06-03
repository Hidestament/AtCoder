"""
B - Savings
https://atcoder.jp/contests/abc206/tasks/abc206_b
"""
N = int(input())

days = 0
while True:
    days += 1
    N -= days
    if N <= 0:
        print(days)
        break
