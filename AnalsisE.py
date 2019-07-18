
def mayor(a,b):
    if (a > b):
        return a
    else:
        return  b

def run():
    list = []
    a = int(input('Dame a: '))
    b = int(input('Dame b: '))
    c = int(input('Dame c:' ))

    print(mayor(a, mayor(b, c)))

run()