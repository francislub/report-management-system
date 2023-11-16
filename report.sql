-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: report
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `class`
--

DROP TABLE IF EXISTS `class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `class` (
  `classID` int NOT NULL,
  `class` varchar(45) NOT NULL,
  PRIMARY KEY (`classID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `class`
--

LOCK TABLES `class` WRITE;
/*!40000 ALTER TABLE `class` DISABLE KEYS */;
INSERT INTO `class` VALUES (1001,'S.1'),(1002,'S.2'),(1003,'S.3'),(1004,'S.4');
/*!40000 ALTER TABLE `class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subject`
--

DROP TABLE IF EXISTS `subject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `subject` (
  `subjectID` int NOT NULL,
  `class` varchar(45) DEFAULT NULL,
  `classteacher` varchar(45) DEFAULT NULL,
  `subject1` varchar(45) DEFAULT NULL,
  `teacher1` varchar(45) DEFAULT NULL,
  `subject2` varchar(45) DEFAULT NULL,
  `teacher2` varchar(45) DEFAULT NULL,
  `subject3` varchar(45) DEFAULT NULL,
  `teacher3` varchar(45) DEFAULT NULL,
  `subject4` varchar(45) DEFAULT NULL,
  `teacher4` varchar(45) DEFAULT NULL,
  `subject5` varchar(45) DEFAULT NULL,
  `teacher5` varchar(45) DEFAULT NULL,
  `subject6` varchar(45) DEFAULT NULL,
  `teacher6` varchar(45) DEFAULT NULL,
  `subject7` varchar(45) DEFAULT NULL,
  `teacher7` varchar(45) DEFAULT NULL,
  `subject8` varchar(45) DEFAULT NULL,
  `teacher8` varchar(45) DEFAULT NULL,
  `subject9` varchar(45) DEFAULT NULL,
  `teacher9` varchar(45) DEFAULT NULL,
  `subject10` varchar(45) DEFAULT NULL,
  `teacher10` varchar(45) DEFAULT NULL,
  `subject11` varchar(45) DEFAULT NULL,
  `teacher11` varchar(45) DEFAULT NULL,
  `subject12` varchar(45) DEFAULT NULL,
  `teacher12` varchar(45) DEFAULT NULL,
  `subject13` varchar(45) DEFAULT NULL,
  `teacher13` varchar(45) DEFAULT NULL,
  `subject14` varchar(45) DEFAULT NULL,
  `teacher14` varchar(45) DEFAULT NULL,
  `subject15` varchar(45) DEFAULT NULL,
  `teacher15` varchar(45) DEFAULT NULL,
  `subject16` varchar(45) DEFAULT NULL,
  `teacher16` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`subjectID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subject`
--

LOCK TABLES `subject` WRITE;
/*!40000 ALTER TABLE `subject` DISABLE KEYS */;
INSERT INTO `subject` VALUES (1001,'S.1','Tr.Lubanjwa Francis','math','Tr.Lubanjwa Francis','phy','Tr.Lubanjwa Francis','Boi','Naka','Chem','Naka','History','Moses Troy','CRE','Naka','','Select','','Select','','Select','','Select','','Select','','Select','','Select','','Select','','Select','','Select'),(1002,'S.2','Moses Troy','Math','Naka','CRE','Tr.Lubanjwa Francis','Bio','Tr.Lubanjwa Francis','Chem','Naka','','Select','','Select','','Select','','Select','','Select','','Select','','Select','','Select','','Select','','Select','','Select','','Select');
/*!40000 ALTER TABLE `subject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teacher`
--

DROP TABLE IF EXISTS `teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teacher` (
  `Ref` int NOT NULL,
  `Name` varchar(100) DEFAULT NULL,
  `Gender` varchar(45) DEFAULT NULL,
  `Mobile` varchar(45) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Nationality` varchar(45) DEFAULT NULL,
  `Address` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Ref`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher`
--

LOCK TABLES `teacher` WRITE;
/*!40000 ALTER TABLE `teacher` DISABLE KEYS */;
INSERT INTO `teacher` VALUES (1000,'Tr.Lubanjwa Francis','Male','741789121','francis@gmail.com','Ugandan','kampala'),(1001,'Naka','Male','078243567','naka@gmail.com','Ugandan','Masaka'),(1002,'Moses Troy','Male','078643456','moses@gmail.com','Ugandan','Kampala');
/*!40000 ALTER TABLE `teacher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `term`
--

DROP TABLE IF EXISTS `term`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `term` (
  `termID` int NOT NULL,
  `year` varchar(45) DEFAULT NULL,
  `term` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`termID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `term`
--

LOCK TABLES `term` WRITE;
/*!40000 ALTER TABLE `term` DISABLE KEYS */;
INSERT INTO `term` VALUES (1001,'1234','1234'),(1002,'4','112'),(1003,'2345','123w');
/*!40000 ALTER TABLE `term` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `year`
--

DROP TABLE IF EXISTS `year`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `year` (
  `yearID` int NOT NULL,
  `year` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`yearID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `year`
--

LOCK TABLES `year` WRITE;
/*!40000 ALTER TABLE `year` DISABLE KEYS */;
INSERT INTO `year` VALUES (1001,'1234'),(1002,'4'),(1003,'2345'),(1004,'asdfg');
/*!40000 ALTER TABLE `year` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'report'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-16 13:04:04
