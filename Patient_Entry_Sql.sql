CREATE TABLE `patient_details` (
  `P_ID` varchar(45) NOT NULL,
  `P_Name` varchar(45) NOT NULL,
  `P_Age` int(11) NOT NULL,
  `P_PNo` double DEFAULT NULL,
  `P_Add` varchar(45) DEFAULT NULL,
  `P_Email` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`P_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;




INSERT INTO `db`.`patient_details`
(`P_Age`,
`P_ID`,
`P_Name`,
`P_PNo`,
`P_Add`)
VALUES
#(
(19,'P_101','Abhishek',1234567890,'ABC'),
(20,'P_102','Anuj',1234567890,'ABC'),
(17,'P_103','Bhavam',1234567890,'ABC'),
(16,'P_104','Hrithik',1234567890,'ABC'),
(20,'P_105','Manas',1234567890,'ABC'),
(25,'P_106','Prabhat',1234567890,'ABC'),
(23,'P_107','Sahil',1234567890,'ABC'),
(20,'P_108','Sudhir',1234567890,'ABC'),
(24,'P_109','Adwit',1234567890,'ABC'),
(24,'P_110','Harman',1234567890,'ABC');
#)