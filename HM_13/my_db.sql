-- MySQL dump 10.13  Distrib 8.0.11, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: company
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
-- Table structure for table `depart`
--

DROP TABLE IF EXISTS `depart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `depart` (
  `name` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name_depart` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `id_depart` int(11) NOT NULL,
  `descriptions` varchar(400) COLLATE utf8mb4_unicode_ci NOT NULL,
  `perf_appraisal` int(11) NOT NULL,
  PRIMARY KEY (`name`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `depart`
--

LOCK TABLES `depart` WRITE;
/*!40000 ALTER TABLE `depart` DISABLE KEYS */;
INSERT INTO `depart` VALUES ('Бучко','IT',1,'disk.yandex.ru/d/adgadgsdgag',10),('Васильева','IT',1,'disk.yandex.ru/d/dgadgag',10),('Гучек','Бухгалтерия',2,'disk.yandex.ru/d/sdgasgasg',10),('Никитин','Бухгалтерия',2,'disk.yandex.ru/d/sdfdahgfakf',10),('Петров','Маркетинг',3,'disk.yandex.ru/d/jhfkjffkjf',10),('Семенова','Маркетинг',3,'disk.yandex.ru/d/hglidfgaief',10),('Сидоров','Экономический отдел',4,'disk.yandex.ru/d/hfdhflfil',10),('Шелестова','Экономический отдел',4,'disk.yandex.ru/d/4Iirgcjhjsfgg',10);
/*!40000 ALTER TABLE `depart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `state`
--

DROP TABLE IF EXISTS `state`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `state` (
  `name` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `id_name` varchar(14) COLLATE utf8mb4_unicode_ci NOT NULL,
  `job_title` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `payment` int(11) NOT NULL,
  `perf_appraisal` int(11) NOT NULL,
  PRIMARY KEY (`name`),
  UNIQUE KEY `name` (`name`),
  CONSTRAINT `fk_1` FOREIGN KEY (`name`) REFERENCES `depart` (`name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `state`
--

LOCK TABLES `state` WRITE;
/*!40000 ALTER TABLE `state` DISABLE KEYS */;
INSERT INTO `state` VALUES ('Бучко','65389B12457BP5','Экономист',2300,5),('Васильева','27854B12457BP5','Бухгалтер',2100,6),('Гучек','42586B12457BP5','Гл_экономист',4600,8),('Никитин','45629B12457BP5','Системный_админ',6300,5),('Петров','35468B12457BP5','Маркетолог',2600,9),('Семенова','54287B12457BP5','Специалист',2200,4),('Сидоров','45689B12457BP5','Разработчик',7200,7),('Шелестова','75632B12457BP5','Гл_бухгалтер',5800,7);
/*!40000 ALTER TABLE `state` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-26 17:16:16
