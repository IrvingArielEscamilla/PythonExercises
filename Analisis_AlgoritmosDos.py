def far2Cent(grades):
    gradesCen = (grades-32) / 1.8
    return gradesCen
def run():
    grades = float(input('Dame los grados a convertir en Centrigrados: '))
    print('{} grados Fahrenheit son: {} grados Centigrados'.format(grades,far2Cent(grades)))

run()