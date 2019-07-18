import random as rd
#Irving Ariel Escamilla Jacobo 417078784
#www.algoritmiamexico.com
#irvingariel.escamilla@comunidad.unam.mx
#Programa que genera numero aleatorios, ordena (QuickSort) y busca (Binary_search) para agregar otro elemento.


def run(): #Funcion principal
    numberList = generateNumbers() #Asigna la variable para la funcion que genera aleatorios

    while True: #Menu de opciones
        command =str(input('''
        
        [a]agregar numero
        [e]liminar numero
        [b]uscar numero
        [s]alir
        
        '''))

        if command.lower() == 'a': #Agregar numero , valida, busca y ejecuta
            print('------------>Agregar numero:<-------------')
            try: #Manejo de error de tipo de dato
                number = int(input('Dame el numero para agregar: '))
                if validation(number) is True:

                    search = binary_search(numberList,number,0,len(numberList)-1)

                    if search is True : #validacion de busqueda
                        print('El numero: {} SI esta en la lista y no sera agregado \n'.format(number))

                    else:
                        print('El numero: {} NO esta en la lista y se agregara \n'.format(number))
                        numberList.append(number) #agrega numero
                        print(sorted(numberList)) #lista ordenada
                        numberList = sorted(numberList) #reasigancion de lista de elemtons

            except ValueError: #manejo de error
                print('Tipo de dato invalido')

        elif command.lower() == 'e': #Eliminar un numero , valida, busca y ejecuta
            print('------------->Eliminar numero:<-----------')
            try:
                number = int(input('Dame el numero a eliminar: \n'))

                if validation(number) is True:
                    search = binary_search(numberList, number, 0, len(numberList) - 1)

                    if search is True:
                        print('El numero: {} sera eliminado...\n'.format(number))
                        numberList.remove(number)
                        print(sorted(numberList))

                    else:
                        print('El numero: {} NO esta en lista y NO puede ser elimado.\n'.format(number))
            except ValueError:
                print('Tipo de dato invalido')

        elif command.lower() == 'b': #Busqueda de un numero, valida y busca
            print('------------>Buscar numero:<-----------\n')
            try:
                number = int(input('Dame el numero a buscar: \n'))

                if validation(number) is True:

                    if (number in numberList) is True:
                        print('El numero: {} SI esta en la lista\n'.format(number))
                    else:
                        print('El numero: {} NO esta en la lista\n'.format(number))
            except ValueError:
                print('Tipo de dato invalido')


        elif command.lower() == 's': #Salir del programa
            break

        else: #Mensaje de opcion invalida
            print('Elige una opcion valida\n')

def generateNumbers(): #Funcion que genera numeros aleatorios y los ordena
    number_list = [] #Crea una llista
    for number in range(0,1000): # 100 veces dura el loop para generar 1000 numeros
        random_number = rd.randint(1,5000) #Se genera en numero aleatorio entre 1-5000
        number_list.append(random_number) #Se agrega el numero a la lista generada arriba

    numberOrder = sorted(number_list) #Orden de la lista por emtodo QuickSort
    print('------------Lista en desorden----------\n')
    print(number_list)
    print('------------Lista Ordenada-------------\n')
    print(numberOrder)

    return numberOrder #Retorna la lista ordenada generada

def binary_search (numbers, number_to_find, low, high): #Funcion de busqueda binaria, recibe una lista, numero a buscar, tope bajo, tope alto.
    if low > high: #Comparacion de topes
        return False

    mid = (low + high)//2 #Punto medio de la lista

    if numbers[mid] == number_to_find: #Si el numero se encuentra en el punto medio
        return True

    elif numbers[mid] > number_to_find: #Recorrido por derecha a traves de la recursiva
        return binary_search(numbers, number_to_find,low, mid-1)

    else: #Recorrido por izquierda a traves de la recursiva
        return binary_search(numbers,number_to_find,mid+1,high)

def validation(number): #validacion del numero entrante
    flag = True

    if number < 0 or number >5000:
        print('Numero es menor a 0 o mayor a 5000 y no son aceptados')
        flag = False

    return flag

run() #Uso de funcion principal
