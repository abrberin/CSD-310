-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: whatabook
-- ------------------------------------------------------
-- Server version	8.0.34

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
-- Table structure for table `book`
--

DROP TABLE IF EXISTS `book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book` (
  `Book_ID` int NOT NULL,
  `Book_Name` varchar(200) NOT NULL,
  `Details` varchar(500) DEFAULT NULL,
  `Author` varchar(200) NOT NULL,
  PRIMARY KEY (`Book_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book`
--

LOCK TABLES `book` WRITE;
/*!40000 ALTER TABLE `book` DISABLE KEYS */;
INSERT INTO `book` VALUES (38,'SQL Performance Explained','It\'s a practical guide for database professionals.','Markus Winand'),(56,'The Art of SQL','Stephane Faroult',' It\'s suitable for both beginners and experienced database professionals.'),(67,'Database Systems: The Complete Book','covering both fundamental concepts and advanced topics','Hector Garcia-Molina'),(74,'NoSQL Distilled: A Brief Guide to the Emerging World of Polyglot Persistence','guide for developers and architects interested in non-relational databases.','Martin Fowler'),(83,'Designing Data-Intensive Applications',' Martin Kleppmann','This book delves into the architecture and design of data-intensive applications, including databases, stream processing, and distributed systems.'),(85,'Database Internals: A Deep Dive into How Distributed Data Systems Work','Alex Petrov','this book provides an in-depth exploration of database internals, consistency models, and distributed algorithms.'),(87,'Database Design for Mere Mortals','It\'s an excellent resource for those new to databases.','Michael J. Hernandez'),(93,'Hadoop: The Definitive Guide','Tom White','extensive information on Hadoop Distributed File System (HDFS) '),(95,'MongoDB: The Definitive Guide','Kristina Chodorow','covers everything from installation and schema design to advanced querying and administration.');
/*!40000 ALTER TABLE `book` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-29 23:36:57
