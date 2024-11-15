这是SOA实验二的图书管理项目
首先执行
pip install -r requirements.txt
来安装虚拟环境依赖

随后搭建数据库，
1.将config.py中的内容替换为自己的内容
2.删除文件夹migrations
3.在本地数据库新建一个数据库，名字和config.py中的相同即可
4.在命令行执行
  flask db init
  flask db migrate
  flask db upgrade
5.此时数据库表已经建立，执行sql文件插入数据即可，注意执行时请把sql文件中有关建表的语句删除，只保留插入数据的语句。
