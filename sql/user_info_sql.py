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
def insert(user_id, name, gender, email_address, student_id, github, gitlab):
    sql = "INSERT INTO user_info (user_id, name, gender, email_address, student_id, github, gitlab) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (user_id, name, gender, email_address, student_id, github, gitlab)
    cursor.execute(sql, val)
    conn.commit()

# 更新
def update(user_id, name=None, gender=None, email_address=None, student_id=None, github=None, gitlab=None):
    updates = []
    values = []

    if name is not None:
        updates.append("name = %s")
        values.append(name)
    if gender is not None:
        updates.append("gender = %s")
        values.append(gender)
    if email_address is not None:
        updates.append("email_address = %s")
        values.append(email_address)
    if student_id is not None:
        updates.append("student_id = %s")
        values.append(student_id)
    if github is not None:
        updates.append("github = %s")
        values.append(github)
    if gitlab is not None:
        updates.append("gitlab = %s")
        values.append(gitlab)

    values.append(user_id)

    if updates:
        sql = f"UPDATE user_info SET {', '.join(updates)} WHERE user_id = %s"
        cursor.execute(sql, values)
        conn.commit()


# TODO: 查询数据
def search(user_id):
    sql = "SELECT * FROM user_info WHERE user_id = %s"
    cursor.execute(sql, (user_id,))
    result = cursor.fetchone()
    return result
