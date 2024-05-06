class Library:
    def __init__(self, title, year, last_seen):
        self.title = title
        self.year = year
        self.last_seen = last_seen
        self.books = [{'title':'The Alchemist','year':1988, 'last seen': 1}, {'title':'The Great Gatsby','year':1925, 'last seen': 10},{'title':'The Chronicles of Narnia ','year':1950, 'last seen': 25}, {'title':'1984','year':1949, 'last seen': 5}]            
        def printTitles(books):
            for book in books:
                print(book['title'])

        def checkYear(book):
            if book['year'] > 2010:
                return True
            else:
                return False

        def booksToCheck(books):
            checked_books = []
            for book in books:
                if checkYear(book):
                    checked_books.append(book)
            return checked_books

        def suspectedBooks(books_to_check):
            suspected_books = []
            for book in books_to_check:
                if book['last seen'] == 1:
                    suspected_books.append(book)
            def suspectedBooks(books_to_check):
                suspected_books = []
                for book in books_to_check:
                    if book['last seen'] == 1:
                        suspected_books.append(book)
                printTitles(suspected_books)  # Call the printTitles() function to print the titles of suspected books
                return suspected_books
