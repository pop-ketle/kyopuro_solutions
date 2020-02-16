from collections import deque
S=list(input())

n=len(S)
ans=set()
for i in range(2**n):
    deq=deque(S)
    tmp=''
    for j in range(n):
        if i>>j & 1:
            tmp+=deq.popleft()
        else:
            tmp+=deq.pop()
    ans.add(tmp)
print(len(ans))