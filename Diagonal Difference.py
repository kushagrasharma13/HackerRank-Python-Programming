n=int(input())
d={}
sum1=0
sum2=0
for i in range(n):
    d[i]=list(map(int,input().split()))
    sum1=sum1+d[i][i]
    sum2=sum2+d[i][n-i-1]
print(abs(sum1-sum2))
