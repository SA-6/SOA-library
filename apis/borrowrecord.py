# 创建蓝图
from flask import Blueprint, request

from extensions import db
from models.borrow_record import BorrowRecord
from utils.commonResponse import CommonResponse

borrow_records_bp = Blueprint('borrow_records', __name__)


# 新增一条借阅记录
@borrow_records_bp.route('/', methods=['POST'])
def add_borrow_record():
    data = request.json
    new_record = BorrowRecord(
        record_id=data.get('record_id'),
        user_id=data.get('user_id'),
        book_id=data.get('book_id'),
        borrow_date=data.get('borrow_date'),
        due_date=data.get('due_date')
    )
    db.session.add(new_record)
    db.session.commit()
    return CommonResponse.success(message="借阅记录已添加")


# 删除借阅记录
@borrow_records_bp.route('/<string:record_id>', methods=['DELETE'])
def delete_borrow_record(record_id):
    record = BorrowRecord.query.get(record_id)
    if not record:
        return CommonResponse.error(message="未找到该借阅记录")
    db.session.delete(record)
    db.session.commit()
    return CommonResponse.success(message="借阅记录已删除")


# 查询所有借阅记录
@borrow_records_bp.route('/', methods=['GET'])
def get_all_borrow_records():
    records = BorrowRecord.query.all()
    result = [r.__dict__ for r in records]
    for r in result:
        del r['_sa_instance_state']
    return CommonResponse.success(data=result)


# 更新借阅记录
@borrow_records_bp.route('/<string:record_id>', methods=['PUT'])
def update_borrow_record(record_id):
    record = BorrowRecord.query.get(record_id)
    if not record:
        return CommonResponse.error(message="未找到该借阅记录")
    data = request.json
    record.user_id = data.get('user_id', record.user_id)
    record.book_id = data.get('book_id', record.book_id)
    record.borrow_date = data.get('borrow_date', record.borrow_date)
    record.due_date = data.get('due_date', record.due_date)
    db.session.commit()
    return CommonResponse.success(message="借阅记录已更新")
