-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 14, 2023 at 05:12 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 7.4.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_appperpustakaan`
--

-- --------------------------------------------------------

--
-- Table structure for table `anggota`
--

CREATE TABLE `anggota` (
  `id_anggota` int(11) NOT NULL,
  `kode_anggota` varchar(10) NOT NULL,
  `nama_anggota` varchar(100) NOT NULL,
  `jk_anggota` enum('L','P') NOT NULL DEFAULT 'L',
  `prodi_anggota` enum('TIF','IND','PET') NOT NULL DEFAULT 'TIF',
  `alamat_anggota` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `anggota`
--

INSERT INTO `anggota` (`id_anggota`, `kode_anggota`, `nama_anggota`, `jk_anggota`, `prodi_anggota`, `alamat_anggota`) VALUES
(1, '1010', 'Wahyudi', 'L', 'TIF', 'Kabupaten Cirebon'),
(2, '2020', 'Adelia', 'P', 'IND', 'Kota Cirebon'),
(8, '3030', 'Gisele', 'P', 'PET', 'Kota Cirebon');

-- --------------------------------------------------------

--
-- Table structure for table `buku`
--

CREATE TABLE `buku` (
  `id_buku` int(11) NOT NULL,
  `kode_buku` varchar(10) NOT NULL,
  `judul_buku` varchar(50) NOT NULL,
  `penulis_buku` varchar(50) NOT NULL,
  `penerbit_buku` varchar(50) NOT NULL,
  `tahun_terbit` varchar(50) NOT NULL,
  `gendre` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `buku`
--

INSERT INTO `buku` (`id_buku`, `kode_buku`, `judul_buku`, `penulis_buku`, `penerbit_buku`, `tahun_terbit`, `gendre`) VALUES
(1, '210', 'Koala Kumal', 'Raditya Dika', 'Gagas Media', '2015', 'Fiksi'),
(2, '211', 'One Piece', 'Eichiro Oda', 'Toei Animation', '1998', '100'),
(3, '212', 'Destilasi Alkena', 'Wira Nagara', 'Gramedia', '2018', '30');

-- --------------------------------------------------------

--
-- Table structure for table `peminjaman`
--

CREATE TABLE `peminjaman` (
  `id_peminjaman` int(11) NOT NULL,
  `kode_peminjaman` varchar(10) NOT NULL,
  `tgll_pinjam` varchar(15) NOT NULL,
  `tanggal_kembali` varchar(15) NOT NULL,
  `kode_buku` int(11) NOT NULL,
  `kode_anggota` int(11) NOT NULL,
  `kode_petugas` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `pengembalian`
--

CREATE TABLE `pengembalian` (
  `id_pengembalian` int(11) NOT NULL,
  `kode_pengembalian` varchar(10) NOT NULL,
  `tgl_pengembalian` varchar(15) NOT NULL,
  `kode_buku` int(11) NOT NULL,
  `kode_anggota` int(11) NOT NULL,
  `kode_petugas` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pengembalian`
--

INSERT INTO `pengembalian` (`id_pengembalian`, `kode_pengembalian`, `tgl_pengembalian`, `kode_buku`, `kode_anggota`, `kode_petugas`) VALUES
(1, '1222', '12-02-2019', 12, 12, 12);

-- --------------------------------------------------------

--
-- Table structure for table `petugas`
--

CREATE TABLE `petugas` (
  `id_petugas` int(11) NOT NULL,
  `kode_petugas` varchar(10) NOT NULL,
  `nama_petugas` varchar(50) NOT NULL,
  `jabatan_petugas` enum('K.Perpus','Admin','Kasir') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `petugas`
--

INSERT INTO `petugas` (`id_petugas`, `kode_petugas`, `nama_petugas`, `jabatan_petugas`) VALUES
(1, '111', 'Krisna', 'Admin'),
(2, '222', 'Pragos', 'Admin'),
(3, '333', 'Amir', 'K.Perpus'),
(4, '444', 'Kania', 'Kasir');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `anggota`
--
ALTER TABLE `anggota`
  ADD PRIMARY KEY (`id_anggota`),
  ADD UNIQUE KEY `UNIk` (`kode_anggota`) USING BTREE;

--
-- Indexes for table `buku`
--
ALTER TABLE `buku`
  ADD PRIMARY KEY (`id_buku`),
  ADD UNIQUE KEY `unik` (`kode_buku`) USING BTREE;

--
-- Indexes for table `peminjaman`
--
ALTER TABLE `peminjaman`
  ADD PRIMARY KEY (`id_peminjaman`),
  ADD UNIQUE KEY `kode pinjam` (`kode_peminjaman`),
  ADD KEY `id_buku` (`kode_buku`),
  ADD KEY `id_anggota` (`kode_anggota`),
  ADD KEY `id_petugas` (`kode_petugas`);

--
-- Indexes for table `pengembalian`
--
ALTER TABLE `pengembalian`
  ADD PRIMARY KEY (`id_pengembalian`),
  ADD UNIQUE KEY `kode kembali` (`kode_pengembalian`),
  ADD KEY `id_buku` (`kode_buku`),
  ADD KEY `id_petugas` (`kode_petugas`),
  ADD KEY `id_anggota` (`kode_anggota`);

--
-- Indexes for table `petugas`
--
ALTER TABLE `petugas`
  ADD PRIMARY KEY (`id_petugas`),
  ADD UNIQUE KEY `kode petugas` (`kode_petugas`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `anggota`
--
ALTER TABLE `anggota`
  MODIFY `id_anggota` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `buku`
--
ALTER TABLE `buku`
  MODIFY `id_buku` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `peminjaman`
--
ALTER TABLE `peminjaman`
  MODIFY `id_peminjaman` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `pengembalian`
--
ALTER TABLE `pengembalian`
  MODIFY `id_pengembalian` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `petugas`
--
ALTER TABLE `petugas`
  MODIFY `id_petugas` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
