def run():
    print('C A L C U L A D O R A  D E  D I V I S A S ')
    print('---Convierte de pesos mexicanos a pesos colombianos')
    print('')

    ammount = float(input('Ingresa la cantidad(mxn):'))
    result = foreign_exchange_calculator(ammount)
    print('${} pesos mexicanos son ${} pesos colombianos'.format(ammount,result))

def foreign_exchange_calculator(ammount):
    mex_to_col = 145.97
    return mex_to_col * ammount

run()