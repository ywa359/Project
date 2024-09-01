CREATE DATABASE IF NOT EXISTS myProject;
USE myProject;
CREATE TABLE IF NOT EXISTS user (
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '用户ID，主键，自动递增',
user_name VARCHAR(20) NOT NULL UNIQUE COMMENT '用户名，非空，唯一',
password VARCHAR(20) NOT NULL COMMENT '密码，非空',
create_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间，非空，默认当前时间',
update_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间，非空，默认当前时间，记录更新时自动更新'
);

CREATE TABLE IF NOT EXISTS user_info (
    user_id INT PRIMARY KEY AUTO_INCREMENT,  -- 用户ID，自动递增
    name VARCHAR(255) NOT NULL,              -- 用户姓名
    gender ENUM('Male', 'Female', 'Other') NOT NULL,  -- 性别，可以选择Male, Female, 或 Other
    email_address VARCHAR(255) NOT NULL,     -- 邮箱地址
    student_id VARCHAR(100) NOT NULL,        -- 学生ID
    github VARCHAR(255),                     -- GitHub 个人主页
    gitlab VARCHAR(255)                      -- GitLab 个人主页
);

CREATE TABLE IF NOT EXISTS user_project (
    project_id INT PRIMARY KEY AUTO_INCREMENT,  -- 项目ID，自动递增
    user_id INT NOT NULL,                       -- 用户ID，外键
    title VARCHAR(255) NOT NULL,                -- 项目标题
    description TEXT NOT NULL,                  -- 项目描述
    start_time DATETIME NOT NULL,               -- 项目开始时间
    end_time DATETIME,                          -- 项目结束时间
    git_link VARCHAR(255),                      -- Git 项目链接
    online_service VARCHAR(255),                -- 在线服务链接（如部署的项目地址）
    skills VARCHAR(255),                        -- 项目使用的技能（例如，编程语言、框架等）
    FOREIGN KEY (user_id) REFERENCES user_info(user_id)  -- 引用 user_info 表的 user_id 作为外键
);

CREATE TABLE IF NOT EXISTS user_skill (
    skill_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    skill_name VARCHAR(255) NOT NULL,
    rate INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user_info(user_id)
);