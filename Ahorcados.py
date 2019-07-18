import random


IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

WORDS = [ 'lavadora',
          'sacadora',
          'sofa',
          'gobierno',
          'diputado',
          'democracia',
          'computadora',
          'teclado']

def display_board(hidden_word,tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('---*---*---*---*---')

def random_word():
    idx = random.randint(0,len(WORDS)-1)
    return WORDS[idx]

def run():
    word = random_word()
    print('A H O R C A D O S')
    hidden_word= ['-'] * len(word)
    tries = 0

    while True:
        display_board(hidden_word,tries)
        current_letter = str(input('Escoge una letra: '))
        letter_indexes = []
        for idx in range(len(word)):
            if word[idx]==current_letter:
                letter_indexes.append(idx)

        if len(letter_indexes) == 0:
            tries +=1

            if tries ==7:
                display_board(hidden_word,tries)
                print('')
                print('Haz perdido ! La palabra correcta era : {}'.format(word))
                break

        else:

            for idx in letter_indexes:
                hidden_word[idx] = current_letter
            letter_indexes = []
        try:
            hidden_word.index('-')
        except ValueError:
            print('')
            print('Felicidades ganaste !! La palabra es: {}'.format(word))
            break
#Inicio
run()