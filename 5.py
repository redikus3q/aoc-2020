fin=open("C:/Users/Andu/Desktop/aoc/5.txt", "r")
x=fin.readline()
Max=0
d={}
while x:
    x=x.replace('F', '0')
    x=x.replace('B', '1')
    x=x.replace('R', '1')
    x=x.replace('L', '0')
    row=int(x[0:7], 2)
    clm=int(x[7:10], 2)
    id=row*8+clm
    d[id]=1
    if(id>Max):
        Max=id
    x=fin.readline()
i=2
#part2
while i:
    if i not in d.keys():
        if i+1 in d.keys() and i-1 in d.keys():
            print(i)
            break
    i+=1