def area():
    a=(input())
    b=float(input())
    c=float(input())
    
    tri=0.5*(a*c)
    cir=3.14159*c*c
    tra=0.5*(a+b)*c
    qua=b*b
    ret=a*b
    
    print("TRIANGULO:",format(tri,'.3f'))
    print("CIRCULO:",format(cir,'.3f'))
    print("TRAPEZIO:",format(tra,'.3f'))
    print("QUADRADO:",format(qua,'.3f'))
    print("RETANGULO:",format(ret,'.3f'))
    
area()