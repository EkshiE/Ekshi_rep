-- MySQL dump 10.13  Distrib 8.0.11, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: university
-- ------------------------------------------------------
-- Server version	8.0.11

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `audience`
--

DROP TABLE IF EXISTS `audience`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `audience` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `id_audience` int(11) NOT NULL,
  `disciplines` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name_teacher` varchar(40) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  CONSTRAINT `fk_1` FOREIGN KEY (`id`) REFERENCES `students` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `audience`
--

LOCK TABLES `audience` WRITE;
/*!40000 ALTER TABLE `audience` DISABLE KEYS */;
INSERT INTO `audience` VALUES (1,'Иванов И.И.',103,'Химия','Сидоров С.С.'),(2,'Лебедев С.И.',105,'Физика','Попов Ф.А.'),(3,'Зайцева И.В.',104,'История','Петров П.П.');
/*!40000 ALTER TABLE `audience` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `audience_1`
--

DROP TABLE IF EXISTS `audience_1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `audience_1` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(40) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `id_audience` int(11) DEFAULT NULL,
  `disciplines` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `name_teacher` varchar(40) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `audience_1`
--

LOCK TABLES `audience_1` WRITE;
/*!40000 ALTER TABLE `audience_1` DISABLE KEYS */;
INSERT INTO `audience_1` VALUES (3,'Зайцева И.В.',104,'История','Пертов Д.Н.'),(1,'Иванов И.И.',103,'Химия','Сидоров С.С.'),(2,'Лебедев С.И.',105,'Физика','Попов Ф.А.');
/*!40000 ALTER TABLE `audience_1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `students` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `date of birth` date NOT NULL,
  `identification number` varchar(14) COLLATE utf8mb4_unicode_ci NOT NULL,
  `group` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES (1,'Иванов И.И.','2002-05-15','1254518В065РВ5',115241),(2,'Лебедев С.И.','2002-10-23','1258518В065РВ5',126325),(3,'Зайцева И.В.','2002-06-01','6354891В065РВ5',142586);
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students_1`
--

DROP TABLE IF EXISTS `students_1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `students_1` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(40) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `date of birth` date DEFAULT NULL,
  `identification number` varchar(14) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `group` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students_1`
--

LOCK TABLES `students_1` WRITE;
/*!40000 ALTER TABLE `students_1` DISABLE KEYS */;
INSERT INTO `students_1` VALUES (3,'Зайцева И.В.','2002-06-01','6354891В065РВ5',142586),(1,'Иванов И.И.','2002-05-15','1254518В065РВ5',115241),(2,'Лебедев С.И.','2002-10-23','1258518В065РВ5',126325);
/*!40000 ALTER TABLE `students_1` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-23 19:06:06
