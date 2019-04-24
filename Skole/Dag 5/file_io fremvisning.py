# read = r
# write = w
# read and wirte = r+
# append = a
# read as bytes = rb 
# write byte = wb 

#bad practice
#f = open("text.txt", "r")
#print(f.read())
#f.close

#s fucking tog 
#with open("text.txt", "r") as f:
    #print(f.read())
    #print(f.name)
    #print(f.mode)
#    print(f.closed)

#    for value in f:
#        print(value,end= "")
    
#    data = f.read(10)
#    while len(data)>0 :
#        print("*",data)
#        data = f.read(10)

#    data = f.readline()
#    while len(data)>0 :
#        print("*",data)
#        data = f.readline()

    #data = f.readlines()
    #for line in data:
    #    print(line)
    
 #   f.seek(21)
 #   print(f.tell())
 #   print(f.read(5))
 #   print(f.tell())
 #   print(f.readline())
 #   print(f.tell())
 #   print(f.tell())


#with open("text.txt" , "r") as rf:
#    with open("text_copy.txt", "w") as wf:
#        for line in rf:
#            wf.write(line.upper())

with open("ss.jpeg" , "rb") as brf:
    with open("ss.copy.jpeg", "wb") as bwf:
        for line in brf:
            bwf.write(line)



#print(f.closed)