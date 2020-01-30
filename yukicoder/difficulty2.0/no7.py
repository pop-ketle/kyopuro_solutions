n=int(input())

def eratosthenes(limit):
    import math
    A=[i for i in range(2,limit+1)]
    P=[]
    while True:
        prime=min(A)
        if prime>math.sqrt(limit):
            break
        P.append(prime)
        
        i=0
        while i<len(A):
            if A[i]%prime==0:
                A.pop(i)
                continue
            i+=1
            
    for a in A:
        P.append(a)
        
    return P
    
P=eratosthenes(n)
dp=[False]*(n+1)
dp[0]=dp[1]=1
for i in range(2,n+1):
    for p in P:
        if i-p>=0 and not dp[i-p]:
            dp[i]=True
            break
        else:
            dp[i]=False
print('Win') if dp[n] else print('Lose')