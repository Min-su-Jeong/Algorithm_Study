# 생성자 범위: (주어진 수(N)-자릿수*9) ~ 주어진 수(N)
n = int(input())

for i in range(n - len(str(n))*9, n):
    check = i
    for k in str(i):
        if k == '-': # 음수인 경우
            continue
        else:
            check += int(k)
            
    if check == int(n):
        print(i)
        break
        
else: # 생성자가 없는 경우
    print(0)