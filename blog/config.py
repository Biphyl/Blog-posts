import os


class Config:
    SECRET_KEY = 'Lovine'
    SQLALCHEMY_DATABASE_URI = 'postgres://quicswskimygnc:a6007b777f1c5937303b5b967f9bed26702675268fc0bd2172a4e2f382a3f3ff@ec2-35-169-254-43.compute-1.amazonaws.com:5432/dacv4uebqhv4bs'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://quicswskimygnc:a6007b777f1c5937303b5b967f9bed26702675268fc0bd2172a4e2f382a3f3ff@ec2-35-169-254-43.compute-1.amazonaws.com:5432/dacv4uebqhv4bs'
    DEBUG = True

class ProdConfig(Config):
    '''
    Production configuration child class
    Args:
        Config:The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgres://quicswskimygnc:a6007b777f1c5937303b5b967f9bed26702675268fc0bd2172a4e2f382a3f3ff@ec2-35-169-254-43.compute-1.amazonaws.com:5432/dacv4uebqhv4bs'

config_options = {
'development':DevConfig,
'production':ProdConfig,
# 'test':TestConfig
}