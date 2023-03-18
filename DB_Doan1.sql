create database `Db_Doan1`;
USE `Db_Doan1`;
/****** Object:  Table `Camera`    Script Date: 1/19/2023 1:01:23 AM ******/


CREATE TABLE `Camera`(
	`CameraID` int NOT NULL AUTO_INCREMENT,
	`UserID` int NOT NULL,
	`HistoryCameraID` int NOT NULL,
	`EventID` int NOT NULL,
	`NotificationID` int NOT NULL,
 CONSTRAINT `PK_Camera` PRIMARY KEY 
(
	`CameraID` ASC
)
);
/****** Object:  Table `EmailList`    Script Date: 1/19/2023 1:01:23 AM ******/


CREATE TABLE `EmailList`(
	`EmailListID` int NOT NULL AUTO_INCREMENT,
	`UserID` int NOT NULL,
	`NotificationID` int NOT NULL,
	`Email` varchar(50) NULL,
 CONSTRAINT `PK_EmailList` PRIMARY KEY 
(
	`EmailListID` ASC
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
	`HelpID` int NOT NULL,
	`Answer` varchar(255) NULL,
	`Question` varchar(255) NULL,
 CONSTRAINT `PK_Help` PRIMARY KEY 
(
	`HelpID` ASC
)
);
/****** Object:  Table `HistoryCamera`    Script Date: 1/19/2023 1:01:23 AM ******/


CREATE TABLE `HistoryCamera`(
	`HistoryCameraID` int NOT NULL,
	`CameraID` int NOT NULL,
	`FilePath` varchar(255) NULL,
	datetime datetime NULL,
 CONSTRAINT `PK_HistoryCamera` PRIMARY KEY 
(
	`HistoryCameraID` ASC
)
);
/****** Object:  Table `Notification`    Script Date: 1/19/2023 1:01:23 AM ******/


CREATE TABLE `Notification`(
	`NotificationID` int NOT NULL,
	`CameraID` int NOT NULL,
	`EmailListID` int NOT NULL,
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
 CONSTRAINT `PK_User` PRIMARY KEY 
(
	`UserID` ASC
)
);
ALTER TABLE `Camera`  ADD  CONSTRAINT FOREIGN KEY (`EventID`) 
REFERENCES `Event` (`EventID`);
ALTER TABLE `Camera` CHECK partition `FK_Camera_Event`;
ALTER TABLE `Camera`  ADD  CONSTRAINT FOREIGN KEY (`HistoryCameraID`)
REFERENCES `HistoryCamera` (`HistoryCameraID`);
ALTER TABLE `Camera` CHECK partition `FK_Camera_HistoryCamera`;
ALTER TABLE `Camera`  ADD  CONSTRAINT FOREIGN KEY (`NotificationID`)
REFERENCES `Notification` (`NotificationID`);
ALTER TABLE `Camera` CHECK partition `FK_Camera_Notification`;
ALTER TABLE `Camera`  ADD  CONSTRAINT FOREIGN KEY (`UserID`)
REFERENCES `User` (`UserID`);
ALTER TABLE `Camera` CHECK partition `FK_Camera_User`;
ALTER TABLE `EmailList`  ADD  CONSTRAINT FOREIGN KEY (`NotificationID`)
REFERENCES `Notification` (`NotificationID`);
ALTER TABLE `EmailList` CHECK partition `FK_EmailList_Notification`;
ALTER TABLE `EmailList`  ADD  CONSTRAINT FOREIGN KEY (`UserID`)
REFERENCES `User` (`UserID`);
ALTER TABLE `EmailList` CHECK partition `FK_EmailList_User`;
ALTER TABLE `Event`  ADD  CONSTRAINT FOREIGN KEY (`CameraID`)
REFERENCES `Camera` (`CameraID`);
ALTER TABLE `Event` CHECK partition `FK_Event_Camera`;
ALTER TABLE `HistoryCamera`  ADD  CONSTRAINT FOREIGN KEY (`CameraID`)
REFERENCES `Camera` (`CameraID`);
ALTER TABLE `HistoryCamera` CHECK partition `FK_HistoryCamera_Camera`;
ALTER TABLE `Notification`  ADD  CONSTRAINT FOREIGN KEY (`CameraID`)
REFERENCES `Camera` (`CameraID`);
ALTER TABLE `Notification` CHECK partition `FK_Notification_Camera`;






