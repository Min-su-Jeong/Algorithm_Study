def solution(num_list):
    ans = [0,0]        # 짝수와 홀수의 개수를 담을 리스트
    for n in num_list: # 리스트 중에서
        ans[n%2] += 1  # 짝수, 홀수 인덱스에 각각 1씩 증가
    return ans