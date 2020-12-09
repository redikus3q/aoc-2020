fin=open("C:/Users/Andu/Desktop/aoc/3.txt", "r")
x=fin.readline()
i1=0
i2=0
i3=0
i4=0
i5=0
s1=0
s2=0
s3=0
s4=0
s5=0
k=0
smax=1
while x:
    if i1>=len(x)-1:
        i1=i1-len(x)+1
    if i2>=len(x)-1:
        i2=i2-len(x)+1
    if i3>=len(x)-1:
        i3=i3-len(x)+1
    if i4>=len(x)-1:
        i4=i4-len(x)+1
    if i5>=len(x)-1:
        i5=i5-len(x)+1
    if(x[i1]=='#'):
        s1+=1
    if(x[i2]=='#'):
        s2+=1
    if(x[i3]=='#'):
        s3+=1
    if(x[i4]=='#'):
        s4+=1
    if(k%2==0):
        if(x[i5]=='#'):
            s5+=1
        i5+=1
    k+=1
    i1=i1+1
    i2+=3
    i3+=5
    i4+=7
    x=fin.readline()
smax=s1*s2*s3*s4*s5
fin.close()
print(smax)