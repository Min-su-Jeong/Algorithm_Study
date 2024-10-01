from collections import Counter

def solution(clothes):
    clothes_count = Counter([kind for name, kind in clothes])
    
    answer = 1
    for count in clothes_count.values():
        answer *= (count + 1)
    
    return answer - 1