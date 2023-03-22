drop database `Db_Doan1`;

create database `Db_Doan1`;
USE `Db_Doan1`;
/****** Object:  Table `Camera`    Script Date: 1/19/2023 1:01:23 AM ******/


CREATE TABLE `Camera`(
	`CameraID` int NOT NULL AUTO_INCREMENT,
	`UserID` int NOT NULL,
    `CameraName` varchar(255) NOT NULL,
    `delete_flag` int NOT NULL,
 CONSTRAINT `PK_Camera` PRIMARY KEY 
(
	`CameraID` ASC
)
);
/****** Object:  Table `EmailList`    Script Date: 1/19/2023 1:01:23 AM ******/


CREATE TABLE `Email`(
	`EmailID` int NOT NULL AUTO_INCREMENT,
	`UserID` int NOT NULL,
	`NotificationID` int NOT NULL,
	`Email` varchar(50) NULL,
 CONSTRAINT `PK_Email` PRIMARY KEY 
(
	`EmailID` ASC
)
);
/****** Object:  Table `Event`    Script Date: 1/19/2023 1:01:23 AM ******/


CREATE TABLE `Event`(
	`EventID` int NOT NULL AUTO_INCREMENT,
	`CameraID` int NOT NULL,
	`Message` varchar(255) NULL,
	datetime datetime NULL,
 CONSTRAINT `PK_Event` PRIMARY KEY 
(
	`EventID` ASC
)
);
/****** Object:  Table `Help`    Script Date: 1/19/2023 1:01:23 AM ******/


CREATE TABLE `Help`(
	`HelpID` int NOT NULL AUTO_INCREMENT,
	`Answer` varchar(255) NULL,
	`Question` varchar(255) NULL,
 CONSTRAINT `PK_Help` PRIMARY KEY 
(
	`HelpID` ASC
)
);
/****** Object:  Table `HistoryCamera`    Script Date: 1/19/2023 1:01:23 AM ******/


CREATE TABLE `CameraHistory`(
	`CameraHistoryID` int NOT NULL AUTO_INCREMENT,
	`CameraID` int NULL,
	`FilePath` varchar(255) NULL,
	datetime datetime NULL,
 CONSTRAINT `PK_CameraHistory` PRIMARY KEY 
(
	`CameraHistoryID` ASC
)
);
/****** Object:  Table `Notification`    Script Date: 1/19/2023 1:01:23 AM ******/


CREATE TABLE `Notification`(
	`NotificationID` int NOT NULL AUTO_INCREMENT,
    `UserID` int NOT NULL,
	`CameraID` int NULL,
    `EventID` int NULL,
	`Message` varchar(255) NULL,
	datetime datetime NULL,
 CONSTRAINT `PK_Notification` PRIMARY KEY 
(
	`NotificationID` ASC
)
);
/****** Object:  Table `User`    Script Date: 1/19/2023 1:01:23 AM ******/


CREATE TABLE `User`(
	`UserID` int NOT NULL AUTO_INCREMENT,
	`UserName` varchar(50) NOT NULL,
	`PassWord` varchar(50) NOT NULL,
	`Role` int NOT NULL,
    `delete_flag` int NOT NULL,
 CONSTRAINT `PK_User` PRIMARY KEY 
(
	`UserID` ASC
)
);

ALTER TABLE `Camera`  ADD  CONSTRAINT FOREIGN KEY (`UserID`)
REFERENCES `User` (`UserID`);
ALTER TABLE `Camera` CHECK partition `FK_Camera_User`;
ALTER TABLE `Email`  ADD  CONSTRAINT FOREIGN KEY (`NotificationID`)
REFERENCES `Notification` (`NotificationID`);
ALTER TABLE `Email` CHECK partition `FK_Email_Notification`;
ALTER TABLE `Email`  ADD  CONSTRAINT FOREIGN KEY (`UserID`)
REFERENCES `User` (`UserID`);
ALTER TABLE `Email` CHECK partition `FK_Email_User`;
ALTER TABLE `Event`  ADD  CONSTRAINT FOREIGN KEY (`CameraID`)
REFERENCES `Camera` (`CameraID`);
ALTER TABLE `Event` CHECK partition `FK_Event_Camera`;
ALTER TABLE `CameraHistory`  ADD  CONSTRAINT FOREIGN KEY (`CameraID`)
REFERENCES `Camera` (`CameraID`);
ALTER TABLE `CameraHistory` CHECK partition `FK_CameraHistory_Camera`;
ALTER TABLE `Notification`  ADD  CONSTRAINT FOREIGN KEY (`UserID`)
REFERENCES `User` (`UserID`);
ALTER TABLE `Notification` CHECK partition `FK_Notification_User`;
ALTER TABLE `Notification`  ADD  CONSTRAINT FOREIGN KEY (`CameraID`)
REFERENCES `Camera` (`CameraID`);
ALTER TABLE `Notification` CHECK partition `FK_Notification_Camera`;
ALTER TABLE `Notification`  ADD  CONSTRAINT FOREIGN KEY (`EventID`)
REFERENCES `Event` (`EventID`);
ALTER TABLE `Notification` CHECK partition `FK_Notification_Event`;

/****** End ******/

select * from User;
select * from Camera;
select * from Event;
select * from Notification;
select * from Email;
select * from CameraHistory;

INSERT INTO Notification(CameraID, EventID, Message, datetime) VALUES (null, null, "test message", "2023-03-19 20:47:00");

DELETE from User WHERE UserID = 1;

UPDATE User SET Password = 'newpassword' WHERE UserID=1