A=[int(input()) for _ in range(5)]

memo=[1,1]
while memo[-1]<=10**15:
    memo.append(memo[-1]+memo[-2])

A,ans=A[::-1],0
for i in range(1,6):
    if A[0] in memo:
        tmp=A[:i]
        idx=memo.index(tmp[0])
        if tmp[0]==1:
            if tmp==memo[idx+1:idx+1+i]: ans=max(ans,i)
        if tmp==memo[idx:idx+i]: ans=max(ans,i)
print(ans)