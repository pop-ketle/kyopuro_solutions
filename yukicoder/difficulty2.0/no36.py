n=int(input())

def prime_factorize(n):
    ls,tmp=[],n
    c=int(n**0.5)+1
    for i in range(2,c):
        while tmp%i==0:
            tmp=tmp//i
            ls.append(i)
        if tmp==1:
            break
    return ls
prime_factor=prime_factorize(n)
if len(prime_factor)>1 and prime_factor[0]*prime_factor[1]<n:
    print('YES')
else:
    print('NO')