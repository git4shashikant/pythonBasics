import shutil
from os import path
from os import rename

# To copy all the information of original file to duplicate file like file permission,
# modification time or meta-data information by use code shutil.copystat(src,dst)

file_name = "../files/test.txt"

# create a new file in write mode to add data
file_obj = open(file_name, "w+")
for i in range(10):
    file_obj.write("This is line %d\r\n" % (i + 1))
file_obj.close()

# file append mode to add data
file_obj = open(file_name, "a+")
for i in range(2):
    file_obj.write("Appending line %d\r\n" % (i + 1))
file_obj.close()

if path.exists("../files/test.txt"):
    print("file location: {}".format(path.realpath("../files/test.txt")))

# read first 12 lines from a file
if path.exists("../files/test.txt"):
    file_obj = open(file_name, "r")
    for i in range(12):
        print(file_obj.readline())
    file_obj.close()

print("--------------")
# read all lines from a file
if path.exists("../files/test.txt"):
    file_obj = open(file_name, "r")
    for line in file_obj:
        print(line)
    file_obj.close()
print("--------------")

# read file content all at ones
if path.exists("../files/test.txt"):
    file_obj = open(file_name, "r")
    contents = file_obj.read()
    print(contents)
    file_obj.close()

# read lines one by one
if path.exists("../files/test.txt"):
    file_obj = open(file_name, "r")
    lines = file_obj.readlines()
    for i in lines:
        print(i)
    file_obj.close()

print(path.isfile("../files/test.txt"))
print(path.isdir("files"))

if not path.exists("../files/copy_test.txt"):
    shutil.copy("../files/test.txt", "../files/copy_test.txt")

if not path.exists("../files/copy_test.txt"):
    rename("../files/copy_test.txt", "files/test.bkp")

shutil.make_archive("files/test.bkp", 'zip')


