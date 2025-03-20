CREATE DATABASE IF NOT EXISTS form_db;
USE form_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    dob DATE NOT NULL,
    age INT NOT NULL,
    gender ENUM('male', 'female', 'others') NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    state VARCHAR(100) NOT NULL,
    courses VARCHAR(100) NOT NULL,
    photo VARCHAR(255)
);
