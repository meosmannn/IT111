import os

def update_file(original, copy):
    f = open(original, 'a')
    print("Add text you want to append and press enter:")
    text_to_append = input()
    f.write('\n' + text_to_append)
    f.close()


    f = open(original, 'r')
    f1 = open(copy, 'w')
    for line in f:
        f1.write(line)
    f.close()


    if os.path.exists(original):
        os.remove(original)
    else:
        print("This file does not exist.")


update_file('Project2Input.txt', 'Project2Update.txt')
