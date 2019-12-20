n=int(input())
V=list(map(int,input().split()))

dp=[0]*n
for i in range(n):
    dp[i] = V[i] if i==0 else max(dp[i-2]+V[i],dp[i-1])
print(dp)