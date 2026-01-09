-- Creates the MySQL server user user_0d_1
-- Password is set to user_0d_1_pwd
-- Script will not fail if the user already exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grants all privileges on the MySQL server to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Ensures that the privileges are applied immediately
FLUSH PRIVILEGES;