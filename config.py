import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:asyu%40234kop4912##@localhost:3306/cybers'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
