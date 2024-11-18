from flask import jsonify, Response, request
from dicttoxml import dicttoxml


class CommonResponse:
    @staticmethod
    def success(status=200, message="请求成功", data=None):
        response = {
            'status': status,
            'message': message,
            'data': data
        }
        accept_header = request.headers.get('Accept', '')
        if 'application/json' in accept_header:
            return jsonify(response)
        elif 'application/xml' in accept_header:
            xml_response = dicttoxml(response, custom_root='response', attr_type=False)
            return Response(xml_response, mimetype='application/xml')
        else:
            return jsonify(response)

    @staticmethod
    def error(status=400, message="请求失败", data=None):
        response = {
            'status': status,
            'message': message,
            'data': data
        }
        accept_header = request.headers.get('Accept', '')
        if 'application/json' in accept_header:
            return jsonify(response)
        elif 'application/xml' in accept_header:
            xml_response = dicttoxml(response, custom_root='response', attr_type=False)
            return Response(xml_response, mimetype='application/xml')
        else:
            return jsonify(response)
