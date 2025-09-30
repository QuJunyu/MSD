CREATE DATABASE IF NOT EXISTS campus_book_trade;
USE campus_book_trade;

CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,  -- Incremental ID
  username VARCHAR(50) UNIQUE NOT NULL,  -- User name (unique)
  password VARCHAR(255) NOT NULL,  -- Password (for subsequent encryption and storage)
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Creation Date
);
