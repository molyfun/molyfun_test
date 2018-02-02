import pymysql

# 打开数据库连接
db = pymysql.connect(
    host='192.168.3.30',
    port=3306,
    user='root',
    passwd='molyfun',
    db='hello_yilin',
    charset='utf8'
    )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

#查询版本
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()    # 使用fetchall方法返回所有查询结果
print("Database version : %s " % data)   # 打印查询结果

#查询
cursor.execute("select * from mh_student_enrol where name='田园';")
data = cursor.fetchone()
print(data)

db.close()  # 关闭连接
