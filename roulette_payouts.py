from random import randint

for _ in range(1):
    value = randint(0, 37)
    if 1 <= value <= 36:
        print("The spin resulted in", value)
        print("Pay", value)
    elif value == 0:
        print("The spin resulted in 0")
    else:
        print("The spin resulted in 00")

f = value % 2

if 1 <= value <= 36 and f == 1:
    print("Pay Black")
    print("Pay Odd")
elif 1 <= value <= 36 and f == 0:
    print("Pay Red")
    print("Pay Even")
elif value == 0:
    print("Pay 0")
else:
    print("Pay 00")

while 1 <= value <=18:
    print("Pay 1 to 18")
    break

while 19 <= value <= 36:
    print("Pay 19 ro 36")
    break



