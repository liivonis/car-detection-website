-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: May 25, 2021 at 10:12 PM
-- Server version: 5.7.24
-- PHP Version: 7.2.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `car_detection`
--

-- --------------------------------------------------------

--
-- Table structure for table `car_count`
--

DROP TABLE IF EXISTS `car_count`;
CREATE TABLE IF NOT EXISTS `car_count` (
  `id` int(6) UNSIGNED NOT NULL AUTO_INCREMENT,
  `CarCount` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `videos`
--

DROP TABLE IF EXISTS `videos`;
CREATE TABLE IF NOT EXISTS `videos` (
  `id` int(6) UNSIGNED NOT NULL AUTO_INCREMENT,
  `VideoName` varchar(600) NOT NULL,
  `TimeStamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Stand-in structure for view `video_count`
-- (See below for the actual view)
--
DROP VIEW IF EXISTS `video_count`;
CREATE TABLE IF NOT EXISTS `video_count` (
`id` int(6) unsigned
,`VideoName` varchar(600)
,`CarCount` int(11)
,`TimeStamp` timestamp
);

-- --------------------------------------------------------

--
-- Stand-in structure for table `car_single_count`
--
CREATE TABLE IF NOT EXISTS `car_single_count` (
  `ID` int(6) UNSIGNED NOT NULL AUTO_INCREMENT,
  `Video_Name` VARCHAR(50),
  `Time_Stamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Car_Sequence_No` int(10),
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure for view `video_count`
--
DROP TABLE IF EXISTS `video_count`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `video_count`  AS  select `t2`.`id` AS `id`,`t2`.`VideoName` AS `VideoName`,`t1`.`CarCount` AS `CarCount`,`t2`.`TimeStamp` AS `TimeStamp` from (`car_count` `t1` join `videos` `t2` on((`t1`.`id` = `t2`.`id`))) ;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
