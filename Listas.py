def average_temps(temps):
    sum_of_temps = 0

    for temp in temps:
        sum_of_temps += float(temp)

    return sum_of_temps / len(temps)


def run():

    temps = [21,24,24,22,20,23,24]
    average = average_temps(temps)
    print('la temperatura promedio es: {}'.format(average))

run()
