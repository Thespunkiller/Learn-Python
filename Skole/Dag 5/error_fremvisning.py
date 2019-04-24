try:

    #a = b
    f = open("text.txt", "r")
    data = f.read()

except FileNotFoundError:
    print("not found")
except NameError:
    print("fail name")
except Exception:
    print ("error error")
else:
    print("hvor er du god")
    print(data)
finally:
    f.close()


print("stuff")
