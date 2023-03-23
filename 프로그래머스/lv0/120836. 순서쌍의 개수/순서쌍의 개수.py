def solution(n):
    l = [i for i in range(1, n+1) if n % i == 0] # n의 약수를 찾아 리스트로 생성
    return len(l) # 리스트 길이 반환