from random import randint


hidden = randint(1, 6)

print("this is the hidden number ",hidden)

inp = int(input("guess a number\n"))

while inp != hidden:
    inp = int(input("guess a number\n"))
    if inp < hidden :
        print("to low")
    elif inp > hidden:
        print("to high")
    elif inp == hidden:
        print("correct")






