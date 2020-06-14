n,m=map(int,input().split())
for i in range(n//2):
    x='.|.'*((i*2)+1)
    print(x.center(m,'-'))
print('WELCOME'.center(m,'-'))
for i in range((n//2)-1,-1,-1):
    x='.|.'*((i*2)+1)
    print(x.center(m,'-'))
