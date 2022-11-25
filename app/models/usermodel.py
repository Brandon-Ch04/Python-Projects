from .entities.User import User
from .entities.Tipousuario import Tipousuario


class UserModel():
    
    @classmethod
    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id,user,password FROM user WHERE user = '{0}'".format(user.user)
            cursor.execute(sql)
            data = cursor.fetchone()                                   
            if data != None:

            
                coincide = User.verificar_password(data[2], user.password)
            
                if coincide:
                    usuario_logeado = User(data[0],data[1],None,None)
                    return usuario_logeado
                else:
                    return None
            else:
                return None                      
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def obtener_por_id(self,db,id):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT USU.id,USU.user,TIP.id,TIP.nombre FROM user USU JOIN tipousuario TIP ON USU.tipousuario_id = TIP.id WHERE USU.id = {0}".format(id)
            cursor.execute(sql)
            data = cursor.fetchone()                                   
            tipousuario = Tipousuario(data[2], data[3]) 
            usuario_logeado = User(data[0], data[1], None, tipousuario)
            return usuario_logeado
        except Exception as ex:
            raise Exception(ex)
