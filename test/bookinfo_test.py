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
            "book_id" : 10190,
            "book_name": "测试",
            "author": "eu",
            "price": "90",
            "description": "约一存力并类还强原心间支较确标。志土由务声共越持始志等积近别集级。能果话之好道市术七候根对。济集想活济战六调引技及业期。及集去律期北看别其由中论育电。",
            "image_path": "http://dummyimage.com/400x400",
            "publisher": "sint ut aute",
            "publisher_time": "1989-09-12",
            "isbn": "10000054",
            "category": "ipsum Lorem ut",
            "code": "44",
            "start_time": "2012-07-09 02:50:31",
            "end_time": "1972-05-14 11:43:45",
            "should_return_date": "1990-04-15",
            "borrow_status": "elit",
            "ebook": "consequat in",
            "search_num": "50"
        })
        assert response.status_code == 200
        assert '书籍已添加' in response.json()['message']
        print_response(response)

        # XML 请求
        response = requests.post('http://127.0.0.1:8080/bookinfo', headers=xml_headers, json={
            "book_id" : 10116,
            "book_name": "csh_test",
            "author": "csh",
            "price": "90",
            "description": "约一存力并类还强原心间支较确标。志土由务声共越持始志等积近别集级。能果话之好道市术七候根对。济集想活济战六调引技及业期。及集去律期北看别其由中论育电。",
            "image_path": "http://dummyimage.com/400x400",
            "publisher": "sint ut aute",
            "publisher_time": "1989-09-12",
            "isbn": "10000054",
            "category": "ipsum Lorem ut",
            "code": "44",
            "start_time": "2012-07-09 02:50:31",
            "end_time": "1972-05-14 11:43:45",
            "should_return_date": "1990-04-15",
            "borrow_status": "elit",
            "ebook": "consequat in",
            "search_num": "50"
        })
        assert response.status_code == 200
        assert '书籍已添加' in response.text
        print_response(response)

        # 验证记录是否已添加到数据库
        with app.app_context():
            book = BookInfo.query.filter_by(book_name='csh_test').first()
            assert book is not None
            assert book.author == 'csh'
            assert book.publisher_time == datetime.strptime('1989-09-12', '%Y-%m-%d').date()
            assert book.isbn == '10000054'
            assert book.price == 90


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

    # 测试通过id查询书籍信息
    def test_get_bookinfo_by_id(self):
        json_headers = {'Accept': 'application/json'}
        xml_headers = {'Accept': 'application/xml'}

        # JSON 请求
        response = requests.get('http://127.0.0.1:8080/bookinfo/10001', headers=json_headers)
        assert response.status_code == 200
        assert len(response.json()['data']) > 0
        print_response(response)

        # XML 请求
        response = requests.get('http://127.0.0.1:8080/bookinfo/10001', headers=xml_headers)
        assert response.status_code == 200
        assert '<data>' in response.text
        print_response(response)

    # 测试更新书籍信息
    def test_update_bookinfo(self):
        json_headers = {'Accept': 'application/json'}
        xml_headers = {'Accept': 'application/xml'}

        # JSON 请求
        response = requests.put('http://127.0.0.1:8080/bookinfo', headers=json_headers, json={
            "book_id"  : 10190,
            "book_name": "wyk_test",
            "author": "updated_author",
            "description": "string",
            "image_path": "string",
            "publisher": "string",
            "publisher_time": "2020-08-24",
            "isbn": "updated_isbn",
            "category": "string",
            "code": "string",
            "price": 39.99,
            "start_time": "2012-07-09 02:50:31",
            "end_time": "2019-08-24 14:15:22",
            "should_return_date": "2019-08-24",
            "borrow_status": "string",
            "ebook": "string",
            "search_num": 50
        })
        assert response.status_code == 200
        assert '书籍信息修改成功' in response.json()['message']
        print_response(response)

        # XML 请求
        response = requests.put('http://127.0.0.1:8080/bookinfo', headers=xml_headers, json={
            "book_id"  : 10190,
            "book_name": "wyk_test",
            "author": "updated_author",
            "description": "string",
            "image_path": "string",
            "publisher": "string",
            "publisher_time": "2020-08-24",
            "isbn": "updated_isbn",
            "category": "string",
            "code": "string",
            "price": 39.99,
            "start_time": "2012-07-09 02:50:31",
            "end_time": "2019-08-24 14:15:22",
            "should_return_date": "2019-08-24",
            "borrow_status": "string",
            "ebook": "string",
            "search_num": 50
        })
        assert response.status_code == 200
        assert '书籍信息修改成功' in response.text
        print_response(response)

        # 验证记录是否已更新
        with app.app_context():
            book = BookInfo.query.filter_by(book_name='wyk_test').first()
            assert book is not None
            assert book.author == 'updated_author'
            assert book.publisher_time == datetime.strptime('2020-08-24', '%Y-%m-%d').date()
            assert book.isbn == 'updated_isbn'
            assert book.price == 39.99

    # 测试删除书籍信息
    def test_delete_bookinfo(self):
        json_headers = {'Accept': 'application/json'}
        xml_headers = {'Accept': 'application/xml'}

        # JSON 请求
        response = requests.delete('http://127.0.0.1:8080/bookinfo/10190', headers=json_headers)
        assert response.status_code == 200
        assert '书籍信息删除成功' in response.json()['message']
        print_response(response)

        # XML 请求
        response = requests.delete('http://127.0.0.1:8080/bookinfo/10116', headers=xml_headers)
        assert response.status_code == 200
        assert '书籍信息删除成功' in response.text
        print_response(response)

        # 验证书籍是否已删除
        with app.app_context():
            book = BookInfo.query.filter_by(book_name='wyk_test').first()
            assert book is None