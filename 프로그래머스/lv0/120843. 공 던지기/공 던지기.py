def solution(numbers, k):
    # k번째 공 던지는 사람: 2*(k-1)번째 요소 / numbers의 길이 초과 불가능: % 연산자 사용
    return numbers[2 * (k - 1) % len(numbers)] 