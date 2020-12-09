fin=open("C:/Users/Andu/Desktop/aoc/8.txt", "r")
l=fin.readlines()
fin.close()
i=0
s=0
d={}
while i not in d:
    d[i]=1
    print(l[i], end="")
    if "acc" in l[i]:
        s+=int(l[i][4:len(l[i])-1])
        i+=1
    elif "jmp" in l[i]:
        if "-" in l[i]:
            i=i+int(l[i][4:len(l[i])-1])
        else:
            i=i+int(l[i][4:len(l[i])-1])
    else:
        i+=1
print(s)
while i!=len(l):
    d[i]=1
    if "acc" in l[i]:
        s+=int(l[i][4:len(l[i])-1])
        i+=1
    elif "jmp" in l[i]:
        if "-" in l[i]:
            i+=1
        else:
            if '\n' in l[i]:
                i=i+int(l[i][4:len(l[i])-1])
            else:
                i=i+int(l[i][4:len(l[i])])
    else:
        i+=1
print(s)
    