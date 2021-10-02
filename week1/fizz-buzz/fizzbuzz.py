def fizzbuzz():
    list = []
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            list.append("Fizzbuzz")
        elif num % 5 == 0:
            list.append("Buzz")
        elif num % 3 == 0:
            list.append("Fizz")
        else:
            list.append(num)
    return list

