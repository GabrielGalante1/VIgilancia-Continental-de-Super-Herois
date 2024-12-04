CREATE DATABASE  IF NOT EXISTS `vingadores` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `vingadores`;
-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: vingadores
-- ------------------------------------------------------
-- Server version	9.1.0

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
-- Table structure for table `chip_gps`
--

DROP TABLE IF EXISTS `chip_gps`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chip_gps` (
  `id_chip_gps` int NOT NULL,
  `localizacao_atual` varchar(255) DEFAULT NULL,
  `ultima_localizacao` varchar(255) DEFAULT NULL,
  `id_tornozeleira` int NOT NULL,
  PRIMARY KEY (`id_chip_gps`),
  KEY `chip_tornozeleira_idx` (`id_tornozeleira`),
  CONSTRAINT `chip_tornozeleira` FOREIGN KEY (`id_tornozeleira`) REFERENCES `tornozeleira` (`id_tornozeleira`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chip_gps`
--

LOCK TABLES `chip_gps` WRITE;
/*!40000 ALTER TABLE `chip_gps` DISABLE KEYS */;
/*!40000 ALTER TABLE `chip_gps` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `convocacao`
--

DROP TABLE IF EXISTS `convocacao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `convocacao` (
  `id_convocacao` int NOT NULL AUTO_INCREMENT,
  `heroi_id` int NOT NULL,
  `motivo` longtext NOT NULL,
  `data_convocacao` date NOT NULL,
  `data_comparecimento` date DEFAULT NULL,
  `status` enum('Pendente','Comparecido','Ausente') NOT NULL,
  PRIMARY KEY (`id_convocacao`),
  KEY `heroi_convocacao_idx` (`heroi_id`),
  CONSTRAINT `heroi_convocacao` FOREIGN KEY (`heroi_id`) REFERENCES `heroi` (`heroi_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `convocacao`
--

LOCK TABLES `convocacao` WRITE;
/*!40000 ALTER TABLE `convocacao` DISABLE KEYS */;
INSERT INTO `convocacao` VALUES (1,1,'Doente','2024-11-29',NULL,'Pendente'),(2,4,'Hulk esmaga','2024-11-30','2024-11-29','Pendente'),(3,4,'Hulk esmaga','2024-11-30','2024-11-29','Pendente'),(4,4,'hulk esmagador','2024-11-30','2024-11-29','Pendente'),(5,1,'Expeliu muita teia','2024-11-30','2024-11-29','Pendente'),(6,5,'O Dr. Maumau está atacando a base dos aventureiros','2024-11-29','2024-11-29','Pendente'),(7,6,'O Dr. Maumau está atacando a base dos aventureiros','2024-11-29','2024-11-30','Pendente'),(8,1,'Sim','2024-11-29','2024-12-04','Pendente');
/*!40000 ALTER TABLE `convocacao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `heroi`
--

DROP TABLE IF EXISTS `heroi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `heroi` (
  `heroi_id` int NOT NULL AUTO_INCREMENT,
  `nome_heroi` varchar(45) DEFAULT NULL,
  `nome_real` varchar(45) DEFAULT NULL,
  `categoria` enum('Humano','Meta-Humano','Alienigena','Deidade') DEFAULT NULL,
  `poderes` varchar(255) DEFAULT NULL,
  `poder_principal` varchar(45) DEFAULT NULL,
  `fraquezas` varchar(255) DEFAULT NULL,
  `nivel_forca` bigint DEFAULT NULL,
  `convocado` enum('Sim','Não') DEFAULT NULL,
  PRIMARY KEY (`heroi_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `heroi`
--

LOCK TABLES `heroi` WRITE;
/*!40000 ALTER TABLE `heroi` DISABLE KEYS */;
INSERT INTO `heroi` VALUES (1,'Homem Aranha','Peter Parkinson','Meta-Humano','Agilidade,Expelir teia','Sentido aranha','Pneumoultramicroscopicosilicovulcanoconiose,Homem',3000),(2,'Aranha Homem','Peter','Humano','','','',1),(3,'Thor','Thor Odinson','Deidade','Raio,Força,Voar','Mjönir','Arrogância',9825),(4,'Hulk','Bruce Benner','Meta-Humano','Resistência,Regeneração','Super Força','Nenhuma Notável',9000),(5,'Super Sereia','Gi','Meta-Humano','Super força,manipulação da água','Canto da sereia','Fogo',6000),(6,'Super Gafanhoto','Roni','Meta-Humano','Super agilidade','Super Inteligência','Northrop F-5 Tiger',9999);
/*!40000 ALTER TABLE `heroi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mandato_de_prisao`
--

DROP TABLE IF EXISTS `mandato_de_prisao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mandato_de_prisao` (
  `id_mandato` int NOT NULL AUTO_INCREMENT,
  `id_heroi` int NOT NULL,
  `motivo_mandato` longtext NOT NULL,
  `data_emissao` date NOT NULL,
  `status` enum('Ativo','Cumprido','Cancelado') NOT NULL,
  PRIMARY KEY (`id_mandato`),
  KEY `heroi_mandato_idx` (`id_heroi`),
  CONSTRAINT `heroi_mandato` FOREIGN KEY (`id_heroi`) REFERENCES `heroi` (`heroi_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mandato_de_prisao`
--

LOCK TABLES `mandato_de_prisao` WRITE;
/*!40000 ALTER TABLE `mandato_de_prisao` DISABLE KEYS */;
/*!40000 ALTER TABLE `mandato_de_prisao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tornozeleira`
--

DROP TABLE IF EXISTS `tornozeleira`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tornozeleira` (
  `id_tornozeleira` int NOT NULL AUTO_INCREMENT,
  `status` enum('Ativo','Inativo') NOT NULL,
  `data_ativacao` date NOT NULL,
  `data_desativacao` date DEFAULT NULL,
  `id_heroi` int NOT NULL,
  PRIMARY KEY (`id_tornozeleira`),
  KEY `tornozeleira_heroi_idx` (`id_heroi`),
  CONSTRAINT `tornozeleira_heroi` FOREIGN KEY (`id_heroi`) REFERENCES `heroi` (`heroi_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tornozeleira`
--

LOCK TABLES `tornozeleira` WRITE;
/*!40000 ALTER TABLE `tornozeleira` DISABLE KEYS */;
/*!40000 ALTER TABLE `tornozeleira` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `trigger_ativacao_insert` BEFORE INSERT ON `tornozeleira` FOR EACH ROW BEGIN
    IF NEW.status = 'Ativo' THEN
        SET NEW.data_ativacao = NOW();  -- Define a data de ativação como o momento atual
        -- Insere a mensagem na tabela de logs
        INSERT INTO log_ativacao_desativacao (mensagem) 
        VALUES (CONCAT('A tornozeleira foi ativada em ', NOW()));
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `tornozeleira_BEFORE_UPDATE` BEFORE UPDATE ON `tornozeleira` FOR EACH ROW BEGIN
	IF NEW.status = 'Inativo' AND OLD.status <> 'Inativo' THEN
		SET NEW.data_desativacao = CURRENT_TIMESTAMP;
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Dumping events for database 'vingadores'
--

--
-- Dumping routines for database 'vingadores'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-03 21:32:51

 