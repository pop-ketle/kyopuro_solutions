# ソートする形だとn=20000の時にTLEが出る
n=int(input())
AB=[list(map(str,input().split())) for _ in range(n)]

cheater,person=[],[]
for a,b in AB:
    cheater.append(a)
    person.append(b)
nocheater=set(person)-set(cheater)
# nocheater=sorted(set(nocheater),key=person.index)
# print(*nocheater,sep="\n")

for p in person:
    if p in nocheater:
        print(p)
        nocheater.remove(p)