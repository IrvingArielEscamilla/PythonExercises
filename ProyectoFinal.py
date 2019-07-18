'''
@ Irving  Ariel Escamilla Jacobo
Algoritmia

'''
#import pyperclip

def run():
    alpha = 'abcdefjhijklmnopqrstuvwxyz'

    while True:
        command = str(input('''
        --------Descifrador de texto------
        
        [L]eer archivo
        [D]escifrar mensaje
        [S]alir
               
        '''))
        #Lectura de texto
        if command.upper() == 'L':
            #print('---Leer  el mensaje---')
            #print('----------Original Text---------')
            #f = open('aleph.txt')
            #text = f.read()
            #print(text)


            #print('---------------Non Accent--------------')
            #nonAcennt = nonAccentMark(text)
            #print(nonAcennt)

            #print('--------------Text separate------------')
            #text = nonAcennt.split()

            #print(text)

            #f.close()

            #cypherCesar()
            decypherCesar()

        elif command.upper() == 'D':
            print('Descifrar el mensaje:')

        elif command.upper() == 'S':
            print('Saliendo...')
            break
        else:
            print('Comando no encontrado.')



def decypher(message):
    pass

def nonAccentMark(text):
    non_accent = "AEIOUaeiou"
    with_accent = 'ÁÉÍÓÚáéíóú'
    accent_inv ='ÀÈÌÒÙàèìòù'
    accent_up='ÂÊÎÔÛâêîôû'

    for i in range (len(non_accent)):
        text =  text.replace(with_accent[i],non_accent[i])
        text = text.replace(accent_inv[i],non_accent[i])
        text = text.replace(accent_up[i],non_accent[i])
    return text.lower()

def cypherCesar():
    ALPHA = 'abcdefghijklmnopqrstuvwxyz'
    cypherMessage = ''
    command = input('Cifrado/Descifrado (c/d)')
    text = input('Dame el texto a cifrar: ')
    id = int(input('Clave  (1-25): '))

    for simbol in text.lower():
        if simbol in  ALPHA:
            pos = ALPHA.find(simbol)

            if command == 'c':
                pos = (pos+id) % 26
            elif  command == 'd':
                pos = (pos-id) % 26

            cypherMessage += ALPHA[pos]

        else:
            cypherMessage += simbol

    print(cypherMessage)

    #pyperclip.copy(cypherMessage)

def decypherCesar():
    ALPHA = 'abcdefghijklmnopqrstuvwxyz'

    cripto = input('Criptograma: ')

    for key in range (1,len(ALPHA)):

        descypherMessage = ''

        for simbol in cripto :
            if simbol in ALPHA:
                pos = ALPHA.find(simbol)

                pos = (pos-key) % len(ALPHA)

                descypherMessage +=ALPHA[pos]

            else:

                descypherMessage += simbol

        print('Clave: {} : {}.'.format(key,descypherMessage))

def countLetters(text):
    counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    alpha = "abcdefghijklmnopqrstuvwxyz"
     text= text.lower()
    for c in :
        if (c in alpha):
            pos = alpha.find(c)
            counts =[pos] = counts =[pos] + 1
    return (counts = )

run()