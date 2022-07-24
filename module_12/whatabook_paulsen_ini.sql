SQL Script for WhatABook Database
CREATE DATABASE whatabook;
CREATE USER ‘whatabook_user’@’localhost’ IDENTIFIED WITH mysql_native_password BY ‘MySQL8IsGREAT!’;
USE whatabook;
CREATE TABLE user (
User_id int auto_increment,
First_name varchar(75),
Last_name varchar(75),
PRIMARY KEY (user_id)
);
CREATE TABLE book (
book_id int auto_increment,
book_name varchar(200),
details_V varchar(500),
author varchar(200),
PRIMARY KEY (book_id)
);
CREATE TABLE store (
Store_id int auto_increment,
Location varchar(500),
PRIMARY KEY (store_id)
);
CREATE TABLE wishlist (
wishlist_id int auto_increment,
user_id int,
book_id int,
PRIMARY KEY (wishlist_id),
CONSTRAINT FK_userwishlist FOREIGN KEY (user_id)
REFERENCES user(user_id),
CONSTRAINT FK_bookwishlist FOREIGN KEY (book_id)
REFERENCES book(book_id)
);
INSERT INTO store (location) VALUES (‘2342 Lost Book AVE New York City’);
INSERT INTO book (book_name, author) VALUES (‘Mad World’, ‘Dug Mind’);
INSERT INTO book (book_name, author) VALUES (‘Lost City’, ‘May Day’);
INSERT INTO book (book_name, author) VALUES (‘The world’, ‘Gabi Holms’);
INSERT INTO book (book_name, author) VALUES (‘Enders Game’, ‘Orson Card’);
INSERT INTO book (book_name, author) VALUES (‘Citizen’, ‘Howard Done’);
INSERT INTO book (book_name, author) VALUES (‘Critters’, ‘Terry Goodkind’);
INSERT INTO book (book_name, author) VALUES (‘Two Towers’, ‘JRR Tolken’);
INSERT INTO book (book_name, author) VALUES (‘Dune’, ‘Frank Hurbert’);
INSERT INTO book (book_name, author) VALUES (‘Gathering’, ‘Simon R Green’);
INSERT INTO user (first_name, last_name) VALUES (‘Donald’, ‘Duck’);
INSERT INTO user (first_name, last_name) VALUES (‘Willard’, ‘Green’);
INSERT INTO user (first_name, last_name) VALUES (‘Nicole’, ‘Rose’);
INSERT INTO wishlist (user_id, book_id) VALUES (‘1’, ‘3’);
INSERT INTO wishlist (user_id, book_id) VALUES (‘2’, ‘9’);
INSERT INTO wishlist (user_id, book_id) VALUES (‘3’, ‘6’);
