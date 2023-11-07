def salary(emp,mt,hours):
    result=mt*hours;
    print("NUMBER =",emp)
    print("SALARY = U$",format(result,'.2f'))


emp=int(input())
mt=int(input())
hours=float(input())

salary(emp,mt,hours)