from flask_mail import Message
from flask import current_app,render_template

def confirmacion_compra(mail,user,book):
    try:
        message = Message('Confirmacion de compra de Libro',
        sender=current_app.config['MAIL_USERNAME'],
        recipients=[''])
        message.html = render_template('emails/confirmacion_compra.html',user=user,book=book)
        mail.send(message)
    except Exception as ex:
        raise Exception(ex)

