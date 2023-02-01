import sys
input = sys.stdin.readline

res = []
while True:
    num1 = int(input())
    if num1 == 0:
        break
    
    num2 = int(str(num1)[::-1]) # 숫자 뒤집기
    if num1 == num2:
        res.append('yes')
    else:
        res.append('no')

for i in res:
    print(i)