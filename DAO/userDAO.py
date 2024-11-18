from models.userinfo import UserInfo
from extensions import db

class userDAO:
  # 创建新用户
  @staticmethod
  def newUser(userInfo):
    db.session.add(userInfo)
    db.session.commit()
    return userInfo

  # 获取所有用户信息
  @staticmethod
  def getAllUsers():
    allUserInfo = UserInfo.query.all()
    return allUserInfo

  # 获取指定用户信息
  @staticmethod
  def getUserInfoByUserId(userId):
    userInfo = UserInfo.query.filter(UserInfo.user_id ==userId).first()
    return userInfo

  # 删除指定用户信息
  @staticmethod
  def deleteUserInfoByUserId(userId):
    userInfo = UserInfo.query.filter(UserInfo.user_id ==userId).first()
    db.session.delete(userInfo)
    db.session.commit()
    return userInfo
  
  # 更新指定用户信息
  @staticmethod
  def updateUserInfoByUserId(userInfo):
    UserInfo.query.filter(UserInfo.user_id == userInfo.user_id).update({
      UserInfo.user_name      :userInfo.user_name,
      UserInfo.user_id        :userInfo.user_id,
      UserInfo.password       :userInfo.password,
      UserInfo.email          :userInfo.email,
      UserInfo.user_type      :userInfo.user_type,
      UserInfo.last_login_time:userInfo.last_login_time,
      UserInfo.prefer_type    :userInfo.prefer_type,
      UserInfo.balance        :userInfo.balance,
      UserInfo.borrow_book_num:userInfo.borrow_book_num,
      UserInfo.search_num     :userInfo.search_num,
    })
    db.session.commit()
    return userInfo

