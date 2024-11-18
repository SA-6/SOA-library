from flask import Blueprint, request, jsonify
from extensions import db
from models.return_record import ReturnRecord
from utils.commonResponse import CommonResponse

return_records_bp = Blueprint('return_records', __name__)

api_list = {
    "return_records_get-all-url": "http://127.0.0.1:8080/return_records/",
    "return_records_post-url": "http://127.0.0.1:8080/return_records/",
    "return_records_put-url": "http://127.0.0.1:8080/return_records/<string:record_id>"
}

@return_records_bp.route('/api', methods=['GET'])
def get_return_record_api():
    return jsonify(api_list)

@return_records_bp.route('/', methods=['GET'])
def get_all_return_records():
    records = ReturnRecord.query.all()
    result = [record.to_dict() for record in records]
    return CommonResponse.success(data=result)


@return_records_bp.route('/', methods=['POST'])
def add_return_record():
    data = request.json
    new_record = ReturnRecord(
        record_id=data.get('record_id'),
        user_id=data.get('user_id'),
        book_id=data.get('book_id'),
        return_date=data.get('return_date')
    )
    db.session.add(new_record)
    db.session.commit()
    return CommonResponse.success(message="归还记录已添加")


@return_records_bp.route('/<string:record_id>', methods=['PUT'])
def update_return_record(record_id):
    record = ReturnRecord.query.get(record_id)
    if not record:
        return CommonResponse.error(message="未找到该归还记录")
    data = request.json
    record.user_id = data.get('user_id', record.user_id)
    record.book_id = data.get('book_id', record.book_id)
    record.return_date = data.get('return_date', record.return_date)
    db.session.commit()
    return CommonResponse.success(message="归还记录已更新")