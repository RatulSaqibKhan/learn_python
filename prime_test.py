number = input("Type a number and press Enter ")
number = int(number)
if number > 1:
    key = 0
    for i in range(number):
        if i < 2:
            continue
        if number % i == 0:
            key = 0
        else:
            key = 1
            break
    if key == 1:
        print(number,"is a prime!")
    else:
        print(number,"is not a prime!")
else:
    print(number,'is not a prime!')

            