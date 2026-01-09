-- Creates the table id_not_null on the MySQL server
-- id: INT with the default value 1
-- name: VARCHAR(256)
-- The script should not fail if the table already exists
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);