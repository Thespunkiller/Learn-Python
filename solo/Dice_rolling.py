from random import randint


c = input("would u like to play y/n\n")
i = 0 
while c == ("y") :
    value = randint(1, 6)
    print (value)
    c = input("would u like to play again\n")

if c == ("n") :
    print ("See you another time")