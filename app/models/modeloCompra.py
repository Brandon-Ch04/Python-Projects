from .entities.purchase import Purchase
from .entities.Book import Book




class ModeloCompra():
    
    @classmethod
    def registrar_compra(self,db,purchase):
        try:
            cursor = db.connection.cursor()
            sql = "INSERT INTO purchase (uuid, book_isbn, user_id) VALUES (uuid(), '{0}', {1})".format(purchase.book.isbn,purchase.user.id)
            cursor.execute(sql)
            db.connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def listar_compras_usuario(self,db,user):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT PUR.date,BO.isbn,BO.title,BO.price FROM purchase PUR JOIN store BO ON PUR.book_isbn = BO.isbn WHERE PUR.user_id = {0}".format(user.id)
            cursor.execute(sql)
            data = cursor.fetchall()
            compras = []
            for row in data:
                bo = Book(row[1],row[2],None,None,row[3])
                pur = Purchase(None,bo,user,row[0])
                compras.append(pur)
            return compras

            
            
        except Exception as ex:
            raise Exception(ex)