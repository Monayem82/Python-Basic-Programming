def salary(emp,sal,sold):
    result=sal+sold*0.15;
    print("TOTAL = R$",format(result,'.2f'))


emp=str(input())
sal=float(input())
sold=float(input())

salary(emp,sal,sold)