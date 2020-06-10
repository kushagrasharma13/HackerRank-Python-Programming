l=[]
N=int(input())
for i in range(N):
    n=list(input().split())
    if n[0]=="insert":
        l.insert(int(n[1]),int(n[2]))
    elif n[0]=='print':
        print(l)
    elif n[0]=='remove':
        l.remove(int(n[1]))
    elif n[0]=='append':
        l.append(int(n[1]))
    elif n[0]=='sort':
        l.sort()
    elif n[0]=='pop':
        l.pop()
    elif n[0]=='reverse':
        l.reverse()
