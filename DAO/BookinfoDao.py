from extensions import db
from models.bookinfo import BookInfo

class BookinfoDao:
    @staticmethod
    def queryAllBookinfo():
        allBookinfo = BookInfo.query.all()
        return allBookinfo
    
    @staticmethod
    def getBookinfoById(book_id):
        book = BookInfo.query.filter(BookInfo.book_id == book_id).first()
        return book

    @staticmethod
    def addNewBookinfo(bookinfo):
        db.session.add(bookinfo)
        db.session.commit()
        return bookinfo
    
    @staticmethod
    def updateBookinfo(bookinfo):
        BookInfo.query.filter(bookinfo.book_id == BookInfo.book_id).update({
            BookInfo.book_name          : bookinfo.book_name,
            BookInfo.author             : bookinfo.author,
            BookInfo.description        : bookinfo.description,
            BookInfo.image_path         : bookinfo.image_path,
            BookInfo.publisher          : bookinfo.publisher,
            BookInfo.publisher_time     : bookinfo.publisher_time,
            BookInfo.isbn               : bookinfo.isbn,
            BookInfo.category           : bookinfo.category,
            BookInfo.code               : bookinfo.code,
            BookInfo.price              : bookinfo.price,
            BookInfo.start_time         : bookinfo.start_time,
            BookInfo.end_time           : bookinfo.end_time,
            BookInfo.should_return_date : bookinfo.should_return_date,
            BookInfo.borrow_status      : bookinfo.borrow_status,
            BookInfo.ebook              : bookinfo.ebook,
            BookInfo.search_num         : bookinfo.search_num
        })
        db.session.commit()
        return bookinfo
    
    @staticmethod
    def deleteBookinfo(book_id):
        bookinfo = BookInfo.query.filter(BookInfo.book_id == book_id).first()
        db.session.delete(bookinfo)
        db.session.commit()
        return bookinfo