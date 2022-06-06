"""
D - Happy Birthday! 2
https://atcoder.jp/contests/abc200/tasks/abc200_d
"""
from collections import deque

N = int(input())
A = [0] + list(map(int, input().split()))

cache = {}
dq = deque()
for i in range(1, N + 1):
    res = A[i] % 200
    array = [i]
    if res in cache:
        B = cache[res]
        print("Yes")
        print(len(B), *B)
        print(len(array), *array)
        exit()
    cache[res] = array
    dq.append([array, res])

while dq:
    now, res = dq.popleft()
    if len(now) == N:
        continue

    for i in range(now[-1] + 1, N + 1):
        next_array = now + [i]
        next_res = (res + A[i]) % 200
        if next_res in cache:
            B = cache[next_res]
            print("Yes")
            print(len(B), *B)
            print(len(next_array), *next_array)
            exit()
        cache[next_res] = next_array
        dq.append([next_array, next_res])

print("No")
