"""
1.전략
- 브루트포스(Brute Force)
- 알파벳, 숫자의 개수를 변수로 선언 후 차량 번호판 형식의 연속 여부를 확인
- 연속인 경우: 알파벳이면 알파벳의 개수 - 1, 숫자면 숫자의 개수 - 1
- 연속이 아닌 경우: 알파벳이면 알파벳의 개수, 숫자면 숫자의 개수

2.시간 복잡도
- 시간 제한: 1초
- O(N): N은 차량 번호판의 길이
"""
import sys
input = sys.stdin.readline

# Input
format = input().rstrip()

# Variables
numAlpha, numDigit = 26, 10
prev = format[0]
res = numAlpha if prev == 'c' else numDigit

# Solution
for f in format[1:]:
    if prev == f:
        if f == 'c':
            res *= numAlpha - 1
        else:
            res *= numDigit - 1
    
    else:
        if f == 'c':
            res *= numAlpha
        else:
            res *= numDigit

    prev = f
         
# Output
print(res)