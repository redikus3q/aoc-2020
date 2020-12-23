fin=open("C:/Users/Andu/Desktop/aoc/22.txt", "r")
d=[[],[]]
def part1():
    di=0
    for l in fin.read().splitlines():
        if "Player" not in l and l!='':
            d[di].append(int(l))
        elif "Player 2" in l:
            di=1
    while len(d[0])!=0 and len(d[1])!=0:
        if d[0][0]>d[1][0]:
            d[0].append(d[0][0])
            d[0].append(d[1][0])
        else:
            d[1].append(d[1][0])
            d[1].append(d[0][0])
        d[0].pop(0)
        d[1].pop(0)
    if len(d[0])==0:
        di=1
    else:
        di=0
    s=0
    for i in range(1, len(d[di])+1):
        s=s+d[di][-i]*i
    return s

def part2():
    def read():
        di=0
        global d
        for l in fin.read().splitlines():
            if "Player" not in l and l!='':
                d[di].append(int(l))
            elif "Player 2" in l:
                di=1
        return d
    a=read()
    d=a
    
    def recurs(d1, d2):
        l=[]
        while len(d1)!=0 and len(d2)!=0:
            a=d1[0]
            b=d2[0]
            if (d1, d2) in l:
                return 1, d1
            l.append((d1,d2))
            d1.pop(0)
            d2.pop(0)
            if a<=len(d1) and b<=len(d2):
                if 1==recurs(d1[:a],d2[:b])[0]:
                    d1.append(a)
                    d1.append(b)
                else:
                    d2.append(b)
                    d2.append(a)
            else:
                if a>b:
                    d1.append(a)
                    d1.append(b)
                else:
                    d2.append(b)
                    d2.append(a) 
        if len(d1)==0:
            return 2, d2
        else:
            return 1, d1
    s=0
    a=recurs(d[0],d[1])[1]
    for i in range(1, len(a)+1):
        s=s+a[-i]*i
    return s
print(part2())
fin.close()