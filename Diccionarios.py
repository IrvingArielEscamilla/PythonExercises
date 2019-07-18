calificaciones = {}
calificaciones['Algoritmos'] = 9
calificaciones['Ing_Software'] = 10
calificaciones['Bases_de_datos']= 8
calificaciones['Web'] = 8

for key in calificaciones:
    print(key)

for value in calificaciones.values():
    print(value)

for key, value in calificaciones.items():
    print('Llave: {}, valor: {}'.format(key,value))

suma_de_calificaciones = 0

for  calificacion in calificaciones.values():
    suma_de_calificaciones += calificacion

promedio = suma_de_calificaciones /len(calificaciones.values())
print(promedio)