CREATE DATABASE IF NOT EXISTS campus_book_trade;
USE campus_book_trade;

CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,  -- Auto-increment ID
  username VARCHAR(50) UNIQUE NOT NULL,  -- Username (unique)
  password VARCHAR(255) NOT NULL,  -- Password (for subsequent encryption and storage)
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Creation time
);

-- Book table (supports publishing and viewing all books)
CREATE TABLE IF NOT EXISTS books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,   -- Book title
    author VARCHAR(100) NOT NULL,  -- Author
    price DECIMAL(10, 2) NOT NULL, -- Price
    user_id INT NOT NULL,          -- Publisher ID (关联 users table)
    publish_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Publishing time
    FOREIGN KEY (user_id) REFERENCES users(id)  --关联 user table
);


-- Insert test users (facilitates testing the login function for C)
-- Username: test1, password: 123456 (C can directly use this account for testing)
INSERT IGNORE INTO users (username, password) VALUES ('test1', '123456');
INSERT IGNORE INTO books (title, author, price, user_id) VALUES 
('Python', 'A', 30.00, 1),  -- Book published by test1
('Java', 'B', 25.50, 2);   -- Book published by test2
