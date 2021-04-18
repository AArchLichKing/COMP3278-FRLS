-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- 主机： localhost
-- 生成日期： 2021-04-18 09:48:32
-- 服务器版本： 8.0.23
-- PHP 版本： 7.3.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `db`
--

-- --------------------------------------------------------

--
-- 表的结构 `Course`
--

CREATE TABLE `Course` (
  `course_id` int NOT NULL,
  `code` varchar(20) NOT NULL,
  `name` varchar(80) NOT NULL,
  `credit` int NOT NULL,
  `dept_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `Course`
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
(10, 'STAT3600', 'Linear statistical analysis', 6, 2),
(11, 'ECON4200', 'Senior Seminar in Economics and Finance', 6, 4),
(12, 'ECON3283', 'Economic Forecasting', 6, 4),
(13, 'ECON3284', 'Introduction to Causal Inference and Statistical Learning', 6, 4),
(14, 'MATH4602', 'Scientific computing', 6, 3),
(15, 'MATH2102', 'Linear algebra II', 6, 3),
(16, 'CCHU9051', 'Mysteries of the Human Mind', 6, 9),
(17, 'CHEM1043', 'General chemistry II', 6, 5),
(18, 'BIOL3404', 'Protein structure and function', 6, 6),
(19, 'BIOC3605', 'Sequence bioinformatics', 6, 6),
(20, 'CCHU9045', 'The Science and Art of Perception', 6, 7),
(21, 'CCHU9021', 'Critical Thinking in Contemporary Society', 6, 9),
(22, 'CCGL9035', 'Challenges of Global Governance: Past and Present', 6, 10);

-- --------------------------------------------------------

--
-- 表的结构 `deadline`
--

CREATE TABLE `deadline` (
  `course_id` int NOT NULL,
  `section_id` int NOT NULL,
  `ddl_id` int NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `event` varchar(160) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `deadline`
--

INSERT INTO `deadline` (`course_id`, `section_id`, `ddl_id`, `date`, `time`, `event`) VALUES
(1, 1, 1, '2021-04-19', '23:59:59', '3-page presentation slides'),
(2, 1, 1, '2021-04-27', '21:00:00', 'Model presentation'),
(9, 1, 1, '2021-04-24', '23:59:59', 'Final presentation '),
(11, 1, 1, '2021-04-30', '23:59:59', 'Paper submission'),
(14, 1, 1, '2021-04-21', '23:59:59', 'Assignment 7'),
(15, 1, 1, '2021-04-22', '12:00:00', 'Homework 5');

-- --------------------------------------------------------

--
-- 表的结构 `Department`
--

CREATE TABLE `Department` (
  `dept_id` int NOT NULL,
  `dept_name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `Department`
--

INSERT INTO `Department` (`dept_id`, `dept_name`) VALUES
(1, 'Computer Science'),
(2, 'Statistics & Actuarial Science'),
(3, 'Mathematics'),
(4, 'HKU Business School'),
(5, 'Chemistry'),
(6, 'Biomedical Sciences'),
(7, 'Paediatrics and Adolescent Medicine'),
(8, 'Ophthalmology'),
(9, 'Philosophy'),
(10, 'Politics and Public Administration');

-- --------------------------------------------------------

--
-- 表的结构 `Instructor`
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
-- 转存表中的数据 `Instructor`
--

INSERT INTO `Instructor` (`instructor_id`, `name`, `title`, `dept_id`, `office`, `office_hour`) VALUES
(1, 'Luo Ping', 'Dr.', 1, 'CB 326', ''),
(2, 'Yu Yizhou', 'Prof.', 1, 'CB 325', 'Monday, 5:30 pm - 6:30 pm'),
(3, 'Huang Zhiyi', 'Dr. ', 1, 'CB 423', 'Tuesday, 4:00 pm - 5:00 pm'),
(4, 'Li Guodong', 'Dr.', 2, 'RRS 222', 'Friday,  2:30pm - 3:30pm'),
(5, 'Zhang Xiaoyu', 'Miss', 2, 'RRS 114', ''),
(7, 'Wu Jiannan', 'Mr', 1, 'None', ''),
(8, 'Zhang Yan, Dora', 'Dr. ', 2, 'RRS 304', 'Friday, 1:30pm - 2:30pm'),
(9, 'Fang Yanwen', 'Miss', 2, 'RRS 112', ''),
(10, 'Law Ka Ho', 'Dr.', 3, 'RRS 314', ''),
(11, 'LIU Tingjun', 'Prof.', 4, 'KK 1002', ''),
(12, 'Maurice K.S. TSE', 'Dr.', 4, 'KK 919', ''),
(13, 'CHING Wai-Ki', 'Prof.', 3, 'RRS 414', ''),
(14, 'CHING Tak Wing ', 'Dr.', 3, 'RRS 316', ''),
(15, 'Li Wentao', 'Dr. ', 2, 'RRS 118', ''),
(16, 'HO, Joshua Wing Kei', 'Dr. ', 6, 'LB 444', ''),
(17, 'YAO Kwok Ming', 'Dr.', 6, 'LB 369', ''),
(18, 'TONG, Angela Pui Ling', 'Dr. ', 5, 'CYC 602', ''),
(19, 'Chan, Godfrey Chi-Fung ', 'Prof.', 7, 'NCB 102', ''),
(20, 'Amit Chaturvedi', 'Dr.', 9, 'RRST 1009', ''),
(21, 'CHOW Wilfred', 'Dr.', 10, 'C 945', ''),
(22, 'Alexandra Cook', 'Prof.', 9, 'RRST 1004', ''),
(23, 'Wu Yanhui', 'Dr.', 4, 'KK 931', '');

-- --------------------------------------------------------

--
-- 表的结构 `Material`
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
-- 转存表中的数据 `Material`
--

INSERT INTO `Material` (`course_id`, `section_id`, `material_id`, `name`, `released_date`, `link`) VALUES
(1, 1, 1, 'Lecture 2: ER model', '2021-02-01', 'https://drive.google.com/file/d/1qCF9CIfcNygJYUw3SFIJ2j6QavZxDjIp/view?usp=sharing'),
(1, 1, 2, 'Lecture 2: ER design', '2021-02-04', 'https://drive.google.com/file/d/101XCSb-KcsF6A72l67i4WRowhSrNZGR1/view?usp=sharing'),
(1, 1, 3, 'Assignment 2: Relational Algebra', '2021-04-01', 'https://drive.google.com/drive/folders/1Fk2l5mSrYdNU1aGNIE_dFxgq0ll37Dd_?usp=sharing'),
(1, 2, 1, 'tutorial files', '2021-04-07', 'https://drive.google.com/drive/u/0/folders/1K9MPFTDDOvcQiGXiKBMgr_xeM56cvrP5'),
(2, 1, 1, 'Lecture 6: Closest Pair', '2021-02-22', 'https://drive.google.com/file/d/14R5wo0G8VpjMJqTs0mkSeH-nTsFpqycZ/view?usp=sharing'),
(2, 2, 1, 'Lecture 1: Divide and Conquer 1', '2021-01-25', 'https://drive.google.com/file/d/1fipkHqRjY6lqYT6BYAaFifQyKcO3rhln/view?usp=sharing'),
(2, 2, 2, 'Lecture 2: Divide and Conquer 2', '2021-01-27', 'https://drive.google.com/file/d/1KNgR40D7ijOv51I3SBBXCu6eKSVmKYv8/view?usp=sharing'),
(3, 1, 1, 'Assignment 1', '2021-03-05', 'https://drive.google.com/file/d/1hbLduFgCxh5LAkhXBsFXWbpOzDqfn5xX/view?usp=sharing'),
(4, 1, 1, 'Assignment 3', '2021-03-12', 'https://drive.google.com/file/d/1mt_w27SktqDe3jkyDgzrf7vT4fi7kVyN/view?usp=sharing'),
(6, 2, 1, 'Tutorial 1', '2021-01-26', 'https://drive.google.com/file/d/1cFsyKtkH0olpdl3fs8Et3Isw6pSgRJ_P/view?usp=sharing');

-- --------------------------------------------------------

--
-- 表的结构 `Message`
--

CREATE TABLE `Message` (
  `course_id` int NOT NULL,
  `section_id` int NOT NULL,
  `message` varchar(160) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `Message`
--

INSERT INTO `Message` (`course_id`, `section_id`, `message`, `time`) VALUES
(1, 1, 'New Assignment released', '2021-04-06 13:51:04'),
(1, 2, 'Tutorial material uploaded', '2021-04-19 11:49:45'),
(4, 1, 'Register Olex system by 16/04', '2021-04-16 11:49:34'),
(15, 1, 'Test 1 result released', '2021-04-16 11:49:34');

-- --------------------------------------------------------

--
-- 表的结构 `Room`
--

CREATE TABLE `Room` (
  `room_id` int NOT NULL,
  `building_name` varchar(40) NOT NULL,
  `room_number` varchar(40) NOT NULL,
  `capacity` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `Room`
--

INSERT INTO `Room` (`room_id`, `building_name`, `room_number`, `capacity`) VALUES
(1, 'online', 'online', 999),
(2, 'CPD', 'LG.10', 50),
(3, 'CYPP', '4', 200),
(4, 'JL', 'G01', 50),
(5, 'JL', 'G05', 60),
(6, 'LE', '5', 100),
(7, 'KB', '223', 200),
(8, 'CPD', 'LG.01', 300),
(9, 'KK', '201', 80),
(10, 'TT', '403', 90);

-- --------------------------------------------------------

--
-- 表的结构 `Section`
--

CREATE TABLE `Section` (
  `course_id` int NOT NULL,
  `section_id` int NOT NULL,
  `name` varchar(40) NOT NULL,
  `type` varchar(40) NOT NULL,
  `zoom_link` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `Section`
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
(6, 2, 'STAT3621 2A Tutorial, 2020', 'Tutorial', ''),
(7, 1, 'STAT3799 2A, 2020', 'Meeting', 'https://hku.zoom.us/j/98577457215?pwd=ODNmY1VpcmY3WWYyUWNkN0w0Rnp1Zz09'),
(9, 1, 'MATH3911 2A, 2020', 'Lecture', ''),
(9, 2, 'MATH3911 2A Tutorial, 2020', 'Tutorial', ''),
(10, 1, 'STAT3600 2B, 2019', 'Lecture', ''),
(10, 2, 'STAT3600 2B Tutorial, 2019', 'Tutorial', ''),
(10, 3, 'STAT3600 2B, 2020', 'Lecture', ''),
(11, 1, 'ECON4200 2I, 2020', 'Lecture', ''),
(12, 1, 'ECON3283 2A, 2020', 'Lecture', ''),
(13, 1, 'ECON3284 2A, 2020', 'Lecture', ''),
(14, 1, 'MATH4602 2A, 2020', 'Lecture', ''),
(15, 1, 'MATH2102 2A, 2020', 'Lecture', ''),
(15, 2, 'MATH2102 2A Tutorial, 2020', 'Tutorial', ''),
(16, 1, 'CCHU9051 2A, 2020', 'Lecture', ''),
(16, 2, 'CCHU9051 2A Tutorial, 2020', 'Tutorial', ''),
(17, 1, 'CHEM1043 2B, 2020', 'Lecture', ''),
(18, 1, 'BIOL3404 2A', 'Lecture', ''),
(19, 1, 'BIOC3605 2A, 2020', 'Lecture', ''),
(20, 1, 'CCHU9045 2B, 2020', 'Lecture', ''),
(21, 1, 'CCHU9021 2B, 2020', 'Lecture', ''),
(21, 2, 'CCHU9021 2B Tutorial, 2020', 'Tutorial', ''),
(22, 1, 'CCGL9035 2A, 2020', 'Lecture', ''),
(22, 2, 'CCGL9035 2A Tutorial, 2020', 'Tutorial', '');

-- --------------------------------------------------------

--
-- 表的结构 `Student`
--

CREATE TABLE `Student` (
  `student_id` varchar(10) NOT NULL,
  `info.name` varchar(80) NOT NULL,
  `info.email_addr` varchar(80) NOT NULL,
  `info.admitted_year` int NOT NULL,
  `info.dept_id` int NOT NULL,
  `duration` time NOT NULL DEFAULT '00:00:00',
  `password` varchar(20) NOT NULL,
  `login.date` date DEFAULT NULL,
  `login.time` time DEFAULT NULL,
  `logout.date` date DEFAULT NULL,
  `logout.time` time DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `Student`
--

INSERT INTO `Student` (`student_id`, `info.name`, `info.email_addr`, `info.admitted_year`, `info.dept_id`, `duration`, `password`, `login.date`, `login.time`, `logout.date`, `logout.time`) VALUES
('1', 'Chen Kangyi', 'ckykevin@connect.hku.hk', 2017, 4, '11:32:07', '123456', '2021-04-18', '15:53:47', '2021-04-05', '15:49:02'),
('2', 'Du Zhixu', '', 2017, 3, '13:05:23', '123456', '2021-04-01', '15:48:24', '2021-04-05', '15:49:06'),
('3', 'Feng Yueman', '', 2017, 2, '16:05:34', '123456', '2021-04-01', '15:48:28', '2021-04-05', '15:49:13'),
('4', 'Tang Yudan', 'tangyd@connect.hku.hk', 2018, 2, '04:05:01', '123456', '2021-04-01', '15:48:31', '2021-04-05', '15:49:18'),
('5', 'Zhang Maoqi', 'maoqi@connect.hku.hk', 2018, 3, '12:32:07', '123456', '2021-04-01', '15:48:35', '2021-04-05', '15:49:22');

-- --------------------------------------------------------

--
-- 表的结构 `Take`
--

CREATE TABLE `Take` (
  `student_id` varchar(10) NOT NULL,
  `course_id` int NOT NULL,
  `section_id` int NOT NULL,
  `this_sem` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `Take`
--

INSERT INTO `Take` (`student_id`, `course_id`, `section_id`, `this_sem`) VALUES
('1', 1, 1, 1),
('1', 1, 2, 1),
('1', 2, 1, 1),
('1', 3, 1, 1),
('1', 11, 1, 1),
('1', 12, 1, 1),
('1', 13, 1, 1),
('2', 16, 1, 1),
('2', 16, 2, 1),
('2', 21, 1, 1),
('2', 21, 2, 1),
('2', 22, 1, 1),
('2', 22, 2, 1),
('3', 1, 1, 1),
('3', 1, 2, 1),
('3', 4, 1, 1),
('3', 4, 3, 1),
('3', 17, 1, 1),
('3', 18, 1, 1),
('3', 19, 1, 1),
('3', 20, 1, 1),
('4', 1, 1, 1),
('4', 1, 2, 1),
('4', 2, 1, 1),
('4', 3, 1, 1),
('4', 4, 1, 1),
('4', 4, 2, 1),
('4', 6, 1, 1),
('4', 7, 1, 1),
('4', 10, 1, 0),
('5', 1, 1, 1),
('5', 1, 2, 1),
('5', 9, 1, 1),
('5', 9, 2, 1),
('5', 10, 3, 1),
('5', 14, 1, 1),
('5', 15, 1, 1),
('5', 15, 2, 1);

-- --------------------------------------------------------

--
-- 表的结构 `Teach`
--

CREATE TABLE `Teach` (
  `instructor_id` int NOT NULL,
  `course_id` int NOT NULL,
  `section_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `Teach`
--

INSERT INTO `Teach` (`instructor_id`, `course_id`, `section_id`) VALUES
(1, 1, 1),
(7, 1, 2),
(3, 2, 1),
(2, 3, 1),
(4, 4, 1),
(5, 4, 2),
(8, 6, 1),
(15, 7, 1),
(10, 9, 1),
(10, 9, 2),
(4, 10, 1),
(9, 10, 2),
(15, 10, 3),
(11, 11, 1),
(12, 12, 1),
(23, 13, 1),
(13, 14, 1),
(14, 15, 1),
(14, 15, 2),
(20, 16, 1),
(20, 16, 2),
(18, 17, 1),
(17, 18, 1),
(16, 19, 1),
(19, 20, 1),
(22, 21, 1),
(22, 21, 2),
(21, 22, 1),
(21, 22, 2);

-- --------------------------------------------------------

--
-- 表的结构 `Time`
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
-- 转存表中的数据 `Time`
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
(4, 2, 1, 'WED', '11:30:00', '12:20:00', '00:50:00', 1),
(4, 3, 1, 'WED', '11:30:00', '12:20:00', '00:50:00', 1),
(6, 1, 1, 'MON', '09:30:00', '12:20:00', '02:50:00', 3),
(7, 1, 1, 'TUE', '17:00:00', '18:00:00', '01:00:00', 1),
(9, 1, 1, 'TUE', '10:30:00', '12:20:00', '01:50:00', 6),
(9, 1, 2, 'FRI', '11:30:00', '12:20:00', '00:50:00', 6),
(9, 2, 1, 'THU', '17:30:00', '18:20:00', '00:50:00', 5),
(10, 3, 1, 'FRI', '14:30:00', '17:20:00', '02:50:00', 7),
(11, 1, 1, 'TUE', '13:30:00', '16:20:00', '02:50:00', 9),
(12, 1, 1, 'WED', '09:30:00', '12:20:00', '02:50:00', 10),
(13, 1, 1, 'THU', '13:30:00', '16:20:00', '02:50:00', 6),
(14, 1, 1, 'MON', '09:30:00', '11:20:00', '01:50:00', 4),
(14, 1, 2, 'FRI', '12:30:00', '13:20:00', '00:50:00', 4),
(14, 1, 3, 'THU', '09:30:00', '10:20:00', '00:50:00', 4),
(15, 1, 1, 'MON', '14:30:00', '15:20:00', '00:50:00', 5),
(15, 1, 2, 'THU', '13:30:00', '15:20:00', '01:50:00', 5),
(15, 2, 1, 'THU', '10:30:00', '11:20:00', '00:50:00', 5),
(16, 1, 1, 'WED', '18:30:00', '20:20:00', '01:50:00', 1),
(16, 2, 1, 'MON', '14:30:00', '15:20:00', '00:50:00', 1),
(17, 1, 1, 'MON', '15:30:00', '17:20:00', '01:50:00', 1),
(17, 1, 2, 'THU', '15:30:00', '16:20:00', '00:50:00', 1),
(18, 1, 1, 'TUE', '10:30:00', '12:20:00', '01:50:00', 1),
(18, 1, 2, 'FRI', '11:30:00', '12:20:00', '00:50:00', 1),
(19, 1, 1, 'TUE', '12:30:00', '13:20:00', '00:50:00', 1),
(19, 1, 2, 'FRI', '12:30:00', '14:20:00', '01:50:00', 1),
(20, 1, 1, 'WED', '16:30:00', '18:20:00', '01:50:00', 8),
(21, 1, 1, 'WED', '14:30:00', '16:20:00', '01:50:00', 1),
(21, 2, 1, 'MON', '15:30:00', '16:20:00', '00:50:00', 1),
(22, 1, 1, 'WED', '12:30:00', '14:20:00', '01:50:00', 1),
(22, 2, 1, 'TUE', '16:30:00', '17:20:00', '00:50:00', 1);

--
-- 转储表的索引
--

--
-- 表的索引 `Course`
--
ALTER TABLE `Course`
  ADD PRIMARY KEY (`course_id`),
  ADD KEY `dept_id_2` (`dept_id`);

--
-- 表的索引 `deadline`
--
ALTER TABLE `deadline`
  ADD PRIMARY KEY (`course_id`,`section_id`,`ddl_id`);

--
-- 表的索引 `Department`
--
ALTER TABLE `Department`
  ADD PRIMARY KEY (`dept_id`);

--
-- 表的索引 `Instructor`
--
ALTER TABLE `Instructor`
  ADD PRIMARY KEY (`instructor_id`),
  ADD KEY `dept_id` (`dept_id`);

--
-- 表的索引 `Material`
--
ALTER TABLE `Material`
  ADD PRIMARY KEY (`course_id`,`section_id`,`material_id`);

--
-- 表的索引 `Message`
--
ALTER TABLE `Message`
  ADD PRIMARY KEY (`course_id`,`section_id`,`message`);

--
-- 表的索引 `Room`
--
ALTER TABLE `Room`
  ADD PRIMARY KEY (`room_id`);

--
-- 表的索引 `Section`
--
ALTER TABLE `Section`
  ADD PRIMARY KEY (`course_id`,`section_id`);

--
-- 表的索引 `Student`
--
ALTER TABLE `Student`
  ADD PRIMARY KEY (`student_id`),
  ADD KEY `info.dept_id` (`info.dept_id`);

--
-- 表的索引 `Take`
--
ALTER TABLE `Take`
  ADD PRIMARY KEY (`student_id`,`course_id`,`section_id`),
  ADD KEY `course_id` (`course_id`,`section_id`);

--
-- 表的索引 `Teach`
--
ALTER TABLE `Teach`
  ADD PRIMARY KEY (`instructor_id`,`course_id`,`section_id`),
  ADD KEY `teach_ibfk_2` (`course_id`,`section_id`);

--
-- 表的索引 `Time`
--
ALTER TABLE `Time`
  ADD PRIMARY KEY (`course_id`,`section_id`,`time_id`),
  ADD KEY `room_id` (`room_id`);

--
-- 限制导出的表
--

--
-- 限制表 `Course`
--
ALTER TABLE `Course`
  ADD CONSTRAINT `course_ibfk_1` FOREIGN KEY (`dept_id`) REFERENCES `Department` (`dept_id`);

--
-- 限制表 `deadline`
--
ALTER TABLE `deadline`
  ADD CONSTRAINT `deadline_ibfk_1` FOREIGN KEY (`course_id`,`section_id`) REFERENCES `Section` (`course_id`, `section_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- 限制表 `Instructor`
--
ALTER TABLE `Instructor`
  ADD CONSTRAINT `instructor_ibfk_1` FOREIGN KEY (`dept_id`) REFERENCES `Department` (`dept_id`);

--
-- 限制表 `Material`
--
ALTER TABLE `Material`
  ADD CONSTRAINT `material_ibfk_1` FOREIGN KEY (`course_id`,`section_id`) REFERENCES `Section` (`course_id`, `section_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- 限制表 `Message`
--
ALTER TABLE `Message`
  ADD CONSTRAINT `message_ibfk_1` FOREIGN KEY (`course_id`,`section_id`) REFERENCES `Section` (`course_id`, `section_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- 限制表 `Section`
--
ALTER TABLE `Section`
  ADD CONSTRAINT `section_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `Course` (`course_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- 限制表 `Student`
--
ALTER TABLE `Student`
  ADD CONSTRAINT `student_ibfk_1` FOREIGN KEY (`info.dept_id`) REFERENCES `Department` (`dept_id`);

--
-- 限制表 `Take`
--
ALTER TABLE `Take`
  ADD CONSTRAINT `take_ibfk_1` FOREIGN KEY (`course_id`,`section_id`) REFERENCES `Section` (`course_id`, `section_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `take_ibfk_2` FOREIGN KEY (`student_id`) REFERENCES `Student` (`student_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- 限制表 `Teach`
--
ALTER TABLE `Teach`
  ADD CONSTRAINT `teach_ibfk_1` FOREIGN KEY (`instructor_id`) REFERENCES `Instructor` (`instructor_id`),
  ADD CONSTRAINT `teach_ibfk_2` FOREIGN KEY (`course_id`,`section_id`) REFERENCES `Section` (`course_id`, `section_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- 限制表 `Time`
--
ALTER TABLE `Time`
  ADD CONSTRAINT `time_ibfk_1` FOREIGN KEY (`course_id`,`section_id`) REFERENCES `Section` (`course_id`, `section_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `time_ibfk_2` FOREIGN KEY (`room_id`) REFERENCES `Room` (`room_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
