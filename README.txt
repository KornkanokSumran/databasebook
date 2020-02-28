## Command for start env
\env\Scripts\activate

## SQL Scripts

mysql -uroot -p
### for create database
CREATE DATABASE book_publishing CHARACTER SET UTF8;

## create noob user
CREATE USER bookuser@localhost IDENTIFIED BY 'useronly';
GRANT ALL PRIVILEGES ON book_publishing.* TO bookuser@localhost;
FLUSH PRIVILEGES;

##insert database
INSERT INTO books_book (isbn,title,published_date, publisher) VALUES
