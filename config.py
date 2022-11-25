from decouple import config

class Config:
    SECRET_KEY = 'mjhti50cip'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ""
    MYSQL_DB = "store"
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME =''
    MAIL_PASSWORD = config('MAIL_PASSWORD')

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}