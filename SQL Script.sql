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

#DELETE FROM `db`.`patient_details` WHERE `P_ID`='P_101';

SELECT * FROM `db`.`patient_details`;

ALTER TABLE `db`.`patient_details` ADD COLUMN `P_Email` VARCHAR(20);

UPDATE `db`.`patient_details` SET `P_Email` = 'abhishek@gmail.com' WHERE `P_ID`='P_101';

ALTER TABLE `db`.`patient_details` CHANGE `P_Age` `P_Age` INT NOT NULL AFTER `P_Name`;


INSERT INTO `db`.`doctor_details`
(`D_Age`,
`D_ID`,
`D_Name`,
`D_PNo`,
`D_Email`,
`D_Add`)
VALUES
#(
(45,'D_101','Prakhar',1234567890,'prakhar@yash.com','ABC'),
(30,'D_102','Shaney',1234567890,'shaney@yash.com','ABC'),
(55,'D_103','Snighda',1234567890,'snighda@yash.com','ABC'),
(32,'D_104','Bhaskar',1234567890,'bhaskar@yash.com','ABC'),
(44,'D_105','Manak',1234567890,'manak@yash.com','ABC'),
(44,'D_106','Anjali',1234567890,'anjali@yash.com','ABC'),
(33,'D_107','Neha',1234567890,'neha@yash.com','ABC'),
(33,'D_108','Sudhir',1234567890,'sudhir@yash.com','ABC'),
(55,'D_109','Aman',1234567890,'aman@yash.com','ABC'),
(39,'D_110','Chhavi',1234567890,'chhavi@yash.com','ABC');
#)


SELECT * FROM `db`.`doctor_details`;

ALTER TABLE `db`.`doctor_details` CHANGE `D_Age` `D_Age` INT NOT NULL AFTER `D_Name`;