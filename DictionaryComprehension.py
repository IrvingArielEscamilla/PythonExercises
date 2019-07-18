
#list comprehension
pares = []
for n in range (1,31):
    if n%2 == 0:
        pares.append[(n)]

even = [num for num in range (1,31) if num%2 ==0]


cuadrados = {}

for num in range (1,11):
    cuadrados[num] = num **2

cuadrados
#dictionary comprehension
    #sugar sintactic

squares = {num: num**2 for num in range(1,11)}