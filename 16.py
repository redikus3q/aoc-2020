fin=open("C:/Users/Andu/Desktop/aoc/16.txt", "r")
import copy
def part1():
    x=[]
    l=fin.readline()
    while l!='\n':
        l=l.split()
        lc=l[-1].index("-")
        a=int(l[-1][:lc])
        b=int(l[-1][lc+1:])
        for i in range(a,b+1):
            x.append(i)
        lc=l[-3].index("-")
        a=int(l[-3][:lc])
        b=int(l[-3][lc+1:])
        for i in range(a,b+1):
            x.append(i)
        l=fin.readline()
    x=set(x)
    while "nearby" not in l:
        l=fin.readline()
    l=fin.readline()
    s=0
    while l:
        l=l.split(',')
        li=[int(a) for a in l if '\n' not in a]
        if '\n' in l[len(l)-1]:
            li.append(int(l[len(l)-1][:len(l[len(l)-1])-1]))
        for n in li:
            if n not in x:
                s+=n
        l=fin.readline()
    return s

def part2():
    x=[]
    x6=[[]]
    l=fin.readline()
    k=1
    while l!='\n':
        x6.append([])
        l=l.split()
        lc=l[-1].index("-")
        a=int(l[-1][:lc])
        b=int(l[-1][lc+1:])
        for i in range(a,b+1):
            x.append(i)
            x6[k].append(i)
        lc=l[-3].index("-")
        a=int(l[-3][:lc])
        b=int(l[-3][lc+1:])
        for i in range(a,b+1):
            x.append(i)
            x6[k].append(i)
        l=fin.readline()
        k+=1
    x=set(x)
    l=fin.readline()
    l=fin.readline()
    l=l.split(',')
    ticket=[int(a) for a in l if '\n' not in a]
    if '\n' in l[len(l)-1]:
        ticket.append(int(l[len(l)-1][:len(l[len(l)-1])-1]))
    l=fin.readline()
    l=fin.readline()
    l=fin.readline()
    xs=[(j for j in range(len(ticket))) for x in range(len(ticket))]
    while l:
        l=l.split(',')
        li=[int(a) for a in l if '\n' not in a]
        if '\n' in l[len(l)-1]:
            li.append(int(l[len(l)-1][:len(l[len(l)-1])-1]))
        for n in li:
            if n not in x:
                break
        else:
            pos=[[] for a in range(len(li))]
            for j in range(len(li)):
                for p in range(1,21):
                    if li[j] in x6[p]:
                        pos[j].append(p)
            for i in range(len(pos)):
                xs[i]=set(xs[i])&set(pos[i])
        l=fin.readline()
    count=1
    answ=[]
    s=1
    while count<=20:
        cxs=copy.deepcopy(xs)
        for a in cxs:
            if len(a)==1:
                for b in a:
                    break
                if b>=1 and b<=6:
                    answ.append(cxs.index(a))
            for i in range(len(xs)):
                if b in xs[i]:
                    xs[i].remove(b)
        count+=1
    for i in answ:
        s*=ticket[i]
    return s

print(part2())