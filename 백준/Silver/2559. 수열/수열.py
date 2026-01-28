N, K = map(int, input().split())
arr = [0] + list(map(int, input().split()))

ret = 100000 * -100
psum = [0] * (N+1)

for i in range(1, N+1):
    psum[i] += psum[i-1] + arr[i]

for i in range(K, N+1):
    ret = max(ret, psum[i] -  psum[i-K])

print(ret)