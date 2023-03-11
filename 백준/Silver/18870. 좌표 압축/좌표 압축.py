import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split())) 
arr2 = sorted(list(set(arr))) # 중복값 제거 후 정렬
dic = {arr2[i] : i for i in range(len(arr2))} # 시간 단축을 위한 딕셔너리 인덱싱 사용

for i in arr:
    print(dic[i], end = ' ') # arr[i]의 key에 해당하는 value 출력