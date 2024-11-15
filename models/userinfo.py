from extensions import db

class UserInfo(db.Model):
    __tablename__ = 'userinfo'
    user_id = db.Column(db.String(10), primary_key=True)
    user_name = db.Column(db.String(100))
    password = db.Column(db.String(20))
    email = db.Column(db.String(30))
    user_type = db.Column(db.CHAR(7))
    last_login_time = db.Column(db.DateTime())
    prefer_type = db.Column(db.String(255))
    balance = db.Column(db.Float())
    borrow_book_num = db.Column(db.Integer())
    search_num = db.Column(db.Integer())