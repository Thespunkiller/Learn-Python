file_name ="text.txt"

def number_of_char():
    with open(file_name, "r") as f:
        char = f.read(1)
        count = {}
        while char:
            if char in count.keys():
                count[char]+= 1
            else:
                 count[char] = 1 
            char = f.read(1)
    print(count)


number_of_char()