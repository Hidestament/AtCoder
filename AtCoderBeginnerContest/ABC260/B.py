"""
B - Better Students Are Needed!
https://atcoder.jp/contests/abc260/tasks/abc260_b
"""

N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

approve = set()
math_approve = [(A[i], i + 1) for i in range(N)]
math_approve.sort(key=lambda x: (-x[0], x[1]))

cnt = 0
for a, i in math_approve:
    if cnt == X:
        break
    approve.add(i)
    cnt += 1

english_approve = [(B[i], i + 1) for i in range(N)]
english_approve.sort(key=lambda x: (-x[0], x[1]))

cnt = 0
for b, i in english_approve:
    if cnt == Y:
        break
    if i in approve:
        continue
    approve.add(i)
    cnt += 1

total_approve = [(A[i] + B[i], i + 1) for i in range(N)]
total_approve.sort(key=lambda x: (-x[0], x[1]))

cnt = 0
for ab, i in total_approve:
    if cnt == Z:
        break
    if i in approve:
        continue
    approve.add(i)
    cnt += 1

print(*sorted(approve))
