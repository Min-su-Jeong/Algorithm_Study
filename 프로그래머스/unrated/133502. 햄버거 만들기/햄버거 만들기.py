def solution(ingredient):
    s = []  # 재료 저장 리스트
    cnt = 0 # 포장할 수 있는 햄버거 개수 저장
    
    for i in ingredient:
        s.append(i)                # ingredient의 값을 순차적으로 s에 추가
        if s[-4:] == [1, 2, 3, 1]: # (빵-야채-고기-빵) 순서로 쌓인 햄버거
            cnt += 1               # cnt 1 증가
            del s[-4:]             # 조건에 해당되는 값 삭제
            
    return cnt