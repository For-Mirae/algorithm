import sys

N = int(input())

tmp_list = []
for i in range(1,N+1):
    tmp = sys.stdin.readline().rstrip()
    tmp_list.append(tmp)


for i in range(0, N):
    l = []
    stack = tmp_list[i]
    l = stack.split(' ')
    tmp = ''
    for j in range(len(l)):
        tmp += ' ' + l.pop()

    print("Case #{}:".format(i+1)+ tmp)