"""
C - Just K
https://atcoder.jp/contests/abc249/tasks/abc249_c
"""

N, K = map(int, input().split())
S = [str(input()) for _ in range(N)]

ans = 0
for bit in range(1, 1 << N):
    apper = set()
    for i in range(N):
        if bit & (1 << i):
            for s in S[i]:
                apper.add(s)

    tmp_ans = 0
    for s in apper:
        cnt = 0
        for i in range(N):
            if bit & (1 << i):
                if s in S[i]:
                    cnt += 1

        if cnt == K:
            tmp_ans += 1

    ans = max(ans, tmp_ans)

print(ans)
