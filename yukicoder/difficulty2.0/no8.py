p=int(input())
NK=[list(map(int,input().split())) for _ in range(p)]

ans=[]
for n,k in NK:
    if n%(k+1)==1:
        ans.append('Lose')
    else:
        ans.append('Win')
print(*ans,sep='\n')