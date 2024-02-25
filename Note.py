class Note:
    """Базовый класс телефонных абонентов"""
    notes_count = 0

    def __init__(self, noteText):
        #self.id = Subscriber.subscribers_count
        self.noteText = noteText
        self.notes_count += 1

    def printNote(self) -> str:
        toString = "" + self.noteText
        return toString