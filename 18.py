fin=open("C:/Users/Andu/Desktop/aoc/18.txt", "r")

def part1():
    s=0
    l=[x for x in fin.readline() if x!=' ' and x!='\n']
    while l:
        par=l.count(')')
        j=0
        while j!=par:
            b=l.index(')')
            a=l[b::-1].index('(')
            a=len(l[:b])-a
            nr=0
            op=0
            for x in l[a+1:b]:
                if x=='+':
                    op=1
                elif x=='*':
                    op=2
                elif op==0:
                    nr=int(x)
                elif op==1:
                    nr=nr+int(x)
                elif op==2:
                    nr=nr*int(x)
            l[a]=nr
            while l[a+1]!=')':
                l.pop(a+1)
            l.pop(a+1)
            j+=1
        nr=0
        op=0
        for x in l:
            if x=='+':
                op=1
            elif x=='*':
                op=2
            elif op==0:
                nr=int(x)
            elif op==1:
                nr=nr+int(x)
            elif op==2:
                nr=nr*int(x)
        s+=nr
        l=[x for x in fin.readline() if x!=' ' and x!='\n']
    return s

def part2():
    s=0
    l=[x for x in fin.readline() if x!=' ' and x!='\n']
    while l:
        par=l.count(')')
        j=0
        while j!=par:
            b=l.index(')')
            a=l[b::-1].index('(')
            a=len(l[:b])-a
            newl=[]
            ok=1
            for x in range(a+1,b):
                if ok==1:
                    newl.append(l[x])
                else:
                    ok=1
                if l[x]=='+':
                    ok=0
                    newl.pop()
                    nor=newl[-1]
                    newl.pop()
                    newl.append(int(nor)+int(l[x+1]))
            nr=0
            op=0
            for x in newl:
                if x=='+':
                    op=1
                elif x=='*':
                    op=2
                elif op==0:
                    nr=int(x)
                elif op==1:
                    nr=nr+int(x)
                elif op==2:
                    nr=nr*int(x)
            l[a]=nr
            while l[a+1]!=')':
                l.pop(a+1)
            l.pop(a+1)
            j+=1
        newl=[]
        ok=1
        for x in range(len(l)):
            if ok==1:
                newl.append(l[x])
            else:
                ok=1
            if l[x]=='+':
                ok=0
                newl.pop()
                nor=newl[-1]
                newl.pop()
                newl.append(int(nor)+int(l[x+1]))
        nr=0
        op=0
        for x in newl:
            if x=='+':
                op=1
            elif x=='*':
                op=2
            elif op==0:
                nr=int(x)
            elif op==1:
                nr=nr+int(x)
            elif op==2:
                nr=nr*int(x)
        s+=nr
        l=[x for x in fin.readline() if x!=' ' and x!='\n']
    return s
print(part2())
fin.close()