# 값을 받으며 들어오는 수가 클 경우 카운트
import sys

N = int(sys.stdin.readline())
cnt = 1
stack = []
for i in range(N):
    stack.append(int(sys.stdin.readline().rstrip()))

num = stack.pop()
for i in reversed(range(len(stack))):
    if stack[i] > num:
        cnt += 1
        num = stack[i]

print(cnt)
