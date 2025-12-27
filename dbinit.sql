CREATE DATABASE IF NOT EXISTS arduinodatadb;

USE arduinodatadb;

CREATE TABLE device (
    device_id INT AUTO_INCREMENT PRIMARY KEY,
    device_name VARCHAR(255) NOT NULL,
    port VARCHAR(255) NOT NULL,
    baud INT NOT NULL,
    is_deleted BOOLEAN NOT NULL DEFAULT FALSE,
    deleted_at DATETIME NULL,
    UNIQUE (device_name)
);

CREATE TABLE reads (
    regtime DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    id INT AUTO_INCREMENT,
    device_id INT NOT NULL,
    readData INT,
    PRIMARY KEY (id),
    FOREIGN KEY (device_id) REFERENCES device(device_id)
);