def solution(answers):
    # 1번, 2번, 3번 수포자가 찍는 방식
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # 점수, 결과 리스트
    score = [0, 0, 0]
    
    # 맞춘 개수 저장
    for idx, ans in enumerate(answers): 
        if s1[idx % 5] == ans:  # 5개의 답이 반복되므로 idx % 5
            score[0] += 1
        if s2[idx % 8] == ans:  # 8개의 답이 반복되므로 idx % 8
            score[1] += 1
        if s3[idx % 10] == ans: # 10개의 답이 반복되므로 idx % 10
            score[2] += 1

    # 가장 많이 맞춘 사람의 개수 반환
    res = [(idx+1) for idx, s in enumerate(score) if s == max(score)]

    return res