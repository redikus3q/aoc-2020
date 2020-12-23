fin=open("C:/Users/Andu/Desktop/aoc/13.txt", "r")
x=int(fin.readline())
la=fin.readline().split(',')
l=[int(a) for a in la if a!='x']
def part1():
    m=x+l[0]+1
    for a in l:
        if x%a==0:
            print(a)
            break
        else:
            c=x//a+1
            c=c*a
            if c<m:
                m=c
                mid=a
    return (m-x)*mid

def part2():
    i=0
    li=[]
    for a in la:
        if a=='x':
            i+=1
        else:
            li.append(i)
            i+=1
    print(li)
    i=0
    z=l[0]
    ok=1
    while ok:
        for a in range(len(li)):
            ok=0
            if (z+li[a])%l[a]!=0:
                ok=1
                break
        
        z+=l[0]
    return z-l[0]

print(part2())
fin.close()
