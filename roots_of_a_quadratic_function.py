import math

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

d = (b ** 2) - (4 * a * c)

if d < 0:
    print("There are 0 roots")
elif d == 0:
    r = (-b / (2 * a))
    print("There is 1 root, and its value is: ", r)
elif d > 0:
    r2 = ((-b + math.sqrt(d)) / (2 * a))
    r3 = ((-b - math.sqrt(d)) / (2 * a))
    print("There are 2 roots, and there values are: ", r2, "and", r3)
else:
    print("Invalid value")

print(d)