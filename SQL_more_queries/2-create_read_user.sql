-- Creates the database hbtn_0d_2 and the user user_0d_2
-- user_0d_2 should have only SELECT privilege in hbtn_0d_2
-- Password is set to user_0d_2_pwd
-- Script will not fail if database or user already exists

-- Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege on the specific database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;