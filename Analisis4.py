
def run():
    Maximo = 0
    Minimo = 100
    CantNumeros = 10
    for i in range(1, CantNumeros + 1):
        print("Ingrese el ", i, "numero")
        Numero = int(input())
        if (Numero > Maximo):
            Maximo = Numero
        elif (Numero < Minimo):
            Minimo = Numero
    print("El valor maximo es el numero", Maximo)

run()