string = "Hej du er"

words = string.split()

#string2 = words[2] + words[1] + words[0]

string2 = ""

i=len(words) -1 
while i >= 0:
    string2 +=words[i] + " "
    i -= 1


print (string2)



for i in range(1,10,4):
    print(i)

for i in range (10):
    print(i)


print(type(len(words)))


string4 = "Goddag"
print(string4[-3:].upper())
for x in string4:
    print(x)


try:
    x=y
    y.print()
except NameError:
    print("name error")
except TypeError:
    print("type fejl")
else:
    print("du god")
    