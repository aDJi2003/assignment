-- Insert ke tabel dim_produk
INSERT INTO dim_produk (nama_produk, kategori, harga_satuan, merek)
VALUES
('Laptop X', 'Elektronik', 15000000, 'Brand A'),
('Smartphone Y', 'Elektronik', 5000000, 'Brand B');

-- Insert ke tabel dim_pelanggan
INSERT INTO dim_pelanggan (nama_pelanggan, jenis_kelamin, usia, lokasi_pelanggan)
VALUES
('Ali', 'L', 30, 'Yogyakarta'),
('Budi', 'L', 25, 'Jakarta');

-- Insert ke tabel dim_waktu
INSERT INTO dim_waktu (tanggal, hari, bulan, kuartal, tahun)
VALUES
('2024-11-14', 'Kamis', 'November', 4, 2024);

-- Insert ke tabel dim_lokasi
INSERT INTO dim_lokasi (nama_toko, kota, provinsi, negara)
VALUES
('Toko A', 'Yogyakarta', 'DIY', 'Indonesia');

-- Insert ke tabel dim_promosi
INSERT INTO dim_promosi (nama_promosi, tipe_promosi, diskon_percent)
VALUES
('Promo Akhir Tahun', 'Diskon', 10);

-- Insert ke tabel fakta_penjualan
INSERT INTO fakta_penjualan (id_produk, id_pelanggan, id_waktu, id_lokasi, id_promosi, jumlah_barang, total_harga, diskon)
VALUES
(1, 1, 1, 1, 1, 2, 30000000, 3000000),
(2, 2, 1, 1, 1, 1, 5000000, 500000);

-- Insert ke tabel fakta_pengembalian
INSERT INTO fakta_pengembalian (id_produk, id_pelanggan, id_waktu, id_lokasi, jumlah_barang_dikembalikan, alasan_pengembalian)
VALUES
(1, 1, 1, 1, 2, 'Barang rusak saat pengiriman');