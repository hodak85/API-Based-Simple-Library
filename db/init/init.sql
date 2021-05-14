CREATE DATABASE mylib;
USE mylib

CREATE TABLE book (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	title VARCHAR(100) NOT NULL,
	author VARCHAR(100) NOT NULL,
	existance Boolean NOT NULL DEFAULT True,
	pub_date DATE
); 

CREATE TABLE user (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	user VARCHAR(100) NOT NULL,
	password VARCHAR(100) NOT NULL
);

INSERT INTO user ( user , password) values ('admin', MD5('admin'));
