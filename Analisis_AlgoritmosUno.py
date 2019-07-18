def es_par(numero):
    return (numero%2==0)

def run():
    max = int(input('Dame el numero tope: '))

    for c in range(0,max-1):
        if(es_par(c)==True):
            print('{} es par'.format(c))

run()