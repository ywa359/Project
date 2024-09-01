CREATE DATABASE IF NOT EXISTS myProject;
USE myProject;

CREATE TABLE IF NOT EXISTS user (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'User ID, primary key, auto-increment',
    user_name VARCHAR(20) NOT NULL UNIQUE COMMENT 'Username, not null, unique',
    password VARCHAR(20) NOT NULL COMMENT 'Password, not null',
    create_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Creation time, not null, defaults to current time',
    update_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Update time, not null, defaults to current time, automatically updates on record update'
);

CREATE TABLE IF NOT EXISTS user_info (
    user_id INT PRIMARY KEY AUTO_INCREMENT,  -- User ID, auto-increment
    name VARCHAR(255) NOT NULL,              -- User name
    gender ENUM('Male', 'Female', 'Other') NOT NULL,  -- Gender, can be Male, Female, or Other
    email_address VARCHAR(255) NOT NULL,     -- Email address
    student_id VARCHAR(100) NOT NULL,        -- Student ID
    github VARCHAR(255),                     -- GitHub profile
    gitlab VARCHAR(255)                      -- GitLab profile
);

CREATE TABLE IF NOT EXISTS user_project (
    project_id INT PRIMARY KEY AUTO_INCREMENT,  -- Project ID, auto-increment
    user_id INT NOT NULL,                       -- User ID, foreign key
    title VARCHAR(255) NOT NULL,                -- Project title
    description TEXT NOT NULL,                  -- Project description
    start_time DATETIME NOT NULL,               -- Project start time
    end_time DATETIME,                          -- Project end time
    git_link VARCHAR(255),                      -- Git project link
    online_service VARCHAR(255),                -- Online service link (e.g., deployed project URL)
    skills VARCHAR(255),                        -- Skills used in the project (e.g., programming languages, frameworks)
    FOREIGN KEY (user_id) REFERENCES user_info(user_id)  -- References user_id from user_info as a foreign key
);

CREATE TABLE IF NOT EXISTS user_skill (
    skill_id INT PRIMARY KEY AUTO_INCREMENT,  -- Skill ID, auto-increment
    user_id INT NOT NULL,                     -- User ID, foreign key
    skill_name VARCHAR(255) NOT NULL,         -- Skill name
    rate INT NOT NULL,                        -- Skill rating
    FOREIGN KEY (user_id) REFERENCES user_info(user_id)  -- References user_id from user_info as a foreign key
);
