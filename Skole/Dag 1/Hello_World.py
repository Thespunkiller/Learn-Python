import datetime

value = "hello,\n\t world"
#print(value)

date = datetime.datetime(2019, 3, 1)
date_string = date.strftime("%d/%m/%Y")

print(date_string)
#print("please enter calculation")

input = input("please enter comma seperateded int:")
#print(input.upper())
ls = input.split(",")
print(ls)