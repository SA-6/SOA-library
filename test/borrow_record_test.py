import unittest,os,sys
from flask import json
from app import app
import requests
from datetime import datetime
from models.borrow_record import BorrowRecord

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
    # 测试新增借阅记录
    def test_add_borrow_record(self):
        json_headers = {'Accept': 'application/json'}
        xml_headers = {'Accept': 'application/xml'}

        # JSON 请求
        response = requests.post('http://127.0.0.1:8080/borrow_records', headers=json_headers, json={
            'record_id': '1',
            'user_id': '8209220223',
            'book_id': '10007',
            'borrow_date': '2023-10-01',
            'due_date': '2023-10-31'
        })
        assert response.status_code == 200
        assert '借阅记录已添加' in response.json()['message']
        print_response(response)

        # XML 请求
        response = requests.post('http://127.0.0.1:8080/borrow_records', headers=xml_headers, json={
            'record_id': '2',
            'user_id': '8209220223',
            'book_id': '10008',
            'borrow_date': '2023-10-01',
            'due_date': '2023-10-31'
        })
        assert response.status_code == 200
        assert '借阅记录已添加' in response.text
        print_response(response)

        # 验证记录是否已添加到数据库
        with app.app_context():
            record = BorrowRecord.query.get('1')
            assert record is not None
            assert record.user_id == '8209220223'
            assert record.book_id == '10007'
            assert record.borrow_date == datetime.strptime('2023-10-01', '%Y-%m-%d').date()
            assert record.due_date == datetime.strptime('2023-10-31', '%Y-%m-%d').date()
            record1 = BorrowRecord.query.get('2')
            assert record1 is not None
            assert record1.user_id == '8209220223'
            assert record1.book_id == '10008'
            assert record1.borrow_date == datetime.strptime('2023-10-01', '%Y-%m-%d').date()
            assert record1.due_date == datetime.strptime('2023-10-31', '%Y-%m-%d').date()


    # 测试查询所有借阅记录
    def test_get_all_borrow_records(self):
        json_headers = {'Accept': 'application/json'}
        xml_headers = {'Accept': 'application/xml'}

        # JSON 请求
        response = requests.get('http://127.0.0.1:8080/borrow_records', headers=json_headers)
        assert response.status_code == 200
        assert len(response.json()['data']) > 0
        print_response(response)

        # XML 请求
        response = requests.get('http://127.0.0.1:8080/borrow_records', headers=xml_headers)
        assert response.status_code == 200
        assert '<data>' in response.text
        print_response(response)

    # 测试更新借阅记录
    def test_update_borrow_record(self):
        json_headers = {'Accept': 'application/json'}
        xml_headers = {'Accept': 'application/xml'}

        # JSON 请求
        response = requests.put('http://127.0.0.1:8080/borrow_records/1', headers=json_headers, json={
            'user_id': '8209220223',
            'book_id': '10007',
            'borrow_date': '2023-11-01',
            'due_date': '2023-11-30'
        })
        assert response.status_code == 200
        assert '借阅记录已更新' in response.json()['message']
        print_response(response)

        # XML 请求
        response = requests.put('http://127.0.0.1:8080/borrow_records/2', headers=xml_headers, json={
            'user_id': '8209220223',
            'book_id': '10008',
            'borrow_date': '2023-11-01',
            'due_date': '2023-11-28'
        })
        assert response.status_code == 200
        assert '借阅记录已更新' in response.text
        print_response(response)

        # 验证记录是否已更新
        with app.app_context():
            record = BorrowRecord.query.get('1')
            assert record is not None
            assert record.user_id == '8209220223'
            assert record.book_id == '10007'
            assert record.borrow_date == datetime.strptime('2023-11-01', '%Y-%m-%d').date()
            assert record.due_date == datetime.strptime('2023-11-30', '%Y-%m-%d').date()
            record1 = BorrowRecord.query.get('2')
            assert record1 is not None
            assert record1.user_id == '8209220223'
            assert record1.book_id == '10008'
            assert record1.borrow_date == datetime.strptime('2023-11-01', '%Y-%m-%d').date()
            assert record1.due_date == datetime.strptime('2023-11-28', '%Y-%m-%d').date()

    # 测试删除借阅记录
    def test_delete_borrow_record(self):
        json_headers = {'Accept': 'application/json'}
        xml_headers = {'Accept': 'application/xml'}

        # JSON 请求
        response = requests.delete('http://127.0.0.1:8080/borrow_records/1', headers=json_headers)
        assert response.status_code == 200
        assert '借阅记录已删除' in response.json()['message']
        print_response(response)

        # XML 请求
        response = requests.delete('http://127.0.0.1:8080/borrow_records/2', headers=xml_headers)
        assert response.status_code == 200
        assert '借阅记录已删除' in response.text
        print_response(response)

        # 验证记录是否已删除
        with app.app_context():
            record = BorrowRecord.query.get('1')
            assert record is None
            record = BorrowRecord.query.get('2')
            assert record is None