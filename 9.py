fin=open("C:/Users/Andu/Desktop/aoc/9.txt", "r")
finput=fin.readlines()
l=[int(a[:len(a)-1]) for a in finput]
l[len(l)-1]=int(finput[len(finput)-1])
fin.close()

def solve1():
    s=[]
    for i in range(25):
        s.append([l[i]+l[j] for j in range(25) if j!=i])
    for i in range(25, len(l)):
        s.append([l[i]+l[i-j] for j in range(25) if i-j!=i])
        if l[i] not in (j for k in s for j in k):
            return l[i]
        s.pop(0)

def solve2():
    a=solve1()
    left=0
    r=0
    s=l[r]
    while s!=a:
        if s<a:
            r+=1
            s=s+l[r]
        elif s>a:
            s=s-l[left]
            left+=1
    return max(l[left:r+1])+min(l[left:r+1])
print(solve2())