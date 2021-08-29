def main():
    # Escribe tu código abajo de esta línea
    gra = int(input("Introduce los grados: "))
    if 360 >= gra >= 0:
        if 90 > gra > 0:
            print("cuadrante 1")
        elif gra == 0 or gra == 90 or gra == 180 or gra == 270 or gra == 360:
            print("eje")
        elif 180 > gra > 90:
            print("cuadrante 2")
        elif 270 > gra > 180:
            print("cuadrante 3")
        else:
            print("cuadrante 4")
    else: 
        print("excede")
if __name__ == '__main__':
    main()
