import sys
input = sys.stdin.readline

# Input
N = int(input())
M = int(input())
if M:
    broken = set(input().split())
else:
    broken = set()

if N == 100:
    print(0)
    sys.exit(0)
    
# Variables
res = abs(100-N)
MAX = 1000000

# Solution
def solution():
    global res

    for i in range(MAX):
        for j in str(i):
            if j in broken:
                break
        else:
            res = min(res, len(str(i)) + abs(i-N))

# Main
solution()

# Output
print(res)