from flask import Flask
from flask_cors import CORS
import config
from flask_migrate import Migrate

from apis.borrowrecord import borrow_records_bp
from apis.returnrecord import return_records_bp
from extensions import db

from models.bookinfo import BookInfo
from models.userinfo import UserInfo
from models.borrow_record import BorrowRecord
from models.return_record import ReturnRecord

from apis.bookinfo import bookinfo_bp
from apis.userinfo import userinfo_bp

app=Flask(__name__)
app.config.from_object(config)
db.init_app(app)
migrate = Migrate(app,db)

app.register_blueprint(bookinfo_bp)
app.register_blueprint(userinfo_bp)
app.register_blueprint(borrow_records_bp, url_prefix='/borrow_records')
app.register_blueprint(return_records_bp,url_prefix='/return_records')

CORS(app, resources=r'/*')
if __name__ == '__main__':
    app.run(debug=True ,host='0.0.0.0', port=8080)