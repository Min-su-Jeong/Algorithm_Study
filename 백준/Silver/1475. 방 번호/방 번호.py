nums = input()
arr = [0] * 10 # 0~9

for n in nums:
    n = int(n)
    if n == 6 or n == 9:     # 6 또는 9인 경우
        if arr[6] <= arr[9]: # 해당 인덱스 값이 더 작은 쪽에 +1
            arr[6] += 1
        else:
            arr[9] += 1
    else:
        arr[n] += 1
        
print(max(arr))