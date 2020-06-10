N=int(input())
d={}
for i in range(N):
    l=list((input().split(' ')))
    name=l[0]
    l.remove(l[0])
    for _ in range(len(l)):
        l[_]=float(l[_])
        #Average of marks
    d[name]=sum(l)/len(l)
checkname=input()
print('%.2f'%d[checkname])
        
