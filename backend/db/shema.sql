-- 创建数据库（如不存在）
CREATE DATABASE IF NOT EXISTS campus_book_trade;
USE campus_book_trade;

-- 用户表（存储登录/注册信息）
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,  -- 自增ID
  username VARCHAR(50) UNIQUE NOT NULL,  -- 用户名（唯一）
  password VARCHAR(255) NOT NULL,  -- 密码（后续加密存储）
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- 创建时间
);
