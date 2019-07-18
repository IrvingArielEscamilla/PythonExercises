def mayor(a,b):
    if(a>b and esPar(a)):
        return a
    else:
        return b

def esPar(a):
    if(a%2==0):
      return True
    else:
       return False

def run():
    a = int(input("Dame a: "))
    b = int(input("Dame b: "))
    c = int(input("Dame c: "))

    print(mayor(a,mayor(b,c)))

run()
