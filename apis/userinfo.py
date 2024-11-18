from flask import Blueprint,request
from utils.commonResponse import CommonResponse
from service.userServices import UserinfoService

userinfo_bp = Blueprint(name='userinfo_bp',import_name=__name__,url_prefix='/')


# 查询部分
# 查询所有用户信息
@userinfo_bp.route('users',methods=['get'])
def query_all():
    return_type = request.headers.get('Accept')
    userinfo_list = UserinfoService.getAllUserinfo()
    url   = request.url
    links = CommonResponse.create_links(rel='get',resource_name='userinfo',request_url=url)

    if return_type == 'application/json':
        return CommonResponse(200,message='获取成功',data=userinfo_list,links=links).response_to_json()
    elif return_type == 'application/xml':
        return CommonResponse(200,message='获取成功',data=userinfo_list,links=links).response_to_xml()

# 查询单个用户的信息
@userinfo_bp.route('users/<user_id>',methods=['get'])
def query_user(user_id):
    return_type = request.headers.get('Accept')
    userinfo = UserinfoService.getUserById(user_id)
    url   = request.url
    links = CommonResponse.create_links(rel='get',resource_name='userinfo',request_url=url)

    if return_type == 'application/json':
        return CommonResponse(200,message='获取成功',data=userinfo,links=links).response_to_json()
    elif return_type == 'application/xml':
        return CommonResponse(200,message='获取成功',data=userinfo,links=links).response_to_xml()

# 新增数据部分
@userinfo_bp.route('users',methods=['post'])
def add_userinfo():
    return_type = request.headers.get('Accept')
    
    userinfo_dict = request.get_json()
    userinfo = UserinfoService.addNewUserinfo(userinfo_dict)
    url   = request.url
    links = CommonResponse.create_links(rel='get',resource_name='userinfo',request_url=url)

    if return_type == 'application/json':
        return CommonResponse(200,message='获取成功',data=userinfo,links=links).response_to_json()
    elif return_type == 'application/xml':
        return CommonResponse(200,message='获取成功',data=userinfo,links=links).response_to_xml()
    
# 修改数据部分
@userinfo_bp.route('users/<user_id>',methods=['put'])
def update_userinfo(user_id):
    return_type = request.headers.get('Accept')
    
    userinfo_dict = request.get_json()
    userinfo_dict['user_id'] = user_id
    userinfo = UserinfoService.updateUserinfo(userinfo_dict)
    url   = request.url
    links = CommonResponse.create_links(rel='get',resource_name='userinfo',request_url=url)

    if return_type == 'application/json':
        return CommonResponse(200,message='获取成功',data=userinfo,links=links).response_to_json()
    elif return_type == 'application/xml':
        return CommonResponse(200,message='获取成功',data=userinfo,links=links).response_to_xml()
    
# 删除数据部分
@userinfo_bp.route('users/<user_id>',methods=['delete']) 
def delete_userinfo(user_id):
    return_type = request.headers.get('Accept')
    userinfo = UserinfoService.deleteUserinfo(user_id)
    url   = request.url
    links = CommonResponse.create_links(rel='get',resource_name='userinfo',request_url=url)

    if return_type == 'application/json':
        return CommonResponse(200,message='获取成功',data=userinfo,links=links).response_to_json()
    elif return_type == 'application/xml':
        return CommonResponse(200,message='获取成功',data=userinfo,links=links).response_to_xml()