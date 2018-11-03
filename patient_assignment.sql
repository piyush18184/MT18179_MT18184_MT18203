CREATE TABLE `patient_assignment` (
  `E_ID` varchar(10) NOT NULL,
  `E_NAME` char(25) NOT NULL,
  `E_TYPE` varchar(45) NOT NULL,
  `E_AGE` int(11) NOT NULL,
  PRIMARY KEY (`E_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
