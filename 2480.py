a=list(map(int,input().split()))
a.sort()
if a[0]==a[1]==a[2]:print(10000+1000*a[2])
elif a[0]!=a[1]!=a[2]:print(a[2]*100)
else:print(1000+a[1]*100)