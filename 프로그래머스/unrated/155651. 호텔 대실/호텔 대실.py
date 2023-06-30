from heapq import heappop, heappush

def solution(book_time):
    cnt = 1
    
    # 대실 시각 분단위로 변환
    times = [(int(s[:2]) * 60 + int(s[3:]), int(e[:2]) * 60 + int(e[3:])) for s, e in book_time]
    # 대실 시작시간 기준 오름차순 정렬
    times.sort()
    
    # 객실 할당
    heap = []
    for s, e in times:
        if not heap:         # 할당한 객실이 존재하지 않는 경우
            heappush(heap,e) # 객실 할당
            continue
        if heap[0] <= s:     # 가장 빠른 대실 종료 시간 <= 현재 대실 시작 시간
            heappop(heap)    # 현재 손님에게 객실 할당
        else:                # 가장 빠른 대실 종료 시간 > 현재 대실 시작 시간
            cnt += 1         # 객실 +1
        heappush(heap,e+10)  # 새로운 객실 추가

    return cnt