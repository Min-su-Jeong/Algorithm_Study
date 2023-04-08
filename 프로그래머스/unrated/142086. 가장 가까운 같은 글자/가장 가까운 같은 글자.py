def solution(s):
    res = []
    word_dict = {} # 글자 사전
    
    for idx, word in enumerate(list(s)): # 리스트의 인덱스, 내용 꺼내기
        if word not in word_dict:        # 사전에 없는 글자인 경우
            res.append(-1)               # -1 추가
            word_dict[word] = idx        # 해당 글자 인덱스 자리에 인덱스 변경
            
        else:                                 # 사전에 글자가 있는 경우
            res.append(idx - word_dict[word]) # 몇 칸 앞에 있는지 계산하여 추가
            word_dict[word] = idx             # 해당 글자 인덱스 자리에 인덱스 변경
            
    return res