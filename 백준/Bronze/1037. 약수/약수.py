# 진짜 약수의 최솟 값과 최댓 값을 곱하면 되는 문제
## 진짜 약수의 개수가 1개인 경우, 그 값에 제곱하면 N이 된다.
## 진짜 약수의 개수가 2개 이상인 경우, 가장 큰 값과 가장 작은 값을 곱하면 N이 된다.

n = int(input())
divisor = list(map(int, input().split()))
answer = max(divisor) * min(divisor)
print(answer)