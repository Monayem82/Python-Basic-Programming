
def posiTive(number):
    print(number)
    count=0
    for i in number:
        if i>0:
            count+=1
        
    print(count)

lis=[]
for i in range(0,6):
    lis.append(int(input()))

posiTive(lis)