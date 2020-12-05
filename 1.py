fin=open("C:/Users/Andu/Desktop/aoc/2.txt", "r")
x=fin.readlines()
s=0
for a in x:
    i=0
    x=''
    y=''
    z=''
    while a[i]!='-':
        x+=a[i]
        i+=1
    i+=1
    while a[i]!=' ':
        y+=a[i]
        i+=1
    i+=1
    z=a[i]
    i+=3
    if '\n' in a:
        a=a[i:len(a)-1]
    else:
        a=a[i:]
    x=int(x)
    y=int(y)
    x-=1
    y-=1
    if(a[x]!=a[y]):
        if a[x]==z or a[y]==z:
            s+=1
print(s)