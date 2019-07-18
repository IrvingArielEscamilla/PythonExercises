

def run():
    list = []
    number =0
    while(number<10):
        numberA = int(input('Dame numero'))
        list.append(numberA)
        number +=1

    print(sorted(list))
    print(list[-1])





run()