n=int(input())
f=int(input())
i=0
n=n-(n%100)
while(True):
    if((n+i)%f==0):break
    i+=1
if(len(str(i))==1):i="0"+str(i)
print(i)