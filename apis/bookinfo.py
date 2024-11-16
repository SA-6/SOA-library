from flask import Blueprint,request
from utils.commonResponse import CommonRresponse
from service.BookinfoService import BookinfoService

bookinfo_bp = Blueprint(name='bookinfo_bp',import_name=__name__,url_prefix='/')


# 查询部分
@bookinfo_bp.route('bookinfo',methods=['get'])
def query_all():
    return_type = request.args.get('return_type')
    bookinfo_list = BookinfoService.getAllBookinfo()
    if return_type == 'JSON':
        return CommonRresponse.success(message='获取成功', data=bookinfo_list)
    elif return_type == 'XML':
        return CommonRresponse.success_xml(message='获取成功', data=bookinfo_list)
    
# 新增数据部分
@bookinfo_bp.route('bookinfo',methods=['post'])
def add_bookinfo():
    return_type = request.args.get('return_type')
    bookinfo_dict = request.get_json()
    bookinfo = BookinfoService.addNewBookinfo(bookinfo_dict)
    if return_type == 'JSON':
        return CommonRresponse.success(message='添加成功', data=bookinfo)
    elif return_type == 'XML':
        return CommonRresponse.success_xml(message='添加成功', data=bookinfo)
    
# 修改数据部分
@bookinfo_bp.route('bookinfo',methods=['put'])
def update_bookinfo():
    return_type = request.args.get('return_type')
    bookinfo_dict = request.get_json()
    bookinfo = BookinfoService.updateBookinfo(bookinfo_dict)
    if return_type == 'JSON':
        return CommonRresponse.success(message='修改成功', data=bookinfo)
    elif return_type == 'XML':
        return CommonRresponse.success_xml(message='修改成功', data=bookinfo)
    
# 删除数据部分
@bookinfo_bp.route('bookinfo/<book_id>',methods=['delete'])
def delete_bookinfo(book_id):
    return_type = request.args.get('return_type')
    bookinfo = BookinfoService.deleteBookinfo(book_id)
    if return_type == 'JSON':
        return CommonRresponse.success(message='删除成功', data=bookinfo)
    elif return_type == 'XML':
        return CommonRresponse.success_xml(message='删除成功', data=bookinfo)
