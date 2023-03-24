import re # 정규 표현식 모듈 사용
def solution(my_string):
    # 1. 정규 표현식을 사용하여 숫자만 추출하여 리스트화 
    # 2. 리스트에 있는 문자->숫자로 변환하여 합 구하기 
    return sum(int(i) for i in re.findall(r'\d', my_string))