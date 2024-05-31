-- Book Details: Menampilkan informasi lengkap tentang buku, termasuk penerbit dan penulis.
CREATE VIEW book_details AS
SELECT 
    b.book_id,
    b.title,
    b.publication_year,
    b.pages,
    p.name AS publisher_name,
    p.city AS publisher_city,
    p.country AS publisher_country,
    STRING_AGG(a.name, ', ') AS authors
FROM 
    book b
JOIN 
    publisher p ON b.publisher_id = p.publisher_id
JOIN 
    book_author ba ON b.book_id = ba.book_id
JOIN 
    author a ON ba.author_id = a.author_id
GROUP BY 
    b.book_id, b.title, b.publication_year, b.pages, p.name, p.city, p.country;


-- User Wishlists: Menampilkan wishlist pengguna beserta buku-buku di dalamnya.
CREATE VIEW user_wishlists AS
SELECT 
    u.user_id,
    u.username,
    w.wishlist_id,
    w.date_created,
    STRING_AGG(b.title, ', ') AS wishlist_books
FROM 
    users u
JOIN 
    wishlist w ON u.user_id = w.user_id
JOIN 
    wishlist_item wi ON w.wishlist_id = wi.wishlist_id
JOIN 
    book b ON wi.book_id = b.book_id
GROUP BY 
    u.user_id, u.username, w.wishlist_id, w.date_created;