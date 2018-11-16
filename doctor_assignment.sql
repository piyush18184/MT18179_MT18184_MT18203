CREATE TABLE `doctor_assignment` (
  `DOC_ID` varchar(10) NOT NULL,
  `PAT_ID` varchar(10) NOT NULL,
  `DOC_MAX_LMT` int(11) DEFAULT NULL,
  `REF_DOC_ID` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`DOC_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



INSERT INTO `db`.`doctor_assignment`
(`DOC_ID`,
`PAT_ID`,
`DOC_MAX_LMT`,
`REF_DOC_ID`)
VALUES
('D_101','P_101',20,''),
('D_101','P_102',20,''),
('D_102','P_103',20,'');
