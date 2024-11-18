from DAO.bookinfoDao import BookinfoDao
from datetime import datetime
from decimal import Decimal
from models.bookinfo import BookInfo

class BookinfoService:

    @staticmethod
    def getAllBookinfo():
        books = BookinfoDao.queryAllBookinfo()
        all_book_info = []
        for book in books:
            all_book_info.append(BookinfoService.bookinfoToDict(book))
        return all_book_info
    
    @staticmethod
    def addNewBookinfo(bookinfo_dict):
        bookinfo = BookinfoService.bookinfoFromDict(bookinfo_dict)
        return BookinfoService.bookinfoToDict(BookinfoDao.addNewBookinfo(bookinfo))
    
    @staticmethod
    def updateBookinfo(bookinfo_dict):
        bookinfo = BookinfoService.bookinfoFromDict(bookinfo_dict)
        return BookinfoService.bookinfoToDict(BookinfoDao.updateBookinfo(bookinfo))
    
    @staticmethod
    def deleteBookinfo(book_id):
        return BookinfoService.bookinfoToDict(BookinfoDao.deleteBookinfo(book_id))
    
    @staticmethod
    def getBookinfoById(book_id):
        return BookinfoService.bookinfoToDict(BookinfoDao.getBookinfoById(book_id))

    @staticmethod
    def bookinfoToDict(bookinfo):
        return {
            'book_id': bookinfo.book_id,
            'book_name': bookinfo.book_name,
            'author': bookinfo.author,
            'description': bookinfo.description,
            'image_path': bookinfo.image_path,
            'publisher': bookinfo.publisher,
            'publisher_time': bookinfo.publisher_time.strftime('%Y-%m-%d %H:%M:%S') if bookinfo.publisher_time else None,
            'isbn': bookinfo.isbn,
            'category': bookinfo.category,
            'code': bookinfo.code,
            'price': float(bookinfo.price) if bookinfo.price is not None else None,
            'start_time': bookinfo.start_time.strftime('%Y-%m-%d %H:%M:%S') if bookinfo.start_time else None,
            'end_time': bookinfo.end_time.strftime('%Y-%m-%d %H:%M:%S') if bookinfo.end_time else None,
            'should_return_date': bookinfo.should_return_date.strftime('%Y-%m-%d %H:%M:%S') if bookinfo.should_return_date else None,
            'borrow_status': bookinfo.borrow_status,
            'ebook': bookinfo.ebook,
            'search_num': int(bookinfo.search_num) if bookinfo.search_num is not None else None
        }
    
    @staticmethod
    def bookinfoFromDict(data):
        book_id = data.get('book_id')
        book_name = data.get('book_name')
        author = data.get('author')
        description = data.get('description')
        image_path = data.get('image_path')
        publisher = data.get('publisher')
        publisher_time = data.get('publisher_time')
        isbn = data.get('isbn')
        category = data.get('category')
        code = data.get('code')
        price = Decimal(data.get('price')) if data.get('price') is not None else None
        start_time = data.get('start_time')
        end_time = data.get('end_time')
        should_return_date = data.get('should_return_date')
        borrow_status = bool(data.get('borrow_status'))
        ebook = bool(data.get('ebook'))
        search_num = int(data.get('search_num')) if data.get('search_num') is not None else 0


        print(publisher_time)
        # 将字符串日期时间转换为 datetime 对象
        if publisher_time:
            publisher_time = datetime.strptime(publisher_time, '%Y-%m-%d')
        if start_time:
            start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
        if end_time:
            end_time = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
        if should_return_date:
            should_return_date = datetime.strptime(should_return_date, '%Y-%m-%d')

        # 创建 BookInfo 对象
        bookinfo = BookInfo(
            book_id=book_id,
            book_name=book_name,
            author=author,
            description=description,
            image_path=image_path,
            publisher=publisher,
            publisher_time=publisher_time,
            isbn=isbn,
            category=category,
            code=code,
            price=price,
            start_time=start_time,
            end_time=end_time,
            should_return_date=should_return_date,
            borrow_status=borrow_status,
            ebook=ebook,
            search_num=search_num
        )

        return bookinfo
    
