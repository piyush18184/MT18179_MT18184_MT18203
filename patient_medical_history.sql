CREATE TABLE `patient_medical_history` (
  `Ref_ID` varchar(10) NOT NULL,
  `Pat_ID` varchar(10) NOT NULL,
  `Prescription` varchar(80) NOT NULL,
  `Past_Reports` varchar(80) NOT NULL,
  PRIMARY KEY (`Ref_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;




INSERT INTO `db`.`patient_medical_history`
(`Ref_ID`,
`Pat_ID`,
`Prescription`,
`Past_Reports`)
VALUES
('RAD_101','P_101','ABCDEF','STUVWXYZ'),
('PAT_101','P_101','ABCDEF','STUVWXYZ'),
('ORT_101','P_101','ABCDEF','STUVWXYZ'),
('GYN_101','P_101','ABCDEF','STUVWXYZ'),
('RAD_102','P_104','ABCDEF','STUVWXYZ'),
('RAD_103','P_103','ABCDEF','STUVWXYZ');