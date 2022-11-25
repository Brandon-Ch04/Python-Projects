class Book():
    def __init__(self,isbn,title,author,edition_year,price):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.edition_year = edition_year
        self.price = price
        self.sold_units = 0

        