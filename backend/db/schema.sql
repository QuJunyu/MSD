CREATE DATABASE IF NOT EXISTS campus_book_trade;
USE campus_book_trade;

CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,  -- Incremental ID
  username VARCHAR(50) UNIQUE NOT NULL,  -- User name (unique)
  password VARCHAR(255) NOT NULL,  -- Password (for subsequent encryption and storage)
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Creation time
);

-- Insert test user (facilitates testing of the login function in C)
-- Username: test1, Password: 123456 (this account can be directly used for testing in C)
INSERT IGNORE INTO users (username, password) VALUES ('test1', '123456');
