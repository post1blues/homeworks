
def write_file():
    with open("myfile.txt", 'w', encoding="utf-8") as file:
        file.write("Hello file world!\n")


def read_file():
    with open("myfile.txt", 'r', encoding="utf-8") as file:
        data = file.read()
    print(data)


if __name__ == '__main__':
    write_file()
    read_file()