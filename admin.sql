CREATE TABLE `admin` (
  `ID` varchar(45) NOT NULL,
  `Password` varchar(45) NOT NULL,
  `Email` varchar(45) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



INSERT INTO `db`.`admin`
(`ID`,
`Password`,
`Email`)
VALUES
('D_101','abc','prakhar@yash.com'),
('D_102','abc','shaney@yash.com'),
('D_103','abc','snighda@yash.com'),
('D_104','abc','bhaskar@yash.com'),
('D_105','abc','manak@yash.com'),
('D_106','abc','anjali@yash.com'),
('D_107','abc','neha@yash.com'),
('D_108','abc','sudhir@yash.com'),
('D_109','abc','aman@yash.com'),
('D_110','abc','chhavi@yash.com'),
('P_101','xyz','abhishek@gmail.com'),
('P_102','xyz','anuj@gmail.com'),
('P_103','xyz','bhavam@gmail.com'),
('P_104','xyz','hrithik@gmail.com'),
('P_105','xyz','manas@gmail.com'),
('P_106','xyz','prabhat@gmail.com'),
('P_107','xyz','sahil@gmail.com'),
('P_108','xyz','sudhir@gmail.com'),
('P_109','xyz','adwit@gmail.com'),
('P_110','xyz','harman@gmail.com');