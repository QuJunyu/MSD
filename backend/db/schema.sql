CREATE DATABASE IF NOT EXISTS campus_book_trade;
USE campus_book_trade;

-- 用户表
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50) UNIQUE NOT NULL,  -- 用户名（唯一）
  password VARCHAR(255) NOT NULL,  -- 密码（后续需加密存储）
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- 创建时间
);

-- 书籍表（支持发布、查看所有书籍）
CREATE TABLE IF NOT EXISTS books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,   -- 书名
    author VARCHAR(100) NOT NULL,  -- 作者
    price DECIMAL(10, 2) NOT NULL, -- 价格
    `condition` VARCHAR(20) NOT NULL,  -- 书籍状态（用反引号避免关键字冲突）
    user_id INT NOT NULL,          -- 发布者ID（关联users表）
    publish_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- 发布时间
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- 插入测试数据
INSERT IGNORE INTO users (username, password) VALUES ('test1', '123456');
INSERT IGNORE INTO users (username, password) VALUES ('test2', '123456');

-- 插入测试书籍（包含状态字段）
INSERT IGNORE INTO books (title, author, price, `condition`, user_id) VALUES 
('Python编程入门', '张三', 30.00, 'new', 1),  -- test1发布
('Java实战', '李四', 25.50, 'used', 2);       -- test2发布
