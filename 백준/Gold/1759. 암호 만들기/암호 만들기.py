"""
1.전략
- 백트래킹(Backtracking)
- res의 길이가 l과 같아지면 출력 및 반환
- 자음 최소 1개, 모음 최소 2개를 포함해야 하므로 개수 count
- 단어 완성 시, 자음 및 모음 counting => 자음: 최소 1개 이상, 모음: 최소 2개 이상인 경우 출력

2.시간복잡도
- O(c^l) = C개 중 L개를 선택하는 조합의 수에 비례
  => 2초 이내 가능
"""
import sys; input = sys.stdin.readline

def backTracking(idx):
    if len(res) == L:
        vo, co = 0, 0
        
        for i in range(L):
            if res[i] in constant:
                vo += 1
            else:
                co += 1
                
        if vo >= 1 and co >= 2:
            print(''.join(res))
        return
    
    for i in range(idx, C):
        res.append(alpha[i])
        backTracking(i + 1)
        res.pop()

L, C = map(int, input().split())
alpha = sorted(list(input().split()))
constant = ['a', 'i', 'o', 'u', 'e']
res = []

backTracking(0)