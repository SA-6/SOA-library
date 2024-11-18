import unittest,os,sys
from flask import json
from app import app
import requests
from datetime import datetime
from models.bookinfo import BookInfo

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
    # 测试新增书籍
    def test_add_bookinfo(self):
        json_headers = {'Accept': 'application/json'}
        xml_headers = {'Accept': 'application/xml'}

        # JSON 请求
        response = requests.post('http://127.0.0.1:8080/bookinfo', headers=json_headers, json={
            "book_name": "wyk_test",
            "author": "string",
            "description": "string",
            "image_path": "string",
            "publisher": "string",
            "publisher_time": "2019-08-24",
            "isbn": "string",
            "category": "string",
            "code": "string",
            "price": 9.99,
            "start_time": "2024/9/18",
            "end_time": "2019-08-24T14:15:22.123Z",
            "should_return_date": "2019-08-24T14:15:22.123Z",
            "borrow_status": "string",
            "ebook": "string",
            "search_num": "string"
        })
        assert response.status_code == 200
        assert '书籍已添加' in response.json()['message']
        print_response(response)

        # XML 请求
        response = requests.post('http://127.0.0.1:8080/borrow_records', headers=xml_headers, json={
            "book_name": "wyk_test",
            "author": "string",
            "description": "string",
            "image_path": "string",
            "publisher": "string",
            "publisher_time": "2019-08-24",
            "isbn": "string",
            "category": "string",
            "code": "string",
            "price": 9.99,
            "start_time": "2024/9/18",
            "end_time": "2019-08-24T14:15:22.123Z",
            "should_return_date": "2019-08-24T14:15:22.123Z",
            "borrow_status": "string",
            "ebook": "string",
            "search_num": "string"
        })
        assert response.status_code == 200
        assert '书籍已添加' in response.text
        print_response(response)

        # 验证记录是否已添加到数据库
        with app.app_context():
            book = BookInfo.query.filter_by(book_name='wyk_test').first()
            assert book is not None
            assert book.author == 'string'
            assert book.publisher_time == datetime.strptime('2019-08-24', '%Y-%m-%d').date()
            assert book.isbn == 'string'
            assert book.price == 9.99


    # 测试查询所有书籍信息
    def test_get_all_bookinfo(self):
        json_headers = {'Accept': 'application/json'}
        xml_headers = {'Accept': 'application/xml'}

        # JSON 请求
        response = requests.get('http://127.0.0.1:8080/bookinfo', headers=json_headers)
        assert response.status_code == 200
        assert len(response.json()['data']) > 0
        print_response(response)

        # XML 请求
        response = requests.get('http://127.0.0.1:8080/bookinfo', headers=xml_headers)
        assert response.status_code == 200
        assert '<data>' in response.text
        print_response(response)

    # 测试更新书籍信息
    def test_update_borrow_record(self):
        json_headers = {'Accept': 'application/json'}
        xml_headers = {'Accept': 'application/xml'}

        # JSON 请求
        response = requests.put('http://127.0.0.1:8080/bookinfo', headers=json_headers, json={
            "book_name": "wyk_test",
            "author": "string",
            "description": "string",
            "image_path": "string",
            "publisher": "string",
            "publisher_time": "2020-08-24",
            "isbn": "string",
            "category": "string",
            "code": "string",
            "price": 39.99,
            "start_time": "2024/9/18",
            "end_time": "2019-08-24T14:15:22.123Z",
            "should_return_date": "2019-08-24T14:15:22.123Z",
            "borrow_status": "string",
            "ebook": "string",
            "search_num": "string"
        })
        assert response.status_code == 200
        assert '书籍信息已更新' in response.json()['message']
        print_response(response)

        # XML 请求
        response = requests.put('http://127.0.0.1:8080/bookinfo', headers=xml_headers, json={
            "book_name": "wyk_test",
            "author": "string",
            "description": "string",
            "image_path": "string",
            "publisher": "string",
            "publisher_time": "2018-08-24",
            "isbn": "string",
            "category": "string",
            "code": "string",
            "price": 29.99,
            "start_time": "2024/9/18",
            "end_time": "2019-08-24T14:15:22.123Z",
            "should_return_date": "2019-08-24T14:15:22.123Z",
            "borrow_status": "string",
            "ebook": "string",
            "search_num": "string"
        })
        assert response.status_code == 200
        assert '书籍信息已更新' in response.text
        print_response(response)

        # 验证记录是否已更新
        with app.app_context():
            book = BookInfo.query.filter_by(book_name='wyk_test').first()
            assert book is not None
            assert book.author == 'updated_author'
            assert book.publisher_time == datetime.strptime('2023-11-01', '%Y-%m-%d').date()
            assert book.isbn == 'updated_isbn'
            assert book.price == 19.99

    # 测试删除书籍信息
    def test_delete_bookinfo(self):
        json_headers = {'Accept': 'application/json'}
        xml_headers = {'Accept': 'application/xml'}

        # JSON 请求
        response = requests.delete('http://127.0.0.1:8080/bookinfo', headers=json_headers)
        assert response.status_code == 200
        assert '书籍信息已删除' in response.json()['message']
        print_response(response)

        # XML 请求
        response = requests.delete('http://127.0.0.1:8080/bookinfo', headers=xml_headers)
        assert response.status_code == 200
        assert '书籍信息已删除' in response.text
        print_response(response)

        # 验证书籍是否已删除
        with app.app_context():
            book = BookInfo.query.filter_by(book_name='wyk_test').first()
            assert book is None