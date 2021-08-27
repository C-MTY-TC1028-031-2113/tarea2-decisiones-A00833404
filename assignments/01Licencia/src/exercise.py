
def main():
    edad = int(input("Ingresa tu edad: "))
    if 110 >= edad >= 18:
        ine = input("¿Tienes identificación oficial? (s/n): ")
        if ine == "s":
            print("Trámite de licencia concedido")
        elif ine == "n":
            print("No cumples requisitos")
        else:
            print("Respuesta incorrecta") 
    elif 18 > edad:
        print("No cumples requisitos")
    else: 
        print("Respuesta incorrecta")     

if __name__ == '__main__':
    main()
