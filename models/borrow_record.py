from extensions import db

class BorrowRecord(db.Model):
    __tablename__ = 'borrow_record'
    record_id = db.Column(db.String(10), primary_key=True)
    user_id = db.Column(db.String(10), db.ForeignKey('userinfo.user_id'))
    book_id = db.Column(db.String(10), db.ForeignKey('bookinfo.book_id'))
    borrow_date = db.Column(db.Date())
    due_date = db.Column(db.Date())