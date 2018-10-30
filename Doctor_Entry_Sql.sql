CREATE TABLE `doctor_details` (
  `D_ID` varchar(10) NOT NULL,
  `D_Name` char(25) NOT NULL,
  `D_Age` int(11) NOT NULL,
  `D_PNo` int(11) DEFAULT NULL,
  `D_Email` varchar(20) NOT NULL,
  `D_Add` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`D_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


INSERT INTO `db`.`doctor_details`
(`D_Age`,
`D_ID`,
`D_Name`,
`D_PNo`,
`D_Email`,
`D_Add`)
VALUES
#(
(45,'D_101','Prakhar',1234567890,'prakhar@yash.com','ABC'),
(30,'D_102','Shaney',1234567890,'shaney@yash.com','ABC'),
(55,'D_103','Snighda',1234567890,'snighda@yash.com','ABC'),
(32,'D_104','Bhaskar',1234567890,'bhaskar@yash.com','ABC'),
(44,'D_105','Manak',1234567890,'manak@yash.com','ABC'),
(44,'D_106','Anjali',1234567890,'anjali@yash.com','ABC'),
(33,'D_107','Neha',1234567890,'neha@yash.com','ABC'),
(33,'D_108','Sudhir',1234567890,'sudhir@yash.com','ABC'),
(55,'D_109','Aman',1234567890,'aman@yash.com','ABC'),
(39,'D_110','Chhavi',1234567890,'chhavi@yash.com','ABC'),
(45,'D_111','Vinod',1234567890,'vinod@yash.com','ABC'),
(30,'D_112','Vijay',1234567890,'vijay@yash.com','ABC'),
(55,'D_113','Viraj',1234567890,'viraj@yash.com','ABC'),
(32,'D_114','Vineet',1234567890,'vineet@yash.com','ABC'),
(44,'D_115','Mayank',1234567890,'mayank@yash.com','ABC'),
(44,'D_116','Shraddha',1234567890,'shraddha@yash.com','ABC')
;
#)
