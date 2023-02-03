import sys
i = int(input())

for _ in range(i):
    n, m = map(int, input().split())
    queue = list(map(int, sys.stdin.readline().split()))
    cnt = 0 # m이 몇 번째에 빠져나갔는지 저장하는 변수
    
    while m != -1:
        if queue[0] == max(queue): # 큐의 맨 앞이 제일 큰 경우
            del queue[0]
            m -= 1
            cnt += 1
            
        else: # 아닌 경우
            queue.append(queue[0]) # 맨 뒤로 보낸 후
            del queue[0]          # 맨 앞의 수 삭제
            
            if m == 0:             # m이 맨 앞인 경우
                m = len(queue) - 1 # 맨 뒤로 순서가 바뀜
            else:                  # 아닌 경우
                m -= 1             # 앞으로 순서를 당김

    print(cnt) # 각 case별로 결과 값 출력