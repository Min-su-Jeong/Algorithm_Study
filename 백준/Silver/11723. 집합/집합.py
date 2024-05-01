"""
1.전략
- 집합
- 조건에 맞도록 연산 진행

2.시간복잡도
- O(N) = N = 3,000,000 (Worst case)
"""
import sys
input = sys.stdin.readline

s = set() # set 함수를 사용한 집합 표현

for _ in range(int(input())):
    op = input().strip().split() # 연산 입력 받기
    
    if len(op) == 1:
        if op[0] == "all":
            s = set([i for i in range(1, 21)])
        else: # empty 연산
            s = set() 
    
    else: # all, empty 연산을 제외한 나머지 연산들
        func, x = op[0], op[1]
        x = int(x)
        if func == "add":
            s.add(x)
        elif func == "remove":
            s.discard(x) # 해당 원소가 집합에 없어도 에러나지 않음(remove 대체)
        elif func == "check":
            print(1 if x in s else 0) # s에 x가 있으면 1, 없으면 0 출력
        elif func == "toggle":
            if x in s:
                s.discard(x)
            else:
                s.add(x)