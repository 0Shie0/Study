x = int(input())
if x > 0 :
    print("x > 0")
    if x <= 10:
        print("0 .. 10")
    else:
        print("10 .. ...")
elif x == 0:
        print("x = 0")
else:
    print("x < 0")
    if x >= -10:
        print("-10 .. 0")
    else:
        print("... .. -10")
print("END")
