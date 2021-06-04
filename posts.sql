-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 04, 2021 at 09:27 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
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
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `id` bigint(20) NOT NULL,
  `yearsOfExperience` int(11) NOT NULL,
  `industry` varchar(100) NOT NULL,
  `region` varchar(100) NOT NULL,
  `province` varchar(100) NOT NULL,
  `city` varchar(100) NOT NULL,
  `age` int(11) NOT NULL,
  `dateadded` date NOT NULL,
  `email` varchar(100) NOT NULL,
  `isAgeViewable` int(11) NOT NULL,
  `firstname` varchar(100) NOT NULL,
  `lastname` varchar(100) NOT NULL,
  `position` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`id`, `yearsOfExperience`, `industry`, `region`, `province`, `city`, `age`, `dateadded`, `email`, `isAgeViewable`, `firstname`, `lastname`, `position`) VALUES
(3, 0, 'Technology', 'VII', 'Cebu', 'Cebu City', 22, '2021-06-05', 'g@g.com', 0, 'Gene Paul', 'Zafra', 'Software Dev Assoc'),
(4, 0, 'Entertainment', 'VII', 'Cebu', 'Lapu-Lapu', 32, '2021-06-05', 'monty123@email.com', 0, 'Monty', 'Python', 'Macho Dancer'),
(5, 0, 'Computer', 'VII', 'Cebu', 'Cebu', 25, '2021-06-05', 'janfrancis@email.com', 0, 'Jan', 'Arzadon', 'Bantay Internetan'),
(6, 0, 'Finance', 'VII', 'Cebu', 'Lapu-Lapu', 30, '2021-06-05', 'zackhilacan@email.com', 0, 'Zack', 'Hilacan', 'Corrupt Official'),
(7, 1, 'Computer', 'VII', 'Cebu', 'Mandaue', 26, '2021-06-05', 'genezaf@email.com', 0, 'Gene', 'Zafra', 'Bantay Internetan'),
(8, 0, 'Music', 'VII', 'Cebu', 'Talisay', 26, '2021-06-05', 'nawit@email.com', 0, 'Nathan', 'Awit', 'Singer'),
(9, 0, 'Manufacturing', 'VII', 'Cebu', 'Danao', 34, '2021-06-05', 'ajcabaron@email.com', 0, 'Adrien', 'Cabaron', 'Blacksmith');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
