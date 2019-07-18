def binary_search(numbers,number_to_find,low,high):
    if low > high:
        return False

    mid = (low + high)/2

    if numbers[mid] == number_to_find:
        return True

    elif numbers[mid] > number_to_find:
        return binary_search(numbers, number_to_find, low,high)
    else:
        return binary_search()


numbers = [1,3,4,5,6,9,10,11,25,27,28,34,36,49,51]

number_to_find = int(input('Ingresa un numero:' ))
binary_search(numbers, number_to_find, 0, len(numbers)-1)