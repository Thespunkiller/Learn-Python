import os

def create_folder():
    os.chdir("C:\\Users\\Zaeed\\Desktop")
    os.makedirs("os_demo\\test\\tmp")

def rename():
    os.chdir("C:\\Users\\Zaeed\\Desktop\\os_demo\\test")
    os.rename("tmp", "temp")

def remove():
    os.chdir("C:\\Users\\Zaeed\\Desktop")
    os.removedirs("os_demo\\test\\tmp")

def search_dir(path, target):
    for dir_path, dir_names, file_names in os.walk(path):
        for f in file_names:
            if f == target: 
                print(dir_path)

#create_folder()
#rename()
#remove()

#search_dir("C:\\Users\\Zaeed\\Desktop\\os_demo", "test.txt")


def check_python_path():
    print("Python" in os.environ["PATH"])

#print(os.environ)
check_python_path()