def cargaPalabras():
    archivo=open('words.txt','r')
    renglon=archivo.readline()
    palabras=renglon.split()
    #print(len(palabras),'palabraas leidas')
    return(palabras) #carga eldiccionario
listaPal=cargaPalabras()

def cargaCifrado():
    archivo=open('textoCifrado.txt','r')
    renglon=archivo.readline()
    return(renglon) #abre texto cifrado

cad=cargaCifrado()
cadena=cad.split('\b')
message=str(cadena)

def descifrar(message):
    LETTERS = "abcdefghijklmnopqrstuvwxyz"
    for key in range(len(LETTERS)):
        if key==19:
            break
        else:
            translated = ""
            for symbol in message:
                if symbol in LETTERS:
                    num = LETTERS.find(symbol)
                    num = num - key
                    if num < 0:
                         num = num + len(LETTERS)
                    translated = translated + LETTERS[num]
                else:
                    translated = translated + symbol
            #print("Descifrando con Key #%s: %s" % (key, translated))
    return(translated)

print(descifrar(message))
