from flask import Flask,render_template,request,url_for,redirect,flash,jsonify
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager,login_user,logout_user,login_required,current_user
from flask_mail import Mail


from .consts import *
from emails import confirmacion_compra


from .models.modeloCompra import ModeloCompra
from .models.bookmodel import BookModel
from .models.usermodel import UserModel

from .models.entities.User import User
from .models.entities.purchase import Purchase
from .models.entities.Book import Book




app = Flask(__name__)

csrf = CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)
mail = Mail()



@login_manager_app.user_loader
def load_user(id):
    return UserModel.obtener_por_id(db,id)


@app.route('/login', methods=['GET','POST'])

def login():       
    if request.method == 'POST':       
        user = User(None,request.form["User"],request.form["Password"],None)
        usuario_logeado = UserModel.login(db,user)
        if usuario_logeado != None:
            login_user(usuario_logeado)
            flash(LOGIN_MSG,"success")
            return redirect(url_for('index'))
        else:
            flash(LOGIN_CREDENCIALESINVALIDAS,'warning')
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

@app.route('/logout')
def logout():
    logout_user()
    flash(LOGOUT,'success')
    return redirect(url_for("login"))

@app.route('/')
@login_required
def index():
    if current_user.is_authenticated:
        if current_user.tipousuario.id == 1:
            try:
                libros_vendidos = BookModel.listing_sold_books(db)
                data = {
                    'titulo': 'Books Sold:',
                    'libros_vendidos': libros_vendidos
                }
                return render_template("index.html",data = data)
            except Exception as ex:
                return render_template('errors/error.html',mensaje=format(ex))    
        else:
            try:

                compras = ModeloCompra.listar_compras_usuario(db,current_user)
                data = {
                    'titulo': 'My books:',
                    'compras':compras
                }
                return render_template("index.html",data = data)
            except Exception as ex:

                return render_template('errors/error.html',mensaje=format(ex))    

        
    else:
        return redirect(url_for('index'))




@app.route('/books')
@login_required
def book_listing():
    try:
        books = BookModel.listing_books(db)
        data = {
            'titulo':'Book listing',
            'books':books
        }
        return render_template('book_listing.html', data = data)

    except Exception as ex:
        return render_template('errors/error.html',mensaje=format(ex))              
    



@app.route('/comprarLibro',methods=['POST'])
@login_required
def comprar_libro():
    data_request = request.get_json()
    print(data_request)
    data = {}
    try:
        #book = Book(data_request['isbn'],None,None,None,None)
        book = BookModel.leer_libro(db,data_request['isbn'])
        
        purchase = Purchase(None,book,current_user)               
        data['exito'] = ModeloCompra.registrar_compra(db,purchase)
        confirmacion_compra(mail,current_user,book)
    except Exception as ex:
        data['mensaje'] = format(ex)
        data['exito'] = False
    return jsonify(data)





def page_not_found(error):
    return render_template('errors/404.html'), 404





def unauthorized_page(error):
    return redirect(url_for('login'))





def inicializar_app(config):
    app.config.from_object(config)
    csrf.init_app(app)
    mail.init_app(app)
    app.register_error_handler(401,unauthorized_page)
    app.register_error_handler(404, page_not_found)
    return app