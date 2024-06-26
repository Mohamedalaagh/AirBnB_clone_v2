-- This script prepares a MySQL server for the project.

-- Create project development database with the name: hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create a new user named: hbnb_dev with all privileges on the database hbnb_dev_db
-- with the password: hbnb_dev_pwd if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges to the new user on the database hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Apply the changes
FLUSH PRIVILEGES;

-- Grant the SELECT privilege to the user hbnb_dev on the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Apply the changes
FLUSH PRIVILEGES;

