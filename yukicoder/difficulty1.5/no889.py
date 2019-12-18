n=int(input())

sosu=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]
root=[4,9,16,25,36,49,64]
cubi=[8,27,64]
perf=[6,28]
if n in sosu:
    print('Sosu!')
elif n in root:
    print('Heihosu!')
elif n in cubi:
    print('Ripposu!')
elif n in perf:
    print('Kanzensu!')
else:
    print(n)