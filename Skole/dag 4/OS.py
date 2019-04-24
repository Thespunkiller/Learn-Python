import os

#print(os.getcwd())
#os.chdir("C:\\Users\Zaeed\\Desktop\\Python\\Dag 4\\test")
#os.makedirs("test\\test2")
#os.rename("test2","test2")
#os.removedirs("test\\test2")
#print(os.listdir())
#print(os.stat("test2"))
#time_stamp = datetime.datetime.fromtimestamp(os.stat("test2").st_mtime)
#print(time_stamp)

#print(dir(os))

#for dir_path, dir_names, file_names in os.walk(".."):
#    print("path", dir_path)
#    print("directories:", dir_names)
#    print("files", file_names)

#print( os.environ.get("HOMEPATH"))

#value = os.path.join(os.getcwd(), "test")
value = os.path.basename("test\\text.txt")
print (value)