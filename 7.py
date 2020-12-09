fin=open("C:/Users/Andu/Desktop/aoc/7.txt", "r")
finx=fin.readlines()
fin.close()
s=0
bag=[' shiny gold bag',]
i=1
v=0
while v<len(bag):
    for x in finx:
        if bag[v] in x:
            s+=1
            for b in bag[v+1:]:
                if b in x:
                    s-=1
            x=x.split()
            a=" "
            a+=x[0]
            a+=" "
            a+=x[1]
            a+=" "
            a+=x[2][:len(x[2])-1]
            if a not in bag:
                bag.append(a)
                i+=1
            else:
                s-=1
    v+=1
print(s)
    