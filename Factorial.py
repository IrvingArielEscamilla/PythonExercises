
def factorial(number):
    if(number==0):
        fact =1;
        return fact
    else:
        fact = number*factorial(number-1)
        return fact

def run():
    number = int(input('Dame numero: '))
    numfact = factorial(number)
    print('El factorial de: {} es: {}'.format(number,numfact))

run()