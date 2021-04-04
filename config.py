class LocalConfig(object):
    DEBUG = True
    DEVELOPMENT = True
    SECRET_KEY = 'do-i-really-need-this'
    SQLALCHEMY_DATABASE_URI='sqlite:////home/mahrezbh/Project/Flask_project/database.db'

class ProductionConfig(LocalConfig):
    DEVELOPMENT = False
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://iemfcubqifxgal:f920816deea058a2ce1f12f32addda426c3898a3a8212ea5a71c1f1420f6aa01@ec2-18-233-83-165.compute-1.amazonaws.com:5432/d70dhgmfvp5b7t'