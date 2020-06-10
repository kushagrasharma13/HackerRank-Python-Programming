a=int(input())
d={}
n=[]
for i in range(a):
    name=input()
    score=float(input())
    d[name]=score
    n.append(score)
c=0
n.sort()
for i in range(len(n)):
    if n[i]<n[i+1]:
        c=n[i+1]
        break
f=[]
for name,score in d.items():
    if score==c:
        f.append(name)
for i in sorted(f):
    print(i)
