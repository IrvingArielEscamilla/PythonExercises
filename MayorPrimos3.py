def is_impar(number):

    if(number%2==0):
        return False
    else:
        return True

    return True




numbers = []
impar = []
def run():
    a = int (input("Dame a:"))
    b = int (input("Dame b:"))
    c = int (input("Dame c:"))

for i in numbers:
    if(is_impar(i)==True):
        impar.append(i)
    print(impar)

run()