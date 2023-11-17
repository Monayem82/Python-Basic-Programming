
def simpleCalculation():
    res=0;
    for x in range(0,2):
        p =int(input())
        u =int(input())
        price =float(input())
        res=res+u*price

    print("VALOR A PAGAR: R$",format(res,'.2f'))

simpleCalculation()






