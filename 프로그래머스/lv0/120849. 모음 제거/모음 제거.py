import re # 정규식 표현 모듈 이용
def solution(my_string):
    return re.sub(r"[a,e,i,o,u]", "", my_string) # 모음자리를 ''으로 치환하여 반환