class LocalConfig(object):
    DEBUG = True
    DEVELOPMENT = True
    SECRET_KEY = 'do-i-really-need-this'
    SQLALCHEMY_DATABASE_URI='sqlite:////home/mahrezbh/Project/Flask_project/database.db'

class ProductionConfig(LocalConfig):
    DEVELOPMENT = False
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://gaybmgxvefbgjb:79057563830eb77ea7276f08bf58ddc04f84802e2c6e5e88e2b053a617de64da@ec2-18-206-20-102.compute-1.amazonaws.com:5432/da3a6a82vsnpti'