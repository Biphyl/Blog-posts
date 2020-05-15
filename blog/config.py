import os


class Config:
    SECRET_KEY = 'Lovine'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    DEBUG = True

class ProdConfig(Config):
    '''
    Production configuration child class
    Args:
        Config:The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

config_options = {
'development':DevConfig,
'production':ProdConfig,
# 'test':TestConfig
}