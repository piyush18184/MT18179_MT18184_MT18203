CREATE TABLE `unassigned_patient` (
  `UP_ID` varchar(10) NOT NULL,
  `UP_PROB_DEP` varchar(20) NOT NULL,
  `UP_E_TYPE` char(1) NOT NULL,
  PRIMARY KEY (`UP_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;




INSERT INTO `db`.`unassigned_patient`
(`UP_ID`,
`UP_PROB_DEP`,
`UP_E_TYPE`)
VALUES
('P-106','PATHOLOGY',''),
('P_107','PATHOLOGY',''),
('P_108','RADIOLOGY','');
