# bit全探索だと制約通らない
n=int(input())
W=list(map(int,input().split()))

if sum(W)%2!=0:
    print('impossible')
    exit()
dp=[[False]*(10001) for _ in range(101)]
dp[0][0],dp[0][W[0]]=True,True
for i in range(n):
    for j in range(10000):
        if dp[i][j]==True:
            dp[i+1][j+W[i]]=True
            dp[i+1][j]=True
if dp[n][int(sum(W)/2)]==True:
    print('possible')
    exit()
print('impossible')