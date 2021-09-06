import sys
import math
testcase = int(sys.stdin.readline())

for _ in range(testcase):
    x, y = map(int, sys.stdin.readline().split())

    distance = y - x
    if math.sqrt(distance).is_integer():
        jump = int(math.sqrt(distance) * 2 - 1)
    else:
        jump = math.floor(math.sqrt(distance) * 2)

    print(jump)