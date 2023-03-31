def solution(score):
    avg = [sum(s)/2 for s in score]                            # 각 요소의 평균 구하기
    return [sorted(avg, reverse=True).index(i)+1 for i in avg] # index 함수를 이용하여 등수 매기기


    
        