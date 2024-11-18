from DAO.userDAO import userDAO
from datetime import datetime
from decimal import Decimal
from models.userinfo import UserInfo

class UserinfoService:

    @staticmethod
    def getAllUserinfo():
        users = userDAO.getAllUsers()
        all_user_info = []
        for user in users:
            all_user_info.append(UserinfoService.userinfoToDict(user))
        return all_user_info
    
    @staticmethod
    def getUserById(userId):
        user = userDAO.getUserInfoByUserId(userId)
        return UserinfoService.userinfoToDict(user)

    @staticmethod
    def addNewUserinfo(userinfo_dict):
        userinfo = UserinfoService.userinfoFromDict(userinfo_dict)
        return UserinfoService.userinfoToDict(userDAO.newUser(userinfo))
    
    @staticmethod
    def updateUserinfo(userinfo_dict):
        userinfo = UserinfoService.userinfoFromDict(userinfo_dict)
        return UserinfoService.userinfoToDict(userDAO.updateUserInfoByUserId(userinfo))
    
    @staticmethod
    def deleteUserinfo(user_id):
        return UserinfoService.userinfoToDict(userDAO.deleteUserInfoByUserId(user_id))
    
    @staticmethod
    def userinfoToDict(userinfo):
        return {
            'user_id': userinfo.user_id,
            'user_name': userinfo.user_name,
            'password': userinfo.password,
            'email': userinfo.email,
            'user_type': userinfo.user_type,
            'last_login_time':userinfo.last_login_time,
            'prefer_type':userinfo.prefer_type,
            'balance':userinfo.balance,
            'borrow_book_num':userinfo.borrow_book_num,
            'search_num':userinfo.search_num
        }
    
    @staticmethod
    def userinfoFromDict(data):
        user_id = data.get('user_id')
        user_name = data.get('user_name')
        password = data.get('password')
        email = data.get('email')
        user_type = data.get('user_type')
        last_login_time = data.get('last_login_time') if data.get('last_login_type') is not None else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        prefer_type = data.get('prefer_type')
        balance = float(data.get('balance')) if data.get('balance') is not None else 0
        borrow_book_num = int(data.get('borrow_book_num')) if data.get('borrow_book_num') is not None else 0
        search_num = int(data.get('search_num')) if data.get('search_num') is not None else 0


        print(last_login_time)
        # 将字符串日期时间转换为 datetime 对象
        if last_login_time:
            last_login_time = datetime.strptime(last_login_time, '%Y-%m-%d %H:%M:%S')

        # 创建 UserInfo 对象
        userinfo = UserInfo(
            user_id=user_id,
            user_name=user_name,
            password=password,
            email=email,
            user_type=user_type,
            last_login_time=last_login_time,
            prefer_type=prefer_type,
            balance=balance,
            borrow_book_num=borrow_book_num,
            search_num=search_num
        )

        return userinfo