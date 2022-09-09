from random import randint

number = 0
while number != 5:
    number = randint(0, 9)
    if number == 5:
        break

    print(number)
    
print('我碰到5了....Orz')