import sys
import math
testcase = int(sys.stdin.readline())

for _ in range(testcase):
    H, W, N = map(int, sys.stdin.readline().split())
    floor = str((N-1) % H + 1)
    room = str(math.ceil(N/H))
    room = room.zfill(2)
    print('{0}{1}'.format(floor,room))