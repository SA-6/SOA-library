# 创建蓝图
from flask import Blueprint, request, jsonify

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

    return_type = request.headers.get('Accept')
    url   = request.url
    links = CommonResponse.create_links(rel='get',resource_name='borrow_records',request_url=url)
    if return_type == 'application/json':
        return CommonResponse(200,message='借阅记录已添加',links=links).response_to_json()
    elif return_type == 'application/xml':
        return CommonResponse(200,message='借阅记录已添加',links=links).response_to_xml()


# 删除借阅记录
@borrow_records_bp.route('/<string:record_id>', methods=['DELETE'])
def delete_borrow_record(record_id):
    record = BorrowRecord.query.get(record_id)

    return_type = request.headers.get('Accept')
    url   = request.url
    links = CommonResponse.create_links(rel='get',resource_name='borrow_records',request_url=url)

    if not record:
        if return_type == 'application/json':
            return CommonResponse(links=links).error(message='未找到借阅记录').response_to_json()
        elif return_type == 'application/xml':
            return CommonResponse(links=links).error(message='未找到借阅记录').response_to_xml()
    db.session.delete(record)
    db.session.commit()
    
    
    if return_type == 'application/json':
        return CommonResponse(200,message='借阅记录已删除',links=links).response_to_json()
    elif return_type == 'application/xml':
        return CommonResponse(200,message='借阅记录已删除',links=links).response_to_xml()


# 查询所有借阅记录
@borrow_records_bp.route('/', methods=['GET'])
def get_all_borrow_records():
    records = BorrowRecord.query.all()
    print(records)
    result = [record.to_dict() for record in records]
    
    return_type = request.headers.get('Accept')
    url   = request.url
    links = CommonResponse.create_links(rel='get',resource_name='borrow_records',request_url=url)

    if return_type == 'application/json':
        return CommonResponse(200,message='获取成功',data=result,links=links).response_to_json()
    elif return_type == 'application/xml':
        return CommonResponse(200,message='获取成功',data=result,links=links).response_to_xml()


# 更新借阅记录
@borrow_records_bp.route('/<string:record_id>', methods=['PUT'])
def update_borrow_record(record_id):
    record = BorrowRecord.query.get(record_id)

    return_type = request.headers.get('Accept')
    url   = request.url
    links = CommonResponse.create_links(rel='get',resource_name='borrow_records',request_url=url)

    if not record:
        if return_type == 'application/json':
            return CommonResponse(links=links).error(message='未找到借阅记录').response_to_json()
        elif return_type == 'application/xml':
            return CommonResponse(links=links).error(message='未找到借阅记录').response_to_xml()
    data = request.json
    record.user_id = data.get('user_id', record.user_id)
    record.book_id = data.get('book_id', record.book_id)
    record.borrow_date = data.get('borrow_date', record.borrow_date)
    record.due_date = data.get('due_date', record.due_date)
    db.session.commit()

    
    if return_type == 'application/json':
        return CommonResponse(200,message='借阅记录已更新',links=links).response_to_json()
    elif return_type == 'application/xml':
        return CommonResponse(200,message='借阅记录已更新',links=links).response_to_xml()
