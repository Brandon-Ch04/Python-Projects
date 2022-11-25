from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin



class User(UserMixin):
    
    def __init__(self, id, user, password, tipousuario):
        self.id = id
        self.user = user
        self.password = password
        self.tipousuario = tipousuario


    @classmethod
    def verificar_password(self,encriptado,password):        
        return check_password_hash(encriptado, password)
        