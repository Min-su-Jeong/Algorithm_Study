import sys
input = sys.stdin.readline

# Input
N = int(input())
K = int(input())
POS = sorted(list(map(int, input().split())))

# Function
distance = [POS[i+1]-POS[i] for i in range(len(POS)-1)]
distance.sort()
res = sum(distance[:N-K])

# Output
print(res)