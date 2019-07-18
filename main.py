from Lamp import Lamp

def run():
    lamp = Lamp(is_turned_on=False)

    while True:
        command = str((input('''

         Elige una opcion:

         [p]render
         [a]pagar
         [s]alir      

        ''')))
        if command == 'p':
            lamp.turn_on()
        elif command == 'a':
            lamp.turn_off()
        else:
            break


run()