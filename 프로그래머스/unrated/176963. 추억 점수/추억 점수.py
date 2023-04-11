def solution(name, yearning, photo):
    # 2개의 for문을 통해 이름을 하나씩 접근 / 만약, 이름이 존재하면 해당하는 추억 점수 인덱스에 접근하여 합 구하기
    return [sum(yearning[name.index(i)] for i in p if i in name) for p in photo]
