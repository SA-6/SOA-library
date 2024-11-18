from flask import Blueprint,request
from flask import jsonify,Response
from dicttoxml import dicttoxml
from utils.commonResponse import CommonResponse
from service.BookinfoService import BookinfoService


bookinfo_bp = Blueprint(name='bookinfo_bp',import_name=__name__,url_prefix='/')

# 查询部分
@bookinfo_bp.route('bookinfo',methods=['get'])
def query_all():
    bookinfo_list = BookinfoService.getAllBookinfo()
    url   = request.url
    links = CommonResponse.create_links(rel='get',resource_name='bookinfo',request_url=url)
    accept_header = request.headers.get('Accept', 'application/json')
    if 'application/json' in accept_header:
        return CommonResponse(200,message='获取成功',data=bookinfo_list,links=links).response_to_json()
    elif 'application/xml' in accept_header:
        return CommonResponse(200,message='获取成功',data=bookinfo_list,links=links).response_to_xml()

@bookinfo_bp.route('bookinfo/<int:book_id>',methods=['get'])
def query_by_id(book_id):
    bookinfo = BookinfoService.getBookinfoById(book_id)
    url   = request.url
    links = CommonResponse.create_links(rel='get',resource_name='bookinfo',request_url=url)
    accept_header = request.headers.get('Accept', 'application/json')
    if 'application/json' in accept_header:
        return CommonResponse(200,message='获取成功',data=bookinfo,links=links).response_to_json()
    elif 'application/xml' in accept_header:
        return CommonResponse(200,message='获取成功',data=bookinfo,links=links).response_to_xml()
    
# 新增数据部分
@bookinfo_bp.route('bookinfo',methods=['post'])
def add_bookinfo():
    return_type = request.headers.get('Accept')
    bookinfo_dict = request.get_json()
    bookinfo = BookinfoService.addNewBookinfo(bookinfo_dict)
    url   = request.url
    links = CommonResponse.create_links(rel='get',resource_name='bookinfo',request_url=url)

    if return_type == 'application/json':
        return CommonResponse(200,message='获取成功',data=bookinfo,links=links).response_to_json()
    elif return_type == 'application/xml':
        return CommonResponse(200,message='获取成功',data=bookinfo,links=links).response_to_xml()
    
# 修改数据部分
@bookinfo_bp.route('bookinfo',methods=['put'])
def update_bookinfo():
    return_type = request.headers.get('Accept')
    bookinfo_dict = request.get_json()
    bookinfo = BookinfoService.updateBookinfo(bookinfo_dict)

    url   = request.url
    links = CommonResponse.create_links(rel='get',resource_name='bookinfo',request_url=url)
    if return_type == 'application/json':
        return CommonResponse(200,message='获取成功',data=bookinfo,links=links).response_to_json()
    elif return_type == 'application/xml':
        return CommonResponse(200,message='获取成功',data=bookinfo,links=links).response_to_xml()
    
# 删除数据部分
@bookinfo_bp.route('bookinfo/<book_id>',methods=['delete'])
def delete_bookinfo(book_id):
    return_type = request.headers.get('Accept')
    bookinfo = BookinfoService.deleteBookinfo(book_id)

    url   = request.url
    links = CommonResponse.create_links(rel='get',resource_name='bookinfo',request_url=url)
    if return_type == 'application/json':
        return CommonResponse(200,message='获取成功',data=bookinfo,links=links).response_to_json()
    elif return_type == 'application/xml':
        return CommonResponse(200,message='获取成功',data=bookinfo,links=links).response_to_xml()
