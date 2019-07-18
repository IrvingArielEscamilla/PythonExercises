#Operadores artimeticos
# + - / * // ** %
#Operadoes de comparacion
# == != <> > < >= <=
#Operadores logicos
# or  and not
#Operadores sobre bits
# & \ ~ << >>
#Operadores de asignacion
# = += -= /= *= %= **= &= \=
# ^= >>= <<=
#Otros operadores
#i in is

#Orden de operaciones PEMDAS
# parentesis, exponente, multiplicacion y division, adicion y sustraccion

a = 3
b = 9
print('---Operadores artimeticos---')
print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a//b)
print(a**b)
print(a%b)

print('---Operadores de comparacion---')
print(a==b)
print(a!=b)
#print(a<>b) No soportado en version 3
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print('---Operadores logicos')
print(0 or 2)
print(True and 0)
print(False or 1)
print([] or 1)
print([1] or 1)
print("hola" and "Irving" and 0)
print('hola' and 0 or "Sting")

print('---Operadores sobre bits')
print(4&2)
print(7&2)
print(4|2)
print(7|2)
print(4^2)
print(7^2)
print(~3)



