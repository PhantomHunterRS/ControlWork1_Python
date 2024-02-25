import Note
import WorkWithFiles


def show_all():
    WorkWithFiles.read_file()


def add_new():
    answerQ1 = input("Введите заметку:\n")
    note = Note.Note(answerQ1)
    WorkWithFiles.add_in_file(note.printNote())


def delete():
    print("Для поиска и удаления заметки введите тектс")
    answerQ1 = input("Какую заметку ищем и удаляем:\n")
    WorkWithFiles.search_delete([answerQ1])


def change():
    pass


def new_file():
    answerQ1 = input("Укажите новый файл:\n")
    answerQ2 = input("Строку которую надо скопировать:\n")
    WorkWithFiles.copy_Subscriber_new_file(int(answerQ2), answerQ1)