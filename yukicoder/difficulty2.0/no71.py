n=int(input())

ans=0
for i in range(n):
    ans=max(ans,i+(n-i)*(i+1))
print(ans)