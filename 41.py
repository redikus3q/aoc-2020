fin=open("C:/Users/Andu/Desktop/aoc/4.txt", "r")
x=fin.readline()
s=0
sfin=0
cid=0
while x:
    if x=='\n':
        if s==8:
            sfin+=1
        elif s==7 and cid==0:
            sfin+=1
        s=0
        cid=0
    else:
        s+=x.count(":")
        if "cid" in x:
            cid=1
    x=fin.readline()
print(sfin)
