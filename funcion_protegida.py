
def run():
    password = str(input('Ingresa tu password: '))
    protected_func(password)

def protected(func):
    def wrapper(password):
        if password == 'platzi':
            return func()
        else:
            print('El password es invalido')
    return wrapper
@protected
def protected_func():
    print('Tu password es correcta.')

run()