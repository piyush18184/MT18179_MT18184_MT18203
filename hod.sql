CREATE TABLE `hod` (
  `H_ID` varchar(10) NOT NULL,
  `H_LEAVE_APPROVAL` varchar(45) NOT NULL,
  `OPD_ALLOTMENT` varchar(45) DEFAULT NULL,
  `H_CONTACT` double NOT NULL,
  `H_PERFORMANCE_REVIEW` varchar(45) DEFAULT NULL,
  `H_ASSIGNMENT_DEP` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`H_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;