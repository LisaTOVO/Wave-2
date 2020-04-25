l = str(input("Please enter the letter of that row: "))
n = int(input("Please enter the number of thart row: "))


while (l == "a") or (l == "c") or (l == "e") or (l == "g"):
    if (n == 1) or (n == 3) or (n == 5) or (n == 7):
        print("The square is black")
    else:
        print("The square is white")
    break

while (l == "b") or (l == "d") or (l == "f") or (l == "h"):
    if (n == 2) or (n == 4) or (n == 6) or (n == 8):
        print("The square is black")
    else:
        print("The square is white")
    break