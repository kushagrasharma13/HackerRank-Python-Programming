from itertools import product
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(product(A,B))
F=str(C[0])
i=1
while i<len(C):
    F=F+" "+str(C[i])
    i+=1
print(F)
