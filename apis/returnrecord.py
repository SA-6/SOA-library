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

    return_type = request.headers.get('Accept')
    url   = request.url
    links = CommonResponse.create_links(rel='get',resource_name='return_records',request_url=url)

    if result == []:
        if return_type == 'application/json':
            return CommonResponse(links=links).error(message='未找到归还记录').response_to_json()
        elif return_type == 'application/xml':
            return CommonResponse(links=links).error(message='未找到归还记录').response_to_xml()
    else :
        if return_type == 'application/json':
            return CommonResponse(200,message='获取成功',data=result,links=links).response_to_json()
        elif return_type == 'application/xml':
            return CommonResponse(200,message='获取成功',data=result,links=links).response_to_xml()


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

    return_type = request.headers.get('Accept')
    url   = request.url
    links = CommonResponse.create_links(rel='get',resource_name='return_records',request_url=url)

    if return_type == 'application/json':
        return CommonResponse(200,message='归还记录已添加',links=links).response_to_json()
    elif return_type == 'application/xml':
        return CommonResponse(200,message='归还记录已添加',links=links).response_to_xml()

@return_records_bp.route('/<string:record_id>', methods=['PUT'])
def update_return_record(record_id):
    record = ReturnRecord.query.get(record_id)

    return_type = request.headers.get('Accept')
    url   = request.url
    links = CommonResponse.create_links(rel='get',resource_name='return_records',request_url=url)

    if not record:
        if return_type == 'application/json':
            return CommonResponse(links=links).error(message='未找到归还记录').response_to_json()
        elif return_type == 'application/xml':
            return CommonResponse(links=links).error(message='未找到归还记录').response_to_xml()
        
    data = request.json
    record.user_id = data.get('user_id', record.user_id)
    record.book_id = data.get('book_id', record.book_id)
    record.return_date = data.get('return_date', record.return_date)
    db.session.commit()
    
    if return_type == 'application/json':
        return CommonResponse(200,message='归还记录已更新',links=links).response_to_json()
    elif return_type == 'application/xml':
        return CommonResponse(200,message='归还记录已更新',links=links).response_to_xml()