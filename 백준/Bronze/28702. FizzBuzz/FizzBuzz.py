import sys
input = sys.stdin.readline

# Input
s = [input().rstrip() for _ in range(3)]

# Solution
def sequence(s):
    for i in range(3):
        if s[i].isdigit():
            return int(s[i]) + (3-i)
        
# Main
res = sequence(s)

if res % 3 == 0 and res % 5 == 0:
    print('FizzBuzz')
elif res % 3 == 0:
    print("Fizz")
elif res % 5 == 0:
    print("Buzz")
else:
    print(res)