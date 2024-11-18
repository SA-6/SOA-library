from flask import jsonify, Response, request
from dicttoxml import dicttoxml
from ripozo import ResourceBase


# 定义资源
class CommonResponse(ResourceBase):
    pks = ('id',)  # 主键字段

    def __init__(self, status=200, message="请求成功", data=None, links=None, **kwargs):
        super(CommonResponse, self).__init__(**kwargs)
        self.status = status
        self.message = message
        self.data = data if data is not None else {}
        self.links = links or []

    def to_restful(self):
        # 构建响应体
        response_body = {
            'status': self.status,
            'message': self.message,
            'data': self.data
        }
        
        # 添加超链接到响应体
        for link in self.links:
            response_body['links'] = response_body.get('links', [])
            response_body['links'].append({
                'rel': link['rel'],
                'href': link['href'],
                'method': link['method']
            })

        return response_body

    @staticmethod
    def success(status=200, message="请求成功", data=None, links=None):
        return CommonResponse(status=status, message=message, data=data, links=links)

    @staticmethod
    def error(status=400, message="请求失败", data=None, links=None):
        return CommonResponse(status=status, message=message, data=data, links=links)

    def response_to_json(self):
        return jsonify(self.to_restful())

    def response_to_xml(self):
        response_body = self.to_restful()
        xml_response = dicttoxml(response_body, custom_root='response', attr_type=False)
        return Response(xml_response, mimetype='application/xml')

    @staticmethod
    def create_links(rel, resource_name, request_url):
        return [
            {"rel": 'self' if rel == 'get'    else f"get_{resource_name}", "href": request_url, 'method': "GET"},
            {"rel": 'self' if rel == 'post'   else f"create_{resource_name}", "href": request_url, 'method': "POST"},
            {"rel": 'self' if rel == 'put'    else f"update_{resource_name}", "href": request_url, 'method': "PUT"},
            {"rel": 'self' if rel == 'delete' else f"delete_{resource_name}", "href": request_url, 'method': "DELETE"},
        ]
