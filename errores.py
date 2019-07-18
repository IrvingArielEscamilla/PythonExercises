countries = {
    'mexico':122,
    'colombia': 49,
    'argentina' : 42,
    'chile' : 18,
    'peru' : 31
}

while True:
    country = str(input('Escribe el nombre del pais: ')).lower()
    try:
         print('La poblacion de : {} es: {} millones'.format(country,countries[country]))

    except KeyError:
        print('No tenemos el dato de este pais : {}'.format(country))
