def logitud(palabra):
    longitud = len(palabra)
    return longitud

def mayus(palabra):
    may = palabra.upper()
    return may

def minuscula(palabra):
    min = palabra.lower()
    return min

def indice(letra):
    indi = palabra.find(letra)
    return indi

#Slice
def subcadena(palabra , a, b):
    sub = palabra[a:b]
    return sub

def  palindromo(cadena):
    palin = cadena[::-1]
    if(palin == cadena):
         return print('Es palindromo')
    else:
        return print('No es palindromo')


palabra = str(input('Dame la palabra:'))
letra = str(input('Dame la letra:'))
a = int(input('Dame indice menor:'))
b = int(input('Dame indice mayor:'))
cadena = str(input('Candena para combrobar si es un palindormo: '))

palin = palindromo(cadena)
sCadena = subcadena(palabra,a,b)




print('Su longitud es : {} '.format(logitud(palabra)))
print('En mayusculas es : {}'.format(mayus(palabra)))
print('En minusculas es: {}'.format(minuscula(palabra)))
print('El indice de la letra {} es : {}'.format(letra, indice(letra)))
print('La subcadena es: {}'.format(sCadena))
