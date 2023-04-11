def solution(name, yearning, photo):
    res, dic = [], {}            # 결과, 딕셔너리 변수
    for i, n in enumerate(name): # name 요소와 인덱스 반환
        dic[n] = yearning[i]     # 이름과 추억 점수를 딕셔너리 형태로 변환
        
    for p in photo:                
        score = 0                  # 추억 점수 초기화
        for name in p:             # 이름 하나씩 꺼내기
            if name in dic:        # 딕셔너리 내에 이름이 존재하면
                score += dic[name] # 해당하는 value 값을 score에 더하기
        res.append(score)          # 리스트에 점수 추가
        
    return res