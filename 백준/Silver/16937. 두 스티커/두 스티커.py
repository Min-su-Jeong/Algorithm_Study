import sys
input = sys.stdin.readline

# Input
H, W = map(int, input().split())
N = int(input())
size = [list(map(int, input().split())) for _ in range(N)]

# Variables
res = 0

# Solution
for i in range(N):
    for j in range(i+1, N):
        r1, c1 = size[i]
        r2, c2 = size[j]

        # 스티커 1, 2를 회전하지 않는 경우
        if (r1 + r2 <= H and max(c1, c2) <= W) or (max(r1, r2) <= H and c1 + c2 <= W):
            res = max(res, r1 * c1 + r2 * c2)

        # 스티커 1을 회전시키는 경우
        if (c1 + r2 <= H and max(r1, c2) <= W) or (max(c1, r2) <= H and r1 + c2 <= W):
            res = max(res, r1 * c1 + r2 * c2)

        # 스티커 2를 회전시키는 경우
        if (r1 + c2 <= H and max(c1, r2) <= W) or (max(r1, c2) <= H and c1 + r2 <= W):
            res = max(res, r1 * c1 + r2 * c2)

        # 두 스티커 모두 회전시키는 경우
        if (c1 + c2 <= H and max(r1, r2) <= W) or (max(c1, c2) <= H and r1 + r2 <= W):
            res = max(res, r1 * c1 + r2 * c2)

# Output
print(res)