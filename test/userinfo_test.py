import unittest,os,sys
from flask import json
from app import app
import requests
from datetime import datetime
from models.bookinfo import BookInfo
from models.userinfo import UserInfo


project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)

# 打印响应内容
def print_response(response):
    print(f"Status Code: {response.status_code}")
    if 'application/json' in response.headers['Content-Type']:
        print("JSON Response:", response.json())
    elif 'application/xml' in response.headers['Content-Type']:
        print("XML Response:", response.text)

class TestApp(unittest.TestCase):
    # 测试新增用户
    def test_add_userinfo(self):
        json_headers = {'Accept': 'application/json'}
        xml_headers = {'Accept': 'application/xml'}

        # JSON 请求
        response = requests.post('http://127.0.0.1:8080/users', headers=json_headers, json={
            "user_id": "user001",
            "password": "abc123",
            "email": "abc123@qq.com",
            "user_type": "Student",
            "prefer_type": "English",
            "balance": 25.5,
            "user_name": "abc",
            "borrow_book_num": 23,
            "search_num": 9,
        })
        # 打印状态码和响应内容，帮助调试
        print("Status Code:", response.status_code)
        print("Response Text:", response.text)
        if response.status_code == 200:
            print("Success:", response.json())
        else:
            print("Error details:", response.json())
        assert response.status_code == 200
        assert '添加成功' in response.json()['message']
        print_response(response)

        # XML 请求
        response = requests.post('http://127.0.0.1:8080/users', headers=xml_headers, json={
            "user_id": "user001",
            "password": "abc123",
            "email": "abc123@qq.com",
            "user_type": "Student",
            "prefer_type": "English",
            "balance": 25.5,
            "user_name": "abc",
            "borrow_book_num": 23,
            "search_num": 9,
        })
        assert response.status_code == 200
        assert '添加成功' in response.text
        print_response(response)

        # 验证记录是否已添加到数据库
        with app.app_context():
            user = UserInfo.query.filter_by(user_id='abc123').first()
            assert user is not None
            assert user.user_name == 'abc'
            assert user.email == 'abc123@qq.com'
            assert user.password == 'abc123'
            assert user.prefer_type == "English"


    # 测试查询所有用户信息
    def test_get_all_userinfo(self):
        json_headers = {'Accept': 'application/json'}
        xml_headers = {'Accept': 'application/xml'}

        # JSON 请求
        response = requests.get('http://127.0.0.1:8080/users', headers=json_headers)
        assert response.status_code == 200
        assert len(response.json()['data']) > 0
        print_response(response)

        # XML 请求
        response = requests.get('http://127.0.0.1:8080/users', headers=xml_headers)
        assert response.status_code == 200
        assert '<data>' in response.text
        print_response(response)

    # 测试通过id查询用户信息
    def test_get_userinfo_by_oid(self):
        json_headers = {'Accept': 'application/json'}
        xml_headers = {'Accept': 'application/xml'}

        # JSON 请求
        response = requests.get('http://127.0.0.1:8080/users/user20', headers=json_headers)
        assert response.status_code == 200
        assert len(response.json()['data']) > 0
        print_response(response)

        # XML 请求
        response = requests.get('http://127.0.0.1:8080/users/user20', headers=xml_headers)
        assert response.status_code == 200
        assert '<data>' in response.text
        print_response(response)

    # 测试更新用户信息
    def test_update_userinfo(self):
        json_headers = {'Accept': 'application/json'}
        xml_headers = {'Accept': 'application/xml'}

        # JSON 请求
        response = requests.put('http://127.0.0.1:8080/users/user20', headers=json_headers, json={
            "password": "abc123",
            "email": "abc123@qq.com",
            "user_type": "Student",
            "prefer_type": "English",
            "balance": 25.5,
            "user_name": "abc",
            "borrow_book_num": 23,
            "search_num": 9,
        })
        assert response.status_code == 200
        assert '修改成功' in response.json()['message']
        print_response(response)

        # XML 请求
        response = requests.put('http://127.0.0.1:8080/users/user20', headers=xml_headers, json={
            "password": "abc123",
            "email": "abc123@qq.com",
            "user_type": "Student",
            "prefer_type": "English",
            "balance": 25.5,
            "user_name": "abc",
            "borrow_book_num": 23,
            "search_num": 9,
        })
        assert response.status_code == 200
        assert '修改成功' in response.text
        print_response(response)

        # 验证记录是否已更新
        with app.app_context():
            user = UserInfo.query.filter_by(user_name='abc').first()
            assert user is not None
            assert user.user_id == 'user20'
            assert user.password == 'abc123'
            assert user.prefer_type == 'English'
            assert user.balance == 25.5

    # 测试删除用户信息
    def test_delete_userinfo(self):
        json_headers = {'Accept': 'application/json'}
        xml_headers = {'Accept': 'application/xml'}

        # JSON 请求
        response = requests.delete('http://127.0.0.1:8080/users/user001', headers=json_headers)
        assert response.status_code == 200
        assert '删除成功' in response.json()['message']
        print_response(response)

        # XML 请求
        response = requests.delete('http://127.0.0.1:8080/users/user001', headers=xml_headers)
        assert response.status_code == 200
        assert '删除成功' in response.text
        print_response(response)

        # 验证用户是否已删除
        with app.app_context():
            user = UserInfo.query.filter_by(user_id='user001').first()
            assert user is None