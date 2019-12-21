a,b=map(int,input().split())

yaku,bi=[],[]
for i in range(1,a+1):
    if a%i==0:
        yaku.append(i)
i=1
while True:
    if b*i>100:
        break
    bi.append(b*i)
    i+=1
for y in yaku:
    if y in bi:
        print('Yes')
        exit()
print('No')