"""
C - Friends and Travel costs
https://atcoder.jp/contests/abc203/tasks/abc203_c
"""

N, K = map(int, input().split())
friends = [list(map(int, input().split())) for _ in range(N)]
friends.sort()

town = 0
for a, b in friends:
    if town == a:
        K += b
        continue
    cost = a - town
    if K - cost < 0:
        break
    else:
        town = a
        K += b - cost

if K:
    town += K

print(town)
