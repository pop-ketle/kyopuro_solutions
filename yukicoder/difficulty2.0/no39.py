import itertools
N=list(input())

all_pattern=list(itertools.permutations(N))
ans=0
for pattern in all_pattern:
    cnt,tmp=0,''
    for i in range(len(N)):
        if pattern[i]!=N[i]: cnt+=1
        if cnt>2:
            break
        tmp+=pattern[i]
    if cnt<=2:
        ans=max(ans,int(tmp))
print(ans)