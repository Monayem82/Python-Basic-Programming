def sphereCal(r):
    pi=3.14159
    result = (4.0/3)*pi*r*r*r

    print("VOLUME =",format(result,'.3f'))

r=int(input())
sphereCal(r)