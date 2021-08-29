import math

def main():
    # Escribe tu código abajo de esta línea
    a=int(input("Da el valor de a: "))
    b=int(input("Da el valor de b: "))
    c=int(input("Da el valor de c: "))
    if a == 0 and b == 0:
        print("No tiene solucion")
    elif a == 0 and b != 0:
        x = (-c/b)
        print(x)
    elif a != 0 and b != 0:
        dis = (b**2-4*a*c)
        if 0 > dis:
            print("Raices complejas")
        elif dis == 0:
            x = -b/(2*a)
            print(x)
        else:
            print(((-b) + dis)/ (2*a))
            print(((-b) - dis)/ (2*a))
    else: 
        x = 0


if __name__ == '__main__':
    main()
