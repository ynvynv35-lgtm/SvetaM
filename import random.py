import random
number1 = random.randint(1, 10)
number2 = int(input())

while number2 != number1:
    if number2 > number1:
        print ("很多")
    elif number2 < number1:
        print ("很少")
    else:
        print ("好啊!")
    number2 = int(input())
    print('Hello, Sveta!!!')
