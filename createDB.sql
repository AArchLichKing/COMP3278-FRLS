-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 06, 2021 at 05:52 AM
-- Server version: 8.0.23
-- PHP Version: 7.3.24-(to be removed in future macOS)

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `createDB`
--

-- --------------------------------------------------------

--
-- Table structure for table `Course`
--

CREATE TABLE `Course` (
  `course_id` int NOT NULL,
  `code` varchar(20) NOT NULL,
  `name` varchar(80) NOT NULL,
  `credit` int NOT NULL,
  `dept_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Course`
--

INSERT INTO `Course` (`course_id`, `code`, `name`, `credit`, `dept_id`) VALUES
(1, 'COMP3278', 'Introduction to database management systems', 6, 1),
(2, 'COMP3250', 'Design and Analysis of Algorithms', 6, 1),
(3, 'COMP3314', 'Machine Learning', 6, 1),
(4, 'STAT4601', 'Time-series analysis', 6, 2),
(5, 'STAT4602', 'Multivariate data analysis', 6, 2),
(6, 'STAT3621', 'Statistical data analysis', 6, 2),
(7, 'STAT3799', 'Directed studies in statistics', 6, 2),
(8, 'STAT4799', 'Statistics project', 12, 2),
(9, 'MATH3911', 'Game Theory and Strategy', 6, 3),
(10, 'STAT3600', 'Linear statistical analysis', 6, 2);

-- --------------------------------------------------------

--
-- Table structure for table `Department`
--

CREATE TABLE `Department` (
  `dept_id` int NOT NULL,
  `dept_name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Department`
--

INSERT INTO `Department` (`dept_id`, `dept_name`) VALUES
(1, 'Computer Science'),
(2, 'Statistics & Actuarial Science'),
(3, 'Mathematics'),
(4, 'HKU Business School');

-- --------------------------------------------------------

--
-- Table structure for table `Instructor`
--

CREATE TABLE `Instructor` (
  `instructor_id` int NOT NULL,
  `name` varchar(80) NOT NULL,
  `title` varchar(10) NOT NULL,
  `dept_id` int NOT NULL,
  `office` varchar(80) NOT NULL,
  `office_hour` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Instructor`
--

INSERT INTO `Instructor` (`instructor_id`, `name`, `title`, `dept_id`, `office`, `office_hour`) VALUES
(1, 'Luo Ping', 'Dr.', 1, 'CB 326', ''),
(2, 'Yu Yizhou', 'Prof.', 1, 'CB 325', 'Monday, 5:30 pm - 6:30 pm'),
(3, 'Huang Zhiyi', 'Dr. ', 1, 'CB 423', 'Tuesday, 4:00 pm - 5:00 pm'),
(4, 'Li Guodong', 'Dr.', 2, 'RRS 222', 'Friday,  2:30pm - 3:30pm'),
(5, 'Zhang Xiaoyu', 'Miss', 2, 'RRS 114', 'None'),
(7, 'Wu Jiannan', 'Mr', 1, 'None', 'None'),
(8, 'Zhang Yan, Dora', 'Dr. ', 2, 'RR 304', 'Friday, 1:30pm - 2:30pm'),
(9, 'Fang Yanwen', 'Miss', 2, 'RRS 112', 'None'),
(10, 'Law Ka Ho', 'Dr.', 3, 'RRS314', '');

-- --------------------------------------------------------

--
-- Table structure for table `Material`
--

CREATE TABLE `Material` (
  `course_id` int NOT NULL,
  `section_id` int NOT NULL,
  `material_id` int NOT NULL,
  `name` varchar(80) NOT NULL,
  `released_date` date NOT NULL,
  `link` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Material`
--

INSERT INTO `Material` (`course_id`, `section_id`, `material_id`, `name`, `released_date`, `link`) VALUES
(1, 1, 1, 'Lecture 2: ER model', '2021-02-01', 'https://drive.google.com/file/d/1qCF9CIfcNygJYUw3SFIJ2j6QavZxDjIp/view?usp=sharing'),
(1, 1, 2, 'Lecture 2: ER design', '2021-02-04', 'https://drive.google.com/file/d/101XCSb-KcsF6A72l67i4WRowhSrNZGR1/view?usp=sharing'),
(2, 1, 1, 'Lecture 6: Closest Pair', '2021-02-22', 'https://drive.google.com/file/d/14R5wo0G8VpjMJqTs0mkSeH-nTsFpqycZ/view?usp=sharing'),
(2, 2, 1, 'Lecture 1: Divide and Conquer 1', '2021-01-25', 'https://drive.google.com/file/d/1fipkHqRjY6lqYT6BYAaFifQyKcO3rhln/view?usp=sharing'),
(2, 2, 2, 'Lecture 2: Divide and Conquer 2', '2021-01-27', 'https://drive.google.com/file/d/1KNgR40D7ijOv51I3SBBXCu6eKSVmKYv8/view?usp=sharing'),
(3, 1, 1, 'Assignment 1', '2021-03-05', 'https://drive.google.com/file/d/1hbLduFgCxh5LAkhXBsFXWbpOzDqfn5xX/view?usp=sharing'),
(4, 1, 1, 'Assignment 3', '2021-03-12', 'https://drive.google.com/file/d/1mt_w27SktqDe3jkyDgzrf7vT4fi7kVyN/view?usp=sharing'),
(6, 2, 1, 'Tutorial 1', '2021-01-26', 'https://drive.google.com/file/d/1cFsyKtkH0olpdl3fs8Et3Isw6pSgRJ_P/view?usp=sharing');

-- --------------------------------------------------------

--
-- Table structure for table `Message`
--

CREATE TABLE `Message` (
  `course_id` int NOT NULL,
  `section_id` int NOT NULL,
  `message` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Message`
--

INSERT INTO `Message` (`course_id`, `section_id`, `message`, `time`) VALUES
(1, 1, 'New Assignment released', '2021-04-06 13:51:04');

-- --------------------------------------------------------

--
-- Table structure for table `Room`
--

CREATE TABLE `Room` (
  `room_id` int NOT NULL,
  `building_name` varchar(40) NOT NULL,
  `room_number` varchar(40) NOT NULL,
  `capacity` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Room`
--

INSERT INTO `Room` (`room_id`, `building_name`, `room_number`, `capacity`) VALUES
(1, 'online', 'online', 0),
(2, 'CPD', 'LG.10', 50),
(3, 'CYPP', '4', 200);

-- --------------------------------------------------------

--
-- Table structure for table `Section`
--

CREATE TABLE `Section` (
  `course_id` int NOT NULL,
  `section_id` int NOT NULL,
  `name` varchar(40) NOT NULL,
  `type` varchar(40) NOT NULL,
  `zoom_link` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Section`
--

INSERT INTO `Section` (`course_id`, `section_id`, `name`, `type`, `zoom_link`) VALUES
(1, 1, 'COMP3278 2B, 2020', 'Lecture', 'https://hku.zoom.us/j/97686555806?pwd=NWxSNVRKTlNDU0NjYTgremxaQ3pldz09'),
(1, 2, 'COMP3278 Tutorial, 2020 ', 'Tutorial', 'https://hku.zoom.com.cn/j/2640918958?pwd=UmFpek1YMkUzNTFoL0ljRW84M1VLUT09'),
(2, 1, 'COMP3250 2A, 2020', 'Lecture', 'https://hku.zoom.us/j/95975951415?pwd=QWRVYThOU1BFZTJRN08wVFVHUEJ4dz09'),
(2, 2, 'COMP3250 2B, 2020', 'Lecture', 'https://hku.zoom.us/j/98446009822?pwd=YWlLOFplRUowMGZCSlplSWRwRTlIdz09'),
(3, 1, 'COMP3314 2A, 2020', 'Lecture', 'https://hku.zoom.us/j/92125651881?pwd=Q0t2WTdrc1ZTMnVOTVAyak82bmpGdz09'),
(4, 1, 'STAT4601 2A, 2020', 'Lecture', 'https://hku.zoom.us/j/92595211727?pwd=am8rR0NucGFWb2RndGZ3RFB0NVFBZz09'),
(4, 2, 'STAT4601 2A Tutorial 1, 2020', 'Tutorial', 'https://hku.zoom.us/j/93339305994?pwd=cDZ3MnNycDFnQmdFN05tTkNmck52QT09'),
(4, 3, 'STAT4601 2A Tutorial 2, 2020', 'Tutorial', 'https://hku.zoom.com.cn/j/3916015671'),
(6, 1, 'STAT3621 2A, 2020', 'lecture', 'https://hku.zoom.us/j/99199478092?pwd=SmZ3UFFvSkJvWEh3aUxYaTNYdGJBZz09'),
(9, 1, 'MATH3911 2A, 2020', 'Lecture', ''),
(10, 1, 'STAT3600 2B, 2019', 'Lecture', ''),
(10, 2, 'STAT3600 2B Tutorial, 2019', 'Tutorial', '');

-- --------------------------------------------------------

--
-- Table structure for table `Student`
--

CREATE TABLE `Student` (
  `student_id` varchar(10) NOT NULL,
  `info.name` varchar(80) NOT NULL,
  `info.email_addr` varchar(80) NOT NULL,
  `info.admitted_year` int NOT NULL,
  `info.dept_id` int NOT NULL,
  `last_login` timestamp NOT NULL,
  `last_logout` timestamp NOT NULL,
  `duration` time NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Student`
--

INSERT INTO `Student` (`student_id`, `info.name`, `info.email_addr`, `info.admitted_year`, `info.dept_id`, `last_login`, `last_logout`, `duration`, `password`) VALUES
('1', 'Chen Kangyi', 'ckykevin@connect.hku.hk', 2017, 4, '2021-03-18 03:32:07', '2021-03-22 03:32:07', '11:32:07', '123456'),
('2', 'Du Zhixu', '', 2017, 3, '2021-03-16 05:05:34', '2021-03-26 02:05:34', '13:05:23', '123456'),
('3', 'Feng Yueman', '', 2017, 2, '2021-03-25 05:05:34', '2021-03-22 05:05:34', '16:05:34', '123456'),
('4', 'Tang Yudan', 'tangyd@connect.hku.hk', 2018, 2, '2021-03-21 07:00:00', '2021-01-02 04:22:01', '04:05:01', '123456'),
('5', 'Zhang Maoqi', 'maoqi@connect.hku.hk', 2018, 3, '2021-03-14 03:32:07', '2021-03-15 03:32:07', '12:32:07', '123456');

-- --------------------------------------------------------

--
-- Table structure for table `Take`
--

CREATE TABLE `Take` (
  `student_id` varchar(10) NOT NULL,
  `course_id` int NOT NULL,
  `section_id` int NOT NULL,
  `this_sem` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Take`
--

INSERT INTO `Take` (`student_id`, `course_id`, `section_id`, `this_sem`) VALUES
('1', 2, 1, 1),
('4', 1, 1, 1),
('4', 1, 2, 1),
('4', 2, 2, 1),
('4', 3, 1, 1),
('4', 4, 1, 1),
('4', 4, 2, 1),
('4', 4, 3, 1),
('4', 6, 1, 1),
('4', 10, 1, 0),
('5', 9, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `Teach`
--

CREATE TABLE `Teach` (
  `instructor_id` int NOT NULL,
  `course_id` int NOT NULL,
  `section_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Teach`
--

INSERT INTO `Teach` (`instructor_id`, `course_id`, `section_id`) VALUES
(1, 1, 1),
(2, 3, 1),
(3, 2, 1),
(4, 4, 1),
(4, 10, 1),
(5, 4, 2),
(7, 1, 2),
(8, 6, 1),
(9, 10, 2),
(10, 9, 1);

-- --------------------------------------------------------

--
-- Table structure for table `Time`
--

CREATE TABLE `Time` (
  `course_id` int NOT NULL,
  `section_id` int NOT NULL,
  `time_id` int NOT NULL,
  `weekday` varchar(10) NOT NULL,
  `start_time` time NOT NULL,
  `end_time` time NOT NULL,
  `duration` time NOT NULL,
  `room_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Time`
--

INSERT INTO `Time` (`course_id`, `section_id`, `time_id`, `weekday`, `start_time`, `end_time`, `duration`, `room_id`) VALUES
(1, 1, 1, 'FRI', '09:30:00', '12:20:00', '01:50:00', 1),
(1, 2, 1, 'TUE', '09:30:00', '10:20:00', '00:50:00', 1),
(2, 1, 1, 'TUE', '12:30:00', '13:20:00', '00:50:00', 2),
(2, 1, 2, 'FRI', '12:30:00', '14:20:00', '01:50:00', 1),
(2, 2, 1, 'TUE', '12:30:00', '13:20:00', '00:50:00', 1),
(2, 2, 2, 'FRI', '12:30:00', '14:20:00', '01:50:00', 1),
(3, 1, 1, 'MON', '14:30:00', '17:20:00', '02:50:00', 1),
(4, 1, 1, 'TUE', '13:30:00', '16:20:00', '02:50:00', 1),
(6, 1, 1, 'MON', '09:30:00', '12:20:00', '02:50:00', 3);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Course`
--
ALTER TABLE `Course`
  ADD PRIMARY KEY (`course_id`);

--
-- Indexes for table `Department`
--
ALTER TABLE `Department`
  ADD PRIMARY KEY (`dept_id`);

--
-- Indexes for table `Instructor`
--
ALTER TABLE `Instructor`
  ADD PRIMARY KEY (`instructor_id`);

--
-- Indexes for table `Material`
--
ALTER TABLE `Material`
  ADD PRIMARY KEY (`course_id`,`section_id`,`material_id`);

--
-- Indexes for table `Room`
--
ALTER TABLE `Room`
  ADD PRIMARY KEY (`room_id`);

--
-- Indexes for table `Section`
--
ALTER TABLE `Section`
  ADD PRIMARY KEY (`course_id`,`section_id`);

--
-- Indexes for table `Student`
--
ALTER TABLE `Student`
  ADD PRIMARY KEY (`student_id`);

--
-- Indexes for table `Take`
--
ALTER TABLE `Take`
  ADD PRIMARY KEY (`student_id`,`course_id`,`section_id`);

--
-- Indexes for table `Teach`
--
ALTER TABLE `Teach`
  ADD PRIMARY KEY (`instructor_id`,`course_id`,`section_id`);

--
-- Indexes for table `Time`
--
ALTER TABLE `Time`
  ADD PRIMARY KEY (`course_id`,`section_id`,`time_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
