-- Creates the table force_name on the MySQL server
-- id: INT
-- name: VARCHAR(256) cannot be null
-- The script should not fail if the table already exists
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);