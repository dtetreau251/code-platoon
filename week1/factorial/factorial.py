def factorialize(num):
    factorial = 1

    while num > 1:
        if num == 0 or num == 1:
            print("invalid number")
            break
        else:
            factorial *= num
            num -= 1
    return factorial 

print(factorialize(5)) # equals 120