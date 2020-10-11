while True:
    try:
        number1 = int(input('Number1: '))
        if number1 < 1 or number1 > 10:
            raise ValueError #this will send it to the print message and back to the input option
        break
    except ValueError:
        print("Invalid integer. The number must be in the range of 1-10.")