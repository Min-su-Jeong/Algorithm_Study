from collections import Counter # Counter 모듈 사용

def solution(s):
    # Counter.items() 함수를 사용하여 한 번만 등장하는 문자를 찾아낸 후 오름차순 정렬 및 병합하여 반환
    return ''.join(sorted([dic[0] for dic in Counter(s).items() if dic[1] == 1]))