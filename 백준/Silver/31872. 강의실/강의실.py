import sys
input = sys.stdin.readline

N, K = map(int, input().split())
room = list(map(int, input().split()))
room.sort()

dist = [room[0]]
for i in range(1, N):
    dist.append(room[i] - room[i - 1])

dist.sort(reverse=True)
skip = sum(dist[:K])

ret = room[-1] - skip
print(ret)