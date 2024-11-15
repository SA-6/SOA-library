from extensions import db
from datetime import datetime

class BookInfo(db.Model):
    __tablename__ = 'bookinfo'
    book_id = db.Column(db.String(10), primary_key=True)
    book_name = db.Column(db.String(255))
    author = db.Column(db.String(255))
    description = db.Column(db.Text())
    image_path = db.Column(db.Text())
    publisher = db.Column(db.String(20))
    publisher_time = db.Column(db.Date())
    isbn = db.Column(db.String(100))
    category = db.Column(db.String(255))
    code = db.Column(db.String(255))
    price = db.Column(db.Float())
    start_time = db.Column(db.DateTime())
    end_time = db.Column(db.DateTime())
    should_return_date = db.Column(db.DateTime())
    borrow_status = db.Column(db.CHAR(3))
    ebook = db.Column(db.Text())
    search_num = db.Column(db.Integer())