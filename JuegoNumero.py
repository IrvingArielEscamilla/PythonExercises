import random

def run():
    number_found = False
    random_number = random.randint(0,20)

    while not number_found:
        number = int(input('Intenta un numero:'))

        if(number == random_number):
            print('Felicidades has encontrado el numero')

        elif number>random_number:
            print('El numero es mas pequenio')
        else:
            print('El numero es mas grande')

run()
