t = input ("giv mig tekst")

def new_string(t):
    if t[:2] == "Is":
        return t
    return "IS" + t
print(new_string(t))