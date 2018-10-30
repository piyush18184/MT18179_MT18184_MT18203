CREATE TABLE `department` (
  `Dep_ID` varchar(10) NOT NULL,
  `Dep_HOD` char(20) NOT NULL,
  `Dep_Name` char(20) NOT NULL,
  `Dep_Building` varchar(25) NOT NULL,
  `Dep_Contact` int(11) NOT NULL,
  `Dep_Rooms` int(11) NOT NULL,
  `Dep_OPD` varchar(25) NOT NULL,
  PRIMARY KEY (`Dep_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



INSERT INTO `db`.`department`
(`Dep_ID`,
`Dep_HOD`,
`Dep_Name`,
`Dep_Building`,
`Dep_Contact`,
`Dep_Rooms`,
`Dep_OPD`)
VALUES
#(
('Dep_101','Prakhar','Pathology','B_101',12345,20,'Phase_I'),
('Dep_102','Shaney','Medicine','B_102',12345,20,'Phase_II'),
('Dep_103','Snighda','Surgery','B_103',12345,20,'Phase_III'),
('Dep_104','Bhaskar','Pediatrics','B_104',12345,20,'Phase_IV'),
('Dep_105','Manak','Gynocology','B_105',12345,20,'Phase_V'),
('Dep_106','Anjali','Oncolgy','B_106',12345,20,'Phase_II'),
('Dep_107','Neha','Dentistry','B_107',12345,20,'Phase_III'),
('Dep_108','Sudhir','ENT','B_108',12345,20,'Phase_II'),
('Dep_109','Aman','Orthopadics','B_109',12345,20,'Phase_II'),
('Dep_110','Chhavi','Pulmonary Medicine','B_110',12345,20,'Phase_VI'),
('Dep_111','Vinod','Neurology','B_111',12345,20,'Phase_VII'),
('Dep_112','Vijay','Physiotherapy','B_112',12345,20,'Phase_VII'),
('Dep_113','Viraj','Pyschiatry','B_113',12345,20,'Phase_V'),
('Dep_114','Vineet','Radiology','B_114',12345,20,'Phase_V'),
('Dep_115','Mayank','Cardiology','B_115',12345,20,'Phase_III'),
('Dep_116','Shraddha','Dermatology','B_116',12345,20,'Phase_VI');
#)
