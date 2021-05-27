-- phpMyAdmin SQL Dump
-- version 4.8.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 20, 2020 at 05:14 PM
-- Server version: 10.1.33-MariaDB
-- PHP Version: 7.2.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "-05:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Course_Management`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `admin_id` int(11) NOT NULL,
  `username` varchar(30) NOT NULL,
  `name` text NOT NULL,
  `password` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`admin_id`, `username`, `name`, `password`) VALUES
(1, 'jude', 'Angel Jude Suarez', 'admin'),
(13, 'jeff', 'Jeff Clint', 'pizza');

-- --------------------------------------------------------

--
-- Table structure for table `Course`
--

CREATE TABLE `course` (
  `course_id` int(11) NOT NULL,
  `course_name` varchar(300) NOT NULL,
  `admin_id` int(11) NOT NULL,
  `day` varchar(30) NOT NULL,
  `time` time NOT NULL,
  `building` varchar(100) NOT NULL,
  `room` varchar(30) NOT NULL,
  `semester` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `course`
--

INSERT INTO `course` (`course_id`, `course_name`, `admin_id`, `day`, `time`, `building`, `room`, `semester`) VALUES
(2, 'Python Programming', 1, 'Thursdays', '15:00', 'S.R Collins', '223', 'Fall');

-- --------------------------------------------------------

--
-- Table structure for table `issue_course`
--

CREATE TABLE `issue_course` (
  `course_id` int(11) NOT NULL,
  `stud_id` int(11) NOT NULL,
  `issue_date` DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `issue_course`
--

INSERT INTO `issue_course` (`course_id`, `stud_id`) VALUES
(2, 2),
(2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `stud_id` int(11) NOT NULL,
  `name` varchar(300) NOT NULL,
  `phone_number` varchar(30) NOT NULL,
  `address` text NOT NULL,
  `password` text NOT NULL,
  `admission_date` DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`stud_id`, `name`, `phone_number`, `address`, `password`) VALUES
(1, 'angel jude suarez', '09125113555', 'Himamaylan City', 'angel21'),
(2, 'adrian mercurio', '09123456789', 'Brgy. suay Himamaylan city', 'admerc345'),
(3, 'Ricardo Dalisay', '09123456789', 'Manila Philippines', 'daisytin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`admin_id`);

--
-- Indexes for table `course`
--
ALTER TABLE `course`
  ADD PRIMARY KEY (`course_id`);


--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`stud_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `admin_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `book`
--
ALTER TABLE `course`
  MODIFY `course_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12312312;

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `stud_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

SET foreign_key_checks = 0;
ALTER TABLE issue_course ADD FOREIGN KEY (course_id) REFERENCES course(course_id);
ALTER TABLE issue_course ADD FOREIGN KEY (stud_id) REFERENCES student(stud_id);
ALTER TABLE course ADD FOREIGN KEY (admin_id) REFERENCES admin(admin_id);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
