def solution(sequence, k):
    res = []
    n = len(sequence)
    prefix_sum, end = 0, 0
    
    for i in range(n):
        # 누적합이 k보다 작을 때 동안 반복하며 
        # end 변수를 통해 마지막 인덱스 값 기록 
        while prefix_sum < k and end < n:
            prefix_sum += sequence[end]
            end +=1 
        
        # 누적합이 k와 같은 경우
        if prefix_sum == k:
            # [시작 인덱스, 마지막 인덱스, 부분 수열의 길이] 형태로 추가
            res.append([i, end-1, end-1-i])
            
        # 다음 누적합을 구하기 위해 현재 시작 인덱스의 값 뺄셈    
        prefix_sum -= sequence[i]

    # 부분 수열의 길이가 짧은 순으로 정렬
    res = sorted(res, key=lambda x: x[2])
    
    return res[0][:2]