def  inverso(cadena):
    invert=cadena[::-1]
    return invert


def run():
    cadena = input('Dame la cadena: ')
    print(inverso(cadena))


run()