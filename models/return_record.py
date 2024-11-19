from extensions import db

class ReturnRecord(db.Model):
    __tablename__ = 'return_record'
    record_id = db.Column(db.String(10), primary_key=True)
    user_id = db.Column(db.String(10), db.ForeignKey('userinfo.user_id'))
    book_id = db.Column(db.String(10), db.ForeignKey('bookinfo.book_id'))
    return_date = db.Column(db.Date())
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
            'returnDate': self.return_date.isoformat() + 'T00:00:00.000+00:00'
        }