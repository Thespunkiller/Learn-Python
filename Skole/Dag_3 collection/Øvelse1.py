#tuple fungere som getter fra java og c# 
#hvilket gør den ikke kan ændres men og kan bruges 
#
values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)
