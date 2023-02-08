import sys
input = sys.stdin.readline

for _ in range(int(input())):
    h, w, n = map(int, input().split())
    floor, num = n % h, n // h + 1
    if floor == 0: # h의 배수인 경우
        floor = h
        num = n // h
    
    print(floor*100+num)