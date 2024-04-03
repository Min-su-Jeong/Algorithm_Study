# 1로 이루어진 배수들을 n으로 나누었을 때 나머지가 0이 되는 경우를 찾는 문제
# 입력은 여러 번의 테스트 케이스로 이루어짐 => try ~ except 문

while True:
    try:
        n = int(input())
    except:
        break
        
    num = 1    # 1로만 이루어진 수
    answer = 1 # 자릿 수
    while True:
        if num%n != 0:
            num = num*10 + 1
            answer += 1
        else:
            break
    
    print(answer)