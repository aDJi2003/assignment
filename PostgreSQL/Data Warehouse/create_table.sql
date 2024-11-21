-- Tabel dimensi produk
CREATE TABLE dim_produk (
    id_produk SERIAL PRIMARY KEY,
    nama_produk VARCHAR(100) NOT NULL,
    kategori VARCHAR(50),
    harga_satuan NUMERIC(10, 2),
    merek VARCHAR(50)
);

-- Tabel dimensi pelanggan
CREATE TABLE dim_pelanggan (
    id_pelanggan SERIAL PRIMARY KEY,
    nama_pelanggan VARCHAR(100) NOT NULL,
    jenis_kelamin CHAR(1) CHECK (jenis_kelamin IN ('L', 'P')),
    usia INTEGER,
    lokasi_pelanggan VARCHAR(100)
);

-- Tabel dimensi waktu
CREATE TABLE dim_waktu (
    id_waktu SERIAL PRIMARY KEY,
    tanggal DATE NOT NULL,
    hari VARCHAR(20),
    bulan VARCHAR(20),
    kuartal INTEGER CHECK (kuartal BETWEEN 1 AND 4),
    tahun INTEGER
);

-- Tabel dimensi lokasi
CREATE TABLE dim_lokasi (
    id_lokasi SERIAL PRIMARY KEY,
    nama_toko VARCHAR(100),
    kota VARCHAR(100),
    provinsi VARCHAR(100),
    negara VARCHAR(100)
);

-- Tabel dimensi promosi
CREATE TABLE dim_promosi (
    id_promosi SERIAL PRIMARY KEY,
    nama_promosi VARCHAR(100),
    tipe_promosi VARCHAR(50),
    diskon_percent NUMERIC(5, 2) CHECK (diskon_percent BETWEEN 0 AND 100)
);

-- Tabel fakta penjualan
CREATE TABLE fakta_penjualan (
    id_transaksi SERIAL PRIMARY KEY,
    id_produk INTEGER REFERENCES dim_produk(id_produk),
    id_pelanggan INTEGER REFERENCES dim_pelanggan(id_pelanggan),
    id_waktu INTEGER REFERENCES dim_waktu(id_waktu),
    id_lokasi INTEGER REFERENCES dim_lokasi(id_lokasi),
    id_promosi INTEGER REFERENCES dim_promosi(id_promosi),
    jumlah_barang INTEGER NOT NULL,
    total_harga NUMERIC(15, 2) NOT NULL,
    diskon NUMERIC(15, 2),
    pendapatan NUMERIC(15, 2) GENERATED ALWAYS AS (total_harga - diskon) STORED
);

-- Tabel fakta pengembalian
CREATE TABLE fakta_pengembalian (
    id_pengembalian SERIAL PRIMARY KEY,
    id_produk INTEGER REFERENCES dim_produk(id_produk),
    id_pelanggan INTEGER REFERENCES dim_pelanggan(id_pelanggan),
    id_waktu INTEGER REFERENCES dim_waktu(id_waktu),
    id_lokasi INTEGER REFERENCES dim_lokasi(id_lokasi),
    jumlah_barang_dikembalikan INTEGER NOT NULL,
    alasan_pengembalian VARCHAR(255)
);
