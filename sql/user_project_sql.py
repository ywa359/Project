from utils.db_manager import DBManager

# 获取单例DBManager实例
db_manager = DBManager()

# 获取数据库连接
conn = db_manager.connect()
# 创建游标对象
cursor = conn.cursor()


# TODO: 插入数据
def insert(user_id, title, description, start_time, end_time, git_link,
           online_service, skills):
    sql = "INSERT INTO user (user_id, title, description, start_time, end_time, git_link, online_service, skills) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (
    user_id, title, description, start_time, end_time, git_link, online_service,
    skills)
    cursor.execute(sql, val)
    conn.commit()


# TODO: 查询数据
def search(user_id):
    sql = "SELECT * FROM user_project WHERE user_id = %s"
    cursor.execute(sql, (user_id,))
    result = cursor.fetchall()
    return result
