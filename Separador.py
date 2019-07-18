def separate(message):
    n =8
    subString= [message[i:i+n] for i in range(0,len(message),n)]
    return subString


def run():

    message = str(input('Dame el mensaje:'))
    print(separate(message))

run()