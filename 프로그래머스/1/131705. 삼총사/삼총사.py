"""
- 조합 문제
- nC3
- 시간 복잡도: 1000C3 => 약 1.7억 (1.7초)
"""
def solution(number):
    ret = 0
    
    for i in range(len(number)):
        for j in range(i):
            for k in range(j):
                if number[i]+number[j]+number[k] == 0:
                    ret += 1
                    
    return ret