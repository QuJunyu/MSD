CREATE DATABASE IF NOT EXISTS campus_book_trade;
USE campus_book_trade;

CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,  -- Incremental ID
  username VARCHAR(50) UNIQUE NOT NULL,  -- User name (unique)
  password VARCHAR(255) NOT NULL,  -- Password (for subsequent encryption and storage)
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Creation Date
);

-- 书籍表（支持发布、查看所有书籍）
CREATE TABLE IF NOT EXISTS books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,   -- 书名
    author VARCHAR(100) NOT NULL,  -- 作者
    price DECIMAL(10, 2) NOT NULL, -- 价格
    user_id INT NOT NULL,          -- 发布者ID（关联users表）
    publish_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- 发布时间
    FOREIGN KEY (user_id) REFERENCES users(id)  -- 关联用户
);


-- 插入测试用户（方便C测试登录功能）
-- 用户名：test1，密码：123456（C可直接用此账号测试）
INSERT IGNORE INTO users (username, password) VALUES ('test1', '123456');
INSERT IGNORE INTO books (title, author, price, user_id) VALUES 
('Python', 'A', 30.00, 1),  -- test1发布的书
('Java', 'B', 25.50, 2);   -- test2发布的书
