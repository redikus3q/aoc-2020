fin=open("C:/Users/Andu/Desktop/aoc/14.txt", "r")

def part1():
    ind=[]
    mem={}
    for l in fin.readlines():
        if l[1]=='a':
            le=35
            ind=[]
            for a in l[7:]:
                if a=='1' or a=='0':
                    ind.append((int(a),le))
                le-=1
        else:
            nr=int(l[4:l.find(']')])
            num=int(l[l.find('=')+2:])
            for a in ind:
                if (num>>a[1])&1!=a[0]:
                    if (num>>a[1])&1==1 and a[0]==0:
                        num=num-2**a[1]
                    elif (num>>a[1])&1==0 and a[0]==1:
                        num=num+2**a[1]
            mem[nr]=num
    return sum(mem.values())

rez=[]
def back(n,k,x):
    for a in range(2):
        x[k]=a
        if k==n-1:
            rez.append(x[:])
        else:
            back(n,k+1,x)

def part2():
    mem={}
    for l in fin.readlines():
        if l[1]=='a':
            ind=[a for a in l[7:len(l)-1]]
        else:
            num=int(l[l.find('=')+2:])
            nr=[a for a in str(bin(int(l[4:l.find(']')])))[2:]]
            nrf=ind
            k=0
            for a in range(len(nrf)):
                if a>35-len(nr):
                    if nrf[a]=='0':
                        nrf[a]=nr[k]
                    k+=1
            n=nrf.count('X')
            x=[0]*n
            back(n,0,x)
            k=0
            nrfc=nrf[:]
            for i in rez:
                k=0
                nrf=nrfc[:]
                for a in range(len(nrf)):
                    if(nrf[a]=='X'):
                        nrf[a]=str(i[k])
                        k+=1
                mem[int("".join(nrf),2)]=num
            rez.clear()
    return sum(mem.values())

print(part2())
fin.close()