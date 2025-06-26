class book :
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
class library :
    def __init__(self):
        self._books = []
    def add_book(self, book) :
        self._books.append(book)
    def check_out_book(self, title) :
        self._books.remove(title)
    def return_book(self, title) :
        self._books.append(title)
    def list_available_books(self) :
        print(self._books)
