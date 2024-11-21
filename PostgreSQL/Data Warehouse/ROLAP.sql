-- Roll-up
SELECT bulan, SUM(total_pendapatan) AS total_pendapatan
FROM (
    SELECT EXTRACT(MONTH FROM dim_waktu.tanggal) AS bulan, fakta_penjualan.pendapatan AS total_pendapatan
    FROM fakta_penjualan
    JOIN dim_waktu ON fakta_penjualan.id_waktu = dim_waktu.id_waktu
) AS subquery
GROUP BY bulan
ORDER BY bulan;

-- Drill-down
SELECT tanggal, nama_produk, SUM(jumlah_barang) AS total_jumlah
FROM fakta_penjualan
JOIN dim_waktu ON fakta_penjualan.id_waktu = dim_waktu.id_waktu
JOIN dim_produk ON fakta_penjualan.id_produk = dim_produk.id_produk
GROUP BY tanggal, nama_produk;

-- Slice
SELECT nama_produk, SUM(pendapatan) AS total_pendapatan
FROM fakta_penjualan
JOIN dim_produk ON fakta_penjualan.id_produk = dim_produk.id_produk
WHERE kategori = 'Elektronik'
GROUP BY nama_produk;

-- Dice
SELECT kota, nama_produk, SUM(jumlah_barang) AS total_jumlah
FROM fakta_penjualan
JOIN dim_lokasi ON fakta_penjualan.id_lokasi = dim_lokasi.id_lokasi
JOIN dim_waktu ON fakta_penjualan.id_waktu = dim_waktu.id_waktu
JOIN dim_produk ON fakta_penjualan.id_produk = dim_produk.id_produk
WHERE kota = 'Yogyakarta' AND kuartal = 4
GROUP BY kota, nama_produk;

-- Pivot
SELECT kota, SUM(jumlah_barang) AS total_jumlah, SUM(pendapatan) AS total_pendapatan
FROM fakta_penjualan
JOIN dim_lokasi ON fakta_penjualan.id_lokasi = dim_lokasi.id_lokasi
GROUP BY kota;
