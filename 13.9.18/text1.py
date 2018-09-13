print("Vvedite a")
a = int(input())
print("Vvedite b")
b = int(input())
print("Vvedite c")
c = int(input())
d = b*b - 4*a*c
if d < 0:
    print("Net lorney")
elif d == 0:
    x = (-b)/(2*a)
    print("X = ", x)
else:
    x1 = (-b + d**0.5)/(2*a)
    x2 = (-b + d**0.5)/(2*a)
    print("x1 = ", x1)
    print("x2 = ", x2)
//123, 242, 252
