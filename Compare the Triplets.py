a=list(map(int,input().split()))
b=list(map(int,input().split()))
a_point=0
b_point=0
for _ in range(3):
    if a[_]>b[_]:
        a_point+=1
    elif a[_]<b[_]:
        b_point+=1
    else:
        pass
print(a_point,b_point)
