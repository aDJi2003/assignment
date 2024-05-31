-- Digunakan untuk memulai sebuah transaksi
BEGIN;

-- Digunakan untuk membuat titik penyimpanan (savepoint) dalam sebuah transaksi
SAVEPOINT savepoint1;

-- Digunakan untuk menambahkan data baru ke dalam tabel book
INSERT INTO book (book_id, title, publication_year, pages, publisher_id) 
VALUES (2, 'Book B', 2023, '250', 2);

-- Digunakan untuk membatalkan semua perubahan yang terjadi sejak savepoint savepoint1 dibuat.
ROLLBACK TO savepoint1;

-- Digunakan untuk menyelesaikan transaksi
COMMIT;