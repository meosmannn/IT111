import os

def create_file(path):
    f = open("file.txt", 'x')
    f.close()

def write_to_file(path, content):
    f = open("file.txt", 'w')
    f.write(content)
    f.close()

def append_to_file(path, content):
    f = open("file.txt", 'a')
    f.write(content)
    f.close()

def delete_file(path):
    if os.path.exists("file.txt"):
        os.remove("file.txt")
    else:
        print("This file does not exist.")

create_file('file.txt')
write_to_file('file.txt', 'This will write to a file.')
append_to_file('file.txt', 'This will append to a file.')
delete_file('file.txt')
    
