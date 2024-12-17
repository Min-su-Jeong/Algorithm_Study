import sys
input = sys.stdin.readline

# Input
arr = [input().rstrip() for _ in range(3)]

# Solution
def sequence():
    for i in range(3):
        if arr[i].isdigit():
            return int(arr[i]) + (3-i)

# Main        
res = sequence()

# Output
if res % 15 == 0:
    print('FizzBuzz')
elif res % 3 == 0:
    print('Fizz')
elif res % 5 == 0:
    print('Buzz')
else:
    print(res)