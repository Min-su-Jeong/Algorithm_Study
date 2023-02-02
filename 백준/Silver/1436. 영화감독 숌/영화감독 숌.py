# 브루트 포스(Brute Force) 접근
import sys
input = sys.stdin.readline

n = int(input())
num = 666
cnt = 0

while n: # n이 0(False)이 아닐 때 까지 반복
    if "666" in str(num): # 숫자에 "666"이 포함되면
        n -= 1
    num += 1
    
print(num-1) # while 문을 빠져나올 때 다음 숫자가 출력되므로 -1 필요  