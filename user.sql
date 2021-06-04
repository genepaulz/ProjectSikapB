-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 04, 2021 at 05:04 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `projectsikap`
--

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` bigint(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `firstname` varchar(100) NOT NULL,
  `lastname` varchar(100) NOT NULL,
  `user_type` int(11) NOT NULL,
  `isVerified` int(11) NOT NULL,
  `companyName` varchar(100) NOT NULL,
  `industry` varchar(100) NOT NULL,
  `region` varchar(100) NOT NULL,
  `province` varchar(100) NOT NULL,
  `city` varchar(100) NOT NULL,
  `age` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `email`, `password`, `firstname`, `lastname`, `user_type`, `isVerified`, `companyName`, `industry`, `region`, `province`, `city`, `age`) VALUES
(1, 'larry_trivett@abscbn.com', '$pbkdf2-sha256$10$/98bI4TwvrdWqvX.3ztHiA$5Y5t8FTrOgD1oHRS.cBiL8xdP5RLJ7wS/pBdub/H0Fw', 'Larry', 'Trivett', 1, 0, 'ABS-CBN', 'Entertainment', '', '', '', 0),
(2, 'wbishop@bpi.com', '$pbkdf2-sha256$10$f49RyrkXwhijVOo9h3DufQ$S9eFQm1CCbuagFXwdgKiRlyODBjJqAXLfptDAgUm8yc', 'Wren', 'Bishop', 1, 0, 'BPI', 'Finanace', '', '', '', 0),
(3, 'woody_saunders@samsung.com', '$pbkdf2-sha256$10$XktJKSUEgPB.r3VOaY0x5g$Qd4vV3hpumfh6/jLzele78vLdDc39Er/uOLBbiUKPas', 'Woody', 'Saunders', 1, 0, 'Samsung', 'Computer', '', '', '', 0),
(4, 'echoholden234@alphamusic.com', '$pbkdf2-sha256$10$Tqn1Puc8ByAEYAyBMGastQ$TvN9dQLfHrMDAh3Aei0HUIJiLGqrJbJPvMgzZOaQvHo', 'Echo', 'Holden', 1, 0, 'Alpha Music', 'Music', '', '', '', 0),
(5, 'jmatthews087@ayala.com', '$pbkdf2-sha256$10$WStF6H3P.b8XwhjD.P./Vw$Csx2lObbQnP.eP/4kviEAPe4rxAD9J8rJG9H.Rg/TCw', 'Joanna', 'Matthews', 1, 0, 'Ayala', 'Manufacturing', '', '', '', 0),
(6, 'jmarks@email.com', '$pbkdf2-sha256$10$6P2/l9JaC0FobQ3BeG8tZQ$V6rTvkqgDQeLpDo0XRAffSVfZPxkC14fcqg2LBLUMzw', 'Jonathan', 'Marks', 0, 0, '', 'Entertainment', 'VII', 'Cebu', 'Cebu', 22),
(7, 'monty123@email.com', '$pbkdf2-sha256$10$ljKmdI4xBgCglDLmXEtpDQ$ckA9AQjfrNOVQwbCjmtDo7wscg4ESUH7dBD.vsmQvUI', 'Monty', 'Python', 0, 0, '', 'Entertainment', 'VII', 'Cebu', 'Lapu-Lapu', 32),
(8, 'janfrancis@email.com', '$pbkdf2-sha256$10$.39v7R2DEKIUgrC29t67Fw$OnUi3bwXliJ/gLzoHTeAx5O6ha/BywuqOg7ldu2pn6E', 'Jan', 'Arzadon', 0, 0, '', 'Computer', 'VII', 'Cebu', 'Cebu', 25),
(9, 'zackhilacan@email.com', '$pbkdf2-sha256$10$sXaOcW5trRXifC/l/F/rPQ$u8y1fA4r4Hi6pDDVL9ySISOsAeVhU7CxsPFAAblyh6A', 'Zack', 'Hilacan', 0, 0, '', 'Finance', 'VII', 'Cebu', 'Lapu-Lapu', 30),
(10, 'genezaf@email.com', '$pbkdf2-sha256$10$AIAQwjjHOEeI0dpbC.H8Pw$H4O9AYu.pbk1cSvRgcqFVaZ38F9MNvDbP.FvceDEhso', 'Gene', 'Zafra', 0, 0, '', 'Computer', 'VII', 'Cebu', 'Mandaue', 26),
(11, 'nawit@email.com', '$pbkdf2-sha256$10$bC2FEGIsBQCgFIIQwri3Ng$y8GV.y5f65364/1bFix0Evq/fLybZfypQQjAJgNv9.U', 'Nathan', 'Awit', 0, 0, '', 'Music', 'VII', 'Cebu', 'Talisay', 26),
(12, 'ajcabaron@email.com', '$pbkdf2-sha256$10$xHivVapVCuH837uXcu4dww$padADW5ulgchUaBNm1JnW8z8XZH5OI3nboXVhCFmDUg', 'Adrien', 'Cabaron', 0, 0, '', 'Manufacturing', 'VII', 'Cebu', 'Danao', 34),
(13, 'llache@email.com', '$pbkdf2-sha256$10$khKC0Hrv3TvnfA.hFMIYAw$5JalPKkrGM0yHlXI9p1JY9H9sUqa9fLak7Nj6Xk8nn0', 'Leo', 'Lache', 0, 0, '', 'Entertainment', 'VII', 'Cebu', 'Carcar ', 28),
(14, 'rowblair95@email.com', '$pbkdf2-sha256$10$Y0zJudea854zpnQOAYAwZg$1nxM5ZpXGYbab7K0khbsrWYBuMx8Mnp52BbhTrUuaCE', 'Rowena', 'Blair', 0, 0, '', 'Computer', 'VII', 'Cebu', 'Mandaue', 29),
(15, 'aubreynash321@email.com', '$pbkdf2-sha256$10$rbXWujcGYEwJYSxFSAmhVA$i60f8B6L5Ui69vYXYDHPALoeTlRN2p94axKSsLZ8syM', 'Aubrey', 'Nash', 0, 0, '', 'Finance', 'VII', 'Cebu', 'Mandaue', 35),
(16, 'priscwint@email.com', '$pbkdf2-sha256$10$nnMOAaDU.h.j9L4XwvhfSw$/5YRyQRO7nJ4iyXdBzdQE07/EGysg1PDTTGbMdiEwmo', 'Priscilla', 'Wintringham', 0, 0, '', 'Manufacturing', 'VII', 'Cebu', 'Lilioan', 34),
(17, 'ted_marsh32@email.com', '$pbkdf2-sha256$10$4Py/V.o9h3Au5bx3rpWSMg$ZRza9ucW/3YtyTCk7.EHHgeRLICF864Ax4O393/D.ig', 'Theodore', 'Marshall', 0, 0, '', 'Computer', 'VII', 'Cebu', 'Carcar ', 23),
(18, 'vitasmart_99@email.com', '$pbkdf2-sha256$10$ea81xlirVeo9pzTGeM/5fw$waDkF5H4MJBtOTAZ8m7JEBKEzjGob2G6xB9BG6ZP2Jw', 'Vita', 'Smart', 0, 0, '', 'Music', 'VII', 'Cebu', 'Talisay', 27),
(19, 'erin_daves84@email.com', '$pbkdf2-sha256$10$SsnZ21urVaoVwpjTGuNcSw$.nxpIAgmra2d8/MgW/sUMbAns0i3i3WgFZijqk6vOLU', 'Erin', 'Daves', 0, 0, '', 'Manufacturing', 'VII', 'Cebu', 'Cebu', 28),
(20, 'audreyh456@email.com', '$pbkdf2-sha256$10$i3Gudc65dy6ldK5VytkbYw$93sL0.UYx94ssnbn9o7uDihoeeoAbAP8dyYdHOSGYE0', 'Audrey', 'Hum', 0, 0, '', 'Finance', 'VII', 'Cebu', 'Cebu', 26);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
