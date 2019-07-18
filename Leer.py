def run():
    counter = 0
    with open('aleph.txt') as f:
        for line in f:
            counter += line.count('Beatriz')
    print('Beatriz se encuentra {} en el texto'.format(counter))
run()