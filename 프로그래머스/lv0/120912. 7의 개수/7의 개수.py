def solution(array):
    cnt = 0
    for i in array:                            # 각 리스트의 원소들에 대하여
        cnt += list(map(int, str(i))).count(7) # 문자->정수 맵핑을 통한 자릿수 분할 후 7의 개수 세기
    return cnt