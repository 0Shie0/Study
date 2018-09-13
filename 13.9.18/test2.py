import random
x = random.randint(0,10)
a = 1
while a == 1:
    b = int(input())
    if b == x:
        print("Yeeey")
        a = 0
    else:        
        print("Error")
print("END")
