def solution(arr, divisor):
    res = [a for a in arr if a % divisor == 0]
    return sorted(res) if res else [-1]

            