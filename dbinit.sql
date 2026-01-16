CREATE DATABASE IF NOT EXISTS arduinodatadb;

USE arduinodatadb;

CREATE TABLE device (
    device_id INT AUTO_INCREMENT PRIMARY KEY,
    device_name VARCHAR(255) NOT NULL,
    baud INT NOT NULL DEFAULT 9600,
    is_deleted BOOLEAN NOT NULL DEFAULT FALSE,
    UNIQUE (device_name)
);