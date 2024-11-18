from flask import jsonify, Response
from dicttoxml import dicttoxml


class CommonResponse:
    def __init__(self) -> None:
        pass

    @staticmethod
    def success(status=200, message="请求成功", data=None):
        response = {
            'status': status,
            'message': message,
            'data': data
        }
        return jsonify(response)

    @staticmethod
    def error(status=400, message="请求失败", data=None):
        response = {
            'status': status,
            'message': message,
            'data': data
        }
        return jsonify(response)

    @staticmethod
    def success_xml(status=200, message="请求成功", data=None, media=None):
        response = {
            'status': status,
            'message': message,
            'data': data,
            'hypermedia': media
        }
        xml_response = dicttoxml(response, custom_root='response', attr_type=False)
        return Response(xml_response, mimetype='application/xml')

    @staticmethod
    def error_xml(status=400, message="请求失败", data=None, media=None):
        response = {
            'status': status,
            'message': message,
            'data': data,
            'hypermedia': media
        }
        xml_response = dicttoxml(response, custom_root='response', attr_type=False)
        return Response(xml_response, mimetype='application/xml')
