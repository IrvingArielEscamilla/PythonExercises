def validing_word(word, alphabet):
    wordSet = set(word)
    characters = alphabet.split(',')
    alphabetSet = set()

    for character in characters:
        alphabetSet.add(character)
    isSet = wordSet.issubset(alphabetSet)

    return isSet

def run():
    alphabet = str(input('Dame el alfabeto: '))
    word = str(input('Dame la palabra: '))

    if(validing_word(word,alphabet)==True):
        print('La palabra: {} es VALIDA para el alfabeto: [{}]'.format(word,alphabet))
    else:
        print('La palabra: {} NO es valida para el alfabeto: [{}]'.format(word,alphabet))

run()