CREATE TABLE `appointments` (
  `P_Appointment_ID` varchar(10) NOT NULL,
  `Appointed_D_ID` varchar(10) NOT NULL,
  `P_Appointment_Date` date NOT NULL,
  `P_Appointment_Time` time NOT NULL,
  PRIMARY KEY (`P_Appointment_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



INSERT INTO `db`.`appointments`
(`P_Appointment_ID`,
`Appointed_D_ID`,
`P_Appointment_Date`,
`P_Appointment_Time`)
VALUES
('RAD_120','D_114','2018-11-15','08:00:00'),
('RAD_121','D_114','2018-11-16','08:00:00'),
('CAR_101','D_115','2018-11-10','08:00:00')
;