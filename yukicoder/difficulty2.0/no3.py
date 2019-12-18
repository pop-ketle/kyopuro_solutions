from queue import Queue
n=int(input())

memo=[float('inf')]*n
def bfs(q):
    x,cnt=q.get()
    if x<1 or x>n:
        return
    else:
        if memo[x-1]>cnt:
            memo[x-1]=cnt
            dst=str(bin(x))[2:].count('1')
            q.put([x-dst,cnt+1])
            q.put([x+dst,cnt+1])

q=Queue()
q.put([1,1])
while not q.empty():
    bfs(q)
print(-1) if memo[-1]==float('inf') else print(memo[-1])