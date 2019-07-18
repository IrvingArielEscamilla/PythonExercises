def raicesReales(a,b,c):
    discriminante = b**2 -( 4*a*c)
    if (discriminante>=0):
        return True
    else:
        return False

def run():
    print('----Formula General----')
    print('Forma general ----ax^2 + bx + c----')
    a = float(input('Dame a:'))
    b = float(input('Dame b:'))
    c = float(input('Dame c:'))

    if(raicesReales(a,b,c)==True):
        print('Las raices son reales ')
    else:
        print('No tiene raices reales')

run()