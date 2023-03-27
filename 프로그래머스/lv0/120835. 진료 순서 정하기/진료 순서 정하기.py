def solution(emergency):
    # emergency 내림차순 정렬
    se = sorted(emergency, reverse=True)
    # 배열의 크기만큼 큰 수부터 우선순위를 매겨 딕셔너리 형태로 정의
    dic = {str(se[i]) : i+1 for i in range(len(emergency))} 

    # emergency의 각 원소에 해당하는 value 값 반환
    return [dic[str(e)] for e in emergency]