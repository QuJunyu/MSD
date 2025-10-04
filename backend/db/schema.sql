-- Create database (if it doesn't exist)
CREATE DATABASE IF NOT EXISTS campus_book;
USE campus_book;

-- User table (supports login, registration, password modification)
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,  -- Username (unique)
    password VARCHAR(255) NOT NULL         -- Password (plain text, needs encryption in actual projects)
);

-- Book table (supports publishing, viewing all books)
CREATE TABLE IF NOT EXISTS books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,   -- Book title
    author VARCHAR(100) NOT NULL,  -- Author
    price DECIMAL(10, 2) NOT NULL, -- Price
    user_id INT NOT NULL,          -- Publisher ID (associated with users table)
    publish_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Publishing time
    FOREIGN KEY (user_id) REFERENCES users(id)  -- Associated user
);

-- Insert test data
INSERT IGNORE INTO users (username, password) VALUES 
('test1', '123456'),  -- Test user 1 (password can be modified)
('test2', '456789');  -- Test user 2

INSERT IGNORE INTO books (title, author, price, user_id) VALUES 
('Python Programming', 'Zhang San', 30.00, 1),  -- Book published by test1
('Java Introduction', 'Li Si', 25.50, 2);   -- Book published by test2
