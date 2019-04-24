#def say():
 #   print("ppp")

#def return_hello():
  #  return "hello"

#placeholder
#def pas():
 #   pass

#print(say())

#def greeting(end,greeting = "hello", recipient = "world"):
#    return "{} {}{}".format(greeting,recipient, end)

#print (greeting("."))
#print(greeting("!", recipient= "peter", greeting="hej"))


def my_sum(*args):
    return sum(args)

dict = {"name": "john", "age": 32, "hair" : True}

def up_dic(**kwargs):
    kwargs["name"] = "john"
    dict.update(kwargs)


#print(create_dic(name = "peter", age = 40, hair = false))
print(dict)
up_dic(name = "peter", age = 40)
print (dict)

print(my_sum(2,3,5,2,3))