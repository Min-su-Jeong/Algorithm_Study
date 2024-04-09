# 연도에서 E, S, M을 각각 뺏을 때의 나머지가 0인 최솟 값을 찾는 문제
E, S, M = map(int, input().split())

year = 1

while True:
    findYear = (year-E)%15 == 0 and (year-S)%28 == 0 and (year-M)%19 == 0
    
    if findYear:
        break
    else:
        year += 1
    
print(year)