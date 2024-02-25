# This is a sample Python script.
import Actions


def print_hi(name):
    while True:
        print("1 - Показать все заметки")
        print("2 - Добавить заметку и сохранить ее")
        print("3 - Удалить заметку")
        print("4 - Редактировать заметку")
        answer = input("Введите Номер операции или Q - для выхода \r")
        if answer == "1":
            Actions.show_all()
        elif answer == "2":
            Actions.add_new()
        elif answer == "3":
            Actions.delete()
        elif answer == "4":
            Actions.change()
        elif (answer == "q" or answer == "Q"):
            break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


