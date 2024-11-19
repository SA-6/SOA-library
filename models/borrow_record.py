from extensions import db


class BorrowRecord(db.Model):
    __tablename__ = 'borrow_record'
    record_id = db.Column(db.String(10), primary_key=True)
    user_id = db.Column(db.String(10), db.ForeignKey('userinfo.user_id'))
    book_id = db.Column(db.String(10), db.ForeignKey('bookinfo.book_id'))
    borrow_date = db.Column(db.Date())
    due_date = db.Column(db.Date())
    @staticmethod
    def format_date(date_obj):
        if date_obj:
            return date_obj.strftime('%Y-%m-%dT%H:%M:%S.000+00:00')
        return None

    def to_dict(self):
        return {
            'recordId': self.record_id,
            'userId': self.user_id,
            'bookId': self.book_id,
            'borrowDate': self.borrow_date.isoformat() + 'T00:00:00.000+00:00',
            'dueDate': self.due_date.isoformat() + 'T00:00:00.000+00:00'
        }
