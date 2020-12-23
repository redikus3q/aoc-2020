fin=open("C:/Users/Andu/Desktop/aoc/15.txt", "r")
l=fin.readline().split(",")
def part():
    d={}
    k=1
    for i in l:
        i=int(i)
        d[i]=k
        k+=1
        actual=i
    k-=1
    d.pop(actual)
    while k!=30000000:  #for part1 replace 30000000 with 2020
        if actual not in d:
            d[actual]=k
            actual=0
        else:
            a=k-d[actual]
            d[actual]=k
            actual=a
        k+=1
    return actual

print(part())
fin.close()