w=int(input())
h=int(input())
n=int(input())
SK=[list(map(int,input().split())) for _ in range(n)]

SK.sort()
S,K=zip(*SK)
print(w*h - (w-len(set(S)))*(h-len(set(K))) - n)