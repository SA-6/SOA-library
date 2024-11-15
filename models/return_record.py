from extensions import db

class ReturnRecord(db.Model):
    __tablename__ = 'return_record'
    record_id = db.Column(db.String(10), primary_key=True)
    user_id = db.Column(db.String(10), db.ForeignKey('userinfo.user_id'))
    book_id = db.Column(db.String(10), db.ForeignKey('bookinfo.book_id'))
    return_date = db.Column(db.Date())