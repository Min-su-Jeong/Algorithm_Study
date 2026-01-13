"""
1. 명함을 돌릴 수 있음 (가로, 세로 swap)
2. 길이 비교
  - 가로 길이 < 세로 길이: 돌려서 리스트에 저장
  - 가로 길이 > 세로 길이: 리스트에 저장
3. 가로 리스트와 세로 리스트에서 각각 최댓값 곱 구하기
"""
def solution(sizes):
    wList, hList = [], []
    for w, h in sizes:
        if w < h:
            wList.append(h)
            hList.append(w)
        else:
            wList.append(w)
            hList.append(h)
        
    return max(wList) * max(hList)