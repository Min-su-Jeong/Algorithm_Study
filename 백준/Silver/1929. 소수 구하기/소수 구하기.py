import sys
input = sys.stdin.readline

# Input
M, N = map(int, input().split())

# Variables
MAX = 1000000
prime = [True for _ in range(MAX+1)]
prime[0] = prime[1] = False

# Solution
def calc_prime():
    for i in range(2, int(MAX**0.5)+1):
        if prime[i]:
            for j in range(i*i, MAX, i):
                prime[j] = False

def solution():
    calc_prime()
    for i in range(M, N+1):
        if prime[i]:
            print(i)

# Main
solution()