file_path = 'notes.txt'


def add_in_file(text):
    with open(file_path, 'a+', encoding="cp1251") as file:
        file.write(text + '\r')


def read_file():
    with open(file_path, encoding="cp1251") as file:
        for line in file:
            print(line.strip())
        print()


def search_delete(information):
    with open(file_path, 'r', encoding="cp1251") as file:
        data = file.readlines()
        del_subscriber = f'{information[0]}\n'
        data.remove(del_subscriber)
    with open(file_path, 'w', encoding="cp1251") as new_file:
        new_file.writelines(data + '\n')


def find_line(line: int)->str:
    with open(file_path, 'r', encoding="cp1251") as file:
        data = file.readlines()
        for x_line in range(0, len(data)):
            if((x_line+1) == line):
                return data[x_line]
        print('Строка не найдена')
        return 0