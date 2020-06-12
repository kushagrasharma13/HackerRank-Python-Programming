S=input()
f=0
for i in S:
    if i.isalnum():
        f=1
        break
if f==1:
    print('True')
else:
    print('False')
f=0
for i in S:
    if i.isalpha():
        f=1
        break
if f==1:
    print('True')
else:
    print('False')
f=0
for i in S:
    if i.isdigit():
        f=1
        break
if f==1:
    print('True')
else:
    print('False')
f=0
for i in S:
    if i.islower():
        f=1
        break
if f==1:
    print('True')
else:
    print('False')
f=0
for i in S:
    if i.isupper():
        f=1
        break
if f==1:
    print('True')
else:
    print('False')
