def esPar(numero):
    return (numero % 2 == 0)

def run ():

    numero = int(input('Dame numero :'))
    print(esPar(numero))

run()