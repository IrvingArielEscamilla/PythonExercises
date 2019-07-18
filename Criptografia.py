KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
    ' ': '+'
}


def cypher(message):
    words = message.split('\b')
    cypher_message = []

    for word in words:
        cypher_word = ''
        for letter in word:
            cypher_word += KEYS[letter]

        cypher_message.append(cypher_word)

    return''.join(cypher_message)


def decypher(message):
    words = message.split('\b')
    decipher_message = []

    for word in words:
        decipher_word =''

        for letter in word:
            for key, value in KEYS.items():
                if value == letter:
                    decipher_word += key
        decipher_message.append(decipher_word)

    return ''.join(decipher_message)


while True:
    command = str(input('''

    Bienvenido a criptografia.
    
    [C]ifrar mensaje
    [D]ecifrar mensaje
    [S]alir
    
    '''))

    if command =='C':
        print('Cifrar')
        message = str(input('Escribe tu mensaje:'))
        cypher_message = cypher(message)
        print(cypher_message)

    elif command == 'D':
        print('Decifrar')
        message = str(input('Escribe tu mensaje cifrado: '))
        decypher_message = decypher(message)
        print(decypher_message)

    elif command == 'S':
        print('Salir')
        break

    else:
        print('Comando no encontrado')