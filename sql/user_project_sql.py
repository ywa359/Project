import mysql.connector

# 连接到 MySQL 服务器
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="8270022",  # 你的 MySQL 密码
    database="myProject"  # 你要连接的数据库名
)

# 创建游标对象
cursor = conn.cursor()


# TODO: 插入数据
def insert(user_id, title, description, start_time, end_time, git_link, online_service, skills):
    sql = "INSERT INTO user (user_id, title, description, start_time, end_time, git_link, online_service, skills) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (user_id, title, description, start_time, end_time, git_link, online_service, skills)
    cursor.execute(sql, val)
    conn.commit()

# TODO: 查询数据
def search(user_id):
    sql = "SELECT * FROM user_project WHERE user_id = %s"
    cursor.execute(sql, (user_id,))
    result = cursor.fetchone()
    return result
