q=int(input())
N=[int(input()) for _ in range(q)]

T=[-1]*10**6
T[0],T[1],T[2],T[3]=0,0,0,1
for i in range(5,10**6):
    T[i-1]=(sum(T[i-5:i-1])%17)

for n in N:
    print(T[n-1])