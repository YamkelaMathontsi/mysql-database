-- MySQL dump 10.13  Distrib 8.0.25, for Linux (x86_64)
--
-- Host: localhost    Database: LifeChoices_Online
-- ------------------------------------------------------
-- Server version	8.0.25-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `LifeChoices_Nextofkin`
--

DROP TABLE IF EXISTS `LifeChoices_Nextofkin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `LifeChoices_Nextofkin` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `surname` varchar(30) NOT NULL,
  `cell_number` varchar(10) NOT NULL,
  `identity_num` varchar(13) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LifeChoices_Nextofkin`
--

LOCK TABLES `LifeChoices_Nextofkin` WRITE;
/*!40000 ALTER TABLE `LifeChoices_Nextofkin` DISABLE KEYS */;
INSERT INTO `LifeChoices_Nextofkin` VALUES (1,'Yamkela','Mathontsi','64905672','0005255857087'),(2,'lastest','one','284','409375037'),(3,'Yamkela','Mathontsi','0864537','0000000000000'),(4,'Yamkela','Mathontsi','0097468358','000000000000'),(5,'really ','last one','0987654321','1234567890987'),(6,'Yamkela','Mhrgkrehigvr','328528956','0005255857087'),(7,'Yamkela','MDFBDFKL','095707','0005255857087'),(8,'okay','dvlkdsvk','035097509','0005255857087'),(9,'woah','what happend','84934983','0005255857087');
/*!40000 ALTER TABLE `LifeChoices_Nextofkin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LifeChoices_Online_NextOf_kin`
--

DROP TABLE IF EXISTS `LifeChoices_Online_NextOf_kin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `LifeChoices_Online_NextOf_kin` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `surname` varchar(30) NOT NULL,
  `cell_num` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LifeChoices_Online_NextOf_kin`
--

LOCK TABLES `LifeChoices_Online_NextOf_kin` WRITE;
/*!40000 ALTER TABLE `LifeChoices_Online_NextOf_kin` DISABLE KEYS */;
/*!40000 ALTER TABLE `LifeChoices_Online_NextOf_kin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LifeChoices_Online_User_info`
--

DROP TABLE IF EXISTS `LifeChoices_Online_User_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `LifeChoices_Online_User_info` (
  `id` int NOT NULL AUTO_INCREMENT,
  `time_in` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `name` varchar(20) NOT NULL,
  `surname` varchar(30) NOT NULL,
  `cell_num` int DEFAULT NULL,
  `identity_num` varchar(13) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LifeChoices_Online_User_info`
--

LOCK TABLES `LifeChoices_Online_User_info` WRITE;
/*!40000 ALTER TABLE `LifeChoices_Online_User_info` DISABLE KEYS */;
INSERT INTO `LifeChoices_Online_User_info` VALUES (1,'2021-07-08 10:43:06','Yamkela','Mathontsi',649056472,'0005255857087'),(2,'2021-07-08 10:46:32','Jason','Calvert',649056472,'9406245876087'),(3,'2021-07-08 10:47:19','Brent','Johnson',649056472,'0106567876087'),(4,'2021-07-08 10:48:56','Devin','Fledermaus',725604783,'9408569661087'),(5,'2021-07-08 10:51:02','Nahum','Van Diemen',825654773,'0208569661087'),(6,'2021-07-08 10:52:01','Atheelah','Van Der Sch',615604773,'0108569661087'),(7,'2021-07-09 10:51:10','John','Smith',647094582,'0005255857087');
/*!40000 ALTER TABLE `LifeChoices_Online_User_info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-11 11:39:04
