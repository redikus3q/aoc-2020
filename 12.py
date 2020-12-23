fin=open("C:/Users/Andu/Desktop/aoc/12.txt", "r")
def part1():
    n=0
    e=0
    f=0
    for x in fin.readlines():
        a=int(x[1:])
        if(x[0]=='N'):
            n=n+a
        elif(x[0]=='S'):
            n=n-a
        elif(x[0]=='E'):
            e=e+a
        elif(x[0]=='W'):
            e=e-a
        elif(x[0]=='R'):
            a=a%360
            f=f+a
            f=f%360
        elif(x[0]=='L'):
            a=a%360
            f=f-a
            f=f%360
        elif(x[0]=='F'):
            if(f==0):
                e=e+a
            elif(f==90):
                n=n-a
            elif(f==180):
                e=e-a
            elif(f==270):
                n=n+a
    return (abs(n)+abs(e))
def part2():
    nw=1
    ew=10
    n=0
    e=0
    for x in fin.readlines():
        a=int(x[1:])
        if(x[0]=='N'):
            nw=nw+a
        elif(x[0]=='S'):
            nw=nw-a
        elif(x[0]=='E'):
            ew=ew+a
        elif(x[0]=='W'):
            ew=ew-a
        elif(x[0]=='R'):
            a=a%360
            if a==90:
                ew,nw=nw,-ew
            elif a==180:
                ew,nw=-ew,-nw
            elif a==270:
                ew,nw=-nw,ew
        elif(x[0]=='L'):
            a=a%360
            if a==90:
                ew,nw=-nw,ew
            elif a==180:
                ew,nw=-ew,-nw
            elif a==270:
                ew,nw=nw,-ew
        elif(x[0]=='F'):
            e=e+ew*a
            n=n+nw*a
    return (abs(n)+abs(e))

print(part2())
fin.close()
