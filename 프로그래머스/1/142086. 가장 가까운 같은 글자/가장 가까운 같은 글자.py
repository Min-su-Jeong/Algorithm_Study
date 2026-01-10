"""
- 글자 등장 여부 확인: 해시 테이블 사용
- 몇 번째 앞에 있는지: 동일 글자끼리의 인덱스 기록 필요
  - 글자가 없으면: -1
  - 글자가 있으면: i - 이전 글자의 index
- 이전 글자 index를 기록하려면?
  - 위 로직 계산 후 dict에 index 값 기록
"""
def solution(s):
    ret = []
    dic = {}
    
    for i, c in enumerate(s):
        if c not in dic:
            ret.append(-1)
        else:
            ret.append(i-dic[c])
        dic[c] = i
        
    return ret