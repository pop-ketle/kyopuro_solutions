x,n=map(int,input().split())
A=list(map(int,input().split()))

mod=1000003
ans=0
for i in range(n):
    ans+=pow(x,A[i],mod)
    ans=ans%mod
print(ans)