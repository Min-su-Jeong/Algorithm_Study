import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num_list = list(map(int, input().split()))

# 누적합 리스트 만들기
prefix_sum = [0]
tmp = 0
for i in num_list:
    tmp += i
    prefix_sum.append(tmp)
    
for _ in range(m):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i-1])