import sys
input = sys.stdin.readline

def solution():
    MAX = 1000000
    m = int(MAX**0.5)+1
    prime = [True for _ in range(MAX)]

    # 에라토스테네스의 체 공식 이용
    for i in range(2, m):
        if prime[i]:
            for j in range(i*i, MAX, i):
                prime[j] = False

    while True:
        n = int(input())
        if n == 0:
            break

        # 문제 조건 식
        for i in range(3, n):                       # a, b 모두 홀수이므로 3부터 시작
            if prime[i] and prime[n-i]:             # a, b 모두 소수인 경우
                print(f"{n} = {i} + {n-i}") # b-a가 가장 큰 수
                break
        else:
            print("Goldbach's conjecture is wrong.")
            
solution()