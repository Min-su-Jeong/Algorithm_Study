def solution(numbers):
    n = sorted(numbers)                    # 오름차순 정렬
    return max(n[0] * n[1], n[-1] * n[-2]) # 양쪽 끝 두 숫자의 곱을 비교하여 최댓값 반환
    