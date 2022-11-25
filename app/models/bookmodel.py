from .entities.Author import Author
from .entities.Book import Book
class BookModel():
    
    @classmethod
    def listing_books(self,db):

        try:
            cursor=db.connection.cursor()
            sql = """SELECT BO.isbn,BO.title,BO.edition_year,BO.price,AUT.last_name,AUT.name 
                 FROM store AS BO JOIN author AS AUT ON BO.author_id = AUT.id
                 ORDER BY title ASC"""
            cursor.execute(sql)
            data = cursor.fetchall()
            books = []
            for row in data:
                Auth = Author(0,row[4],row[5])
                Bo = Book(row[0], row[1],Auth,row[2],row[3])
                books.append(Bo)
            return books
        except Exception as ex:
            raise Exception(ex)
    

    @classmethod
    def leer_libro(self,db,isbn):
        try:
            cursor=db.connection.cursor()
            sql = """SELECT isbn, title, edition_year, price 
                    FROM store WHERE isbn = '{0}'""".format(isbn)
            cursor.execute(sql)
            data = cursor.fetchone()
            books = Book(data[0], data[1], None, data[2], data[3])
            
            return books
        except Exception as ex:
            raise Exception(ex)



    @classmethod
    def listing_sold_books(self,db):

        try:
            cursor=db.connection.cursor()
            sql = """SELECT PUR.book_isbn,STR.title,STR.price,
                     COUNT(PUR.book_isbn) AS sold_units 
                     FROM purchase PUR JOIN store STR ON PUR.book_isbn = STR.isbn
                     GROUP BY PUR.book_isbn ORDER BY 4 DESC, 2 ASC"""
            cursor.execute(sql)
            data = cursor.fetchall()
            books = []
            for row in data:
                
                Bo = Book(row[0], row[1],None,None,row[2])
                Bo.sold_units = int(row[3])
                books.append(Bo)
            return books
        except Exception as ex:
            raise Exception(ex)
