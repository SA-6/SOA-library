HOST_NAME = 'localhost'
PORT = '3306'
DATABASE = 'soa'
USERNAME ='root'
PASSWORD = '123456'
DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST_NAME}:{PORT}/{DATABASE}'

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
JSON_AS_ASCII = False