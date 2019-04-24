
def my_sum(*args):
    return sum(args)
    

def int_list(str_list):
    """this is a doc string. this method return a list of int based on a list of givin strings """
    int_list = []
    for s in str_list:
        int_list.append(int(s))
    return(int_list)

values = int_list(input("input numbers").split(","))

print (my_sum(*values))