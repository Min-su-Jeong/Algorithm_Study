"""
1.전략
- DFS
- 숫자문자열들이 담긴 res 배열 => 오름차순 정렬
- 첫번째와 마지막 인덱스를 나눠 출력

2.시간복잡도
- check 함수 : O(1)
- dfs 함수 : O(10^k) = 10^8 = 100,000,000
  => 1초 이내 가능
"""
def check(a, b, op):
    if op == '<':
        if a > b: 
            return False
    if op == '>':
        if a < b: 
            return False
        
    return True

def dfs(cnt, num):
    if cnt == k+1:
        res.append(num)
        return
  
    for i in range(10):
        if visited[i]: 
            continue

        if cnt == 0 or check(num[cnt-1], str(i), signs[cnt-1]):
            visited[i] = 1
            dfs(cnt+1, num+str(i))
            visited[i] = 0

# 입력 받기
k = int(input())
signs = list(input().split())

# 파라미터 초기화
res = []
visited = [0]*10

# 순회 시작
dfs(0, '')
res.sort()

# 결과 출력
print(res[-1])
print(res[0])