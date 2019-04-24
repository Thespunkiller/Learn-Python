
def min_max(data):
    max = data[0]
    min = data[0]
    for num in data:
        if num > max :
            max = num
        if num < min :
            min = num
    return min, max


#print(min_max([2,2,4,6,7,9]))