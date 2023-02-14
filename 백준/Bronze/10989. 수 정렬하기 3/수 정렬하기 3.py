import sys
input = sys.stdin.readline
l = [0] * 10001
for _ in range(int(input())):
    l[int(input())] += 1 # 입력받은 값을 리스트의 인덱스로 하여 1씩 증가

for i in range(10001):
    if l[i] != 0: # 인덱스에 0이 아닌 숫자만 선택
        for j in range(l[i]): 
            print(i) # 있으면 해당 숫자만큼 반복 출력