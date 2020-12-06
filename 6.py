fin=open("C:/Users/Andu/Desktop/aoc/6.txt", "r")
x=fin.readline()
#first
# s=[]
# sm=0
# while x:
#     if x=='\n':
#         a=set(s)
#         sm=len(a)+sm
#         s.clear()
#     else:
#         for i in x:
#             if(i!='\n'):
#                 s+=i
#     x=fin.readline()
# a=set(s)
# sm=len(a)+sm
# print(sm)
d={}
sm=0
ppl=0
while x:
    if x=='\n':
        for i in d.keys():
            if d[i]==ppl:
                sm+=1
        d.clear()
        ppl=0
    else:
        ppl+=1
        for i in x:
            if(i!='\n'):
                if i in d.keys():
                    d[i]+=1
                else:
                    d[i]=1
    x=fin.readline()
for i in d.keys():
    if d[i]==ppl:
        sm+=1
print(sm)