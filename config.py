HOST_NAME = 'localhost'
PORT = '3306'
DATABASE = 'SOA'
USERNAME ='root'
PASSWORD = 'csh0106lyx0120'
DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST_NAME}:{PORT}/{DATABASE}'

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
JSON_AS_ASCII = False