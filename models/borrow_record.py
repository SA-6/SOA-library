from extensions import db


class BorrowRecord(db.Model):
    __tablename__ = 'borrow_record'
    record_id = db.Column(db.String(10), primary_key=True)
    user_id = db.Column(db.String(10), db.ForeignKey('userinfo.user_id'))
    book_id = db.Column(db.String(10), db.ForeignKey('bookinfo.book_id'))
    borrow_date = db.Column(db.Date())
    due_date = db.Column(db.Date())

    def to_dict(self):
        return {
            'record_id': self.record_id,
            'user_id': self.user_id,
            'book_id': self.book_id,
            'borrow_date': self.borrow_date.strftime('%Y-%m-%d') if self.borrow_date else None,
            'due_date': self.due_date.strftime('%Y-%m-%d') if self.due_date else None
        }
