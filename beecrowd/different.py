def different(*arg):
    add1=1
    add2=1
    result=0
    for i in range(len(arg)):
        if i<2:
            add1=add1*arg[i]
        else:
            add2=add2*arg[i]
    
    result=add1-add2;
    print("DIFERENCA =",result)

a=int(input())
b=int(input())
c=int(input())
d=int(input())

different(a,b,c,d)