from utils.db_manager import DBManager

# 获取单例DBManager实例
db_manager = DBManager()

# 获取数据库连接
conn = db_manager.connect()
# 创建游标对象
cursor = conn.cursor()


# TODO: 插入数据
def insert(user_name, password):
    sql = "INSERT INTO user (user_name, password) VALUES (%s, %s)"
    val = (user_name, password)
    cursor.execute(sql, val)
    conn.commit()


# TODO: 查询数据
def search():
    cursor.execute("SELECT * FROM user")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def exist(user_name, password):
    select_query = "select * from user where user_name=%s and password=%s"
    cursor.execute(select_query, (user_name, password))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    if len(rows) == 1:
        return True, rows[0][0]
    return False, None


def duplicate(user_name):
    select_query = "select * from user where user_name=%s"
    cursor.execute(select_query, (user_name,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    return len(rows) == 1
