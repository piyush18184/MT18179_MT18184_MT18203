CREATE TABLE `doctor_professional_details` (
  `D_Department` char(20) NOT NULL,
  `D_DID` varchar(10) NOT NULL,
  `D_OPD_TIME_START` time NOT NULL,
  `D_OPD_TIME_END` time NOT NULL,
  `D_Type` varchar(20) NOT NULL,
  `D_Specialization` char(25) NOT NULL,
  `D_RoomNo` varchar(10) NOT NULL,
  `D_ExtensionNo` int(11) NOT NULL,
  PRIMARY KEY (`D_DID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



INSERT INTO `db`.`doctor_professional_details`
(`D_Department`,
`D_DID`,
`D_OPD_TIME_START`,
`D_OPD_TIME_END`,
`D_Type`,
`D_Specialization`,
`D_RoomNo`,
`D_ExtensionNo`)
VALUES
#(              
('Pathology','D_101','08:00:00','10:00:00','Junior Resident','Pursuing MD in Pathology','R_101',12345),
('Medicine','D_102','08:00:00','10:00:00','Junior Resident','Pursuing MD in Medicine','R_102',12345),
('Surgery','D_103','09:00:00','12:00:00','Junior Resident','Pursuing MD in Surgery','R_103',12345),
('Pediatrics','D_104','13:00:00','17:00:00','Junior Resident','Pursuing MD in Pediatrics','R_104',12345),
('Gynocology','D_105','12:00:00','14:00:00','Senior Resident','MD in Gynocology','R_105',12345),
('Oncolgy','D_106','13:00:00','15:00:00','Senior Resident','MD in Oncology','R_106',12345),
('Dentistry','D_107','08:00:00','10:00:00','Senior Resident','MD in Dentistry','R_107',12345),
('ENT','D_108','08:00:00','10:00:00','Senior Resident','MD in ENT','R_108',12345),
('Orthopadics','D_109','10:00:00','11:00:00','Specialist','MD in Orthopadics','R_109',12345),
('Pulmonary Medicine','D_110','15:00:00','18:00:00','Senior Specialist','MD in Pulmonary Medicine','R_110',12345),
('Neurology','D_111','18:00:00','20:00:00','Specialist','MD in Neurology','R_111',12345),
('Physiotherapy','D_112','20:00:00','21:00:00','Specialist','MD in Physiotherapy','R_112',12345),
('Pyschiatry','D_113','19:00:00','21:00:00','Senior Specialist','MD in Pyschiatry','R_113',12345),
('Radiology','D_114','16:00:00','18:00:00','HOD','MD in Radiology','R_114',12345),
('Cardiology','D_115','18:00:00','19:00:00','HOD','MD in Cardiology','R_115',12345),
('Dermatology','D_116','10:00:00','11:00:00','HOD','MD in Dermatology','R_116',12345)
;
#)