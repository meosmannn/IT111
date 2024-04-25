import re

def search_file():
    filename = input("Enter the name of the file to be searched: ")

    txt = input("Enter a search character expression: ")

    found = False

    try:
        with open(filename) as f:
            for line in f:
                match = re.search(txt, line)
                if match:
                    print(match.string)
                    found = True
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
        return

    if not found:
        print(f"The character expression '{txt}' was not found in the file {filename}.")
    else:
        print(f"The character expression '{txt}' was found in the file {filename}.")

search_file()
