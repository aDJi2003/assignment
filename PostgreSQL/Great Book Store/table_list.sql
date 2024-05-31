CREATE TABLE publisher (
    publisher_id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    city VARCHAR(255),
    country VARCHAR(255),
    telephone VARCHAR(20),
    year_founded INT
);

CREATE TABLE author (
    author_id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    year_born INT,
    year_died INT
);

CREATE TABLE book (
    book_id INT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    publication_year INT,
    pages VARCHAR(100),
    publisher_id INT REFERENCES publisher(publisher_id)
);

CREATE TABLE book_author (
    book_id INT REFERENCES book(book_id),
    author_id INT REFERENCES author(author_id),
    PRIMARY KEY (book_id, author_id)
);

CREATE TABLE customer (
    customer_id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    street VARCHAR(255),
    city VARCHAR(255),
    country VARCHAR(255),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);

CREATE TABLE publisher_contact (
    contact_id INT PRIMARY KEY,
    contact_name VARCHAR(255),
    contact_email VARCHAR(255),
    contact_phone VARCHAR(20),
    publisher_id INT REFERENCES publisher(publisher_id)
);

CREATE TABLE users (
    user_id INT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    customer_id INT UNIQUE REFERENCES customer(customer_id)
);

CREATE TABLE wishlist (
    wishlist_id INT PRIMARY KEY,
    date_created DATE NOT NULL,
    user_id INT REFERENCES users(user_id)
);

CREATE TABLE wishlist_item (
    wishlist_id INT REFERENCES wishlist(wishlist_id),
    book_id INT REFERENCES book(book_id),
    date_added DATE NOT NULL,
    PRIMARY KEY (wishlist_id, book_id)
);

CREATE TABLE category (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE book_category (
    book_id INT REFERENCES book(book_id),
    category_id INT REFERENCES category(category_id),
    PRIMARY KEY (book_id, category_id)
);

CREATE TABLE review (
    review_id SERIAL PRIMARY KEY,
    book_id INT REFERENCES book(book_id),
    user_id INT REFERENCES users(user_id),
    comment TEXT,
    date_posted DATE NOT NULL
);

CREATE TABLE session (
    session_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    session_token VARCHAR(255) NOT NULL,
    expiration_date TIMESTAMP NOT NULL
);

CREATE TABLE genre (
    genre_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE book_genre (
    book_id INT REFERENCES book(book_id),
    genre_id INT REFERENCES genre(genre_id),
    PRIMARY KEY (book_id, genre_id)
);