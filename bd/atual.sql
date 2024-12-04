CREATE DATABASE  IF NOT EXISTS `vingadores_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `vingadores_db`;
-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: vingadores_db
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
  `chip_gps_id` int NOT NULL AUTO_INCREMENT,
  `localizacao_atual` varchar(255) DEFAULT NULL,
  `ultima_localizacao` varchar(255) DEFAULT NULL,
  `tornozeleira_id` int DEFAULT NULL,
  PRIMARY KEY (`chip_gps_id`),
  KEY `tornozeleira_id` (`tornozeleira_id`),
  CONSTRAINT `chip_gps_ibfk_1` FOREIGN KEY (`tornozeleira_id`) REFERENCES `tornozeleira` (`tornozeleira_id`)
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
  `convocacao_id` int NOT NULL AUTO_INCREMENT,
  `motivo` text NOT NULL,
  `data_convocacao` date NOT NULL,
  `data_comparecimento` date DEFAULT NULL,
  `status` enum('Pendente','Comparecido','Ausente') NOT NULL,
  `heroi_id` int DEFAULT NULL,
  PRIMARY KEY (`convocacao_id`),
  KEY `heroi_id` (`heroi_id`),
  CONSTRAINT `convocacao_ibfk_1` FOREIGN KEY (`heroi_id`) REFERENCES `heroi` (`heroi_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `convocacao`
--

LOCK TABLES `convocacao` WRITE;
/*!40000 ALTER TABLE `convocacao` DISABLE KEYS */;
/*!40000 ALTER TABLE `convocacao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fraqueza`
--

DROP TABLE IF EXISTS `fraqueza`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fraqueza` (
  `fraqueza_id` int NOT NULL AUTO_INCREMENT,
  `descricao` varchar(255) NOT NULL,
  PRIMARY KEY (`fraqueza_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fraqueza`
--

LOCK TABLES `fraqueza` WRITE;
/*!40000 ALTER TABLE `fraqueza` DISABLE KEYS */;
/*!40000 ALTER TABLE `fraqueza` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `habilidade`
--

DROP TABLE IF EXISTS `habilidade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `habilidade` (
  `habilidade_id` int NOT NULL AUTO_INCREMENT,
  `descricao` varchar(255) NOT NULL,
  PRIMARY KEY (`habilidade_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `habilidade`
--

LOCK TABLES `habilidade` WRITE;
/*!40000 ALTER TABLE `habilidade` DISABLE KEYS */;
/*!40000 ALTER TABLE `habilidade` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `heroi`
--

DROP TABLE IF EXISTS `heroi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `heroi` (
  `heroi_id` int NOT NULL AUTO_INCREMENT,
  `nome_heroi` varchar(45) NOT NULL,
  `nome_real` varchar(45) NOT NULL,
  `categoria` enum('Humano','Meta-Humano','Alienigena','Deidade') NOT NULL,
  `nivel_forca` bigint NOT NULL,
  `convocado` tinyint(1) DEFAULT '0',
  `poderes` varchar(255) DEFAULT NULL,
  `poder_principal` varchar(45) DEFAULT NULL,
  `fraquezas` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`heroi_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `heroi`
--

LOCK TABLES `heroi` WRITE;
/*!40000 ALTER TABLE `heroi` DISABLE KEYS */;
INSERT INTO `heroi` VALUES (1,'ad','ad','Meta-Humano',3000,0,'um, dois','tres','quatro'),(2,'Homem Aranha','Peter Parkinson','Meta-Humano',3000,0,'agilidade, teia','sentido aranha','pneumoultramicroscopicosilicovulcanoconiose, homem');
/*!40000 ALTER TABLE `heroi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `heroi_fraqueza`
--

DROP TABLE IF EXISTS `heroi_fraqueza`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `heroi_fraqueza` (
  `heroi_id` int NOT NULL,
  `fraqueza_id` int NOT NULL,
  PRIMARY KEY (`heroi_id`,`fraqueza_id`),
  KEY `fraqueza_id` (`fraqueza_id`),
  CONSTRAINT `heroi_fraqueza_ibfk_1` FOREIGN KEY (`heroi_id`) REFERENCES `heroi` (`heroi_id`),
  CONSTRAINT `heroi_fraqueza_ibfk_2` FOREIGN KEY (`fraqueza_id`) REFERENCES `fraqueza` (`fraqueza_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `heroi_fraqueza`
--

LOCK TABLES `heroi_fraqueza` WRITE;
/*!40000 ALTER TABLE `heroi_fraqueza` DISABLE KEYS */;
/*!40000 ALTER TABLE `heroi_fraqueza` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `heroi_habilidade`
--

DROP TABLE IF EXISTS `heroi_habilidade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `heroi_habilidade` (
  `heroi_id` int NOT NULL,
  `habilidade_id` int NOT NULL,
  PRIMARY KEY (`heroi_id`,`habilidade_id`),
  KEY `habilidade_id` (`habilidade_id`),
  CONSTRAINT `heroi_habilidade_ibfk_1` FOREIGN KEY (`heroi_id`) REFERENCES `heroi` (`heroi_id`),
  CONSTRAINT `heroi_habilidade_ibfk_2` FOREIGN KEY (`habilidade_id`) REFERENCES `habilidade` (`habilidade_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `heroi_habilidade`
--

LOCK TABLES `heroi_habilidade` WRITE;
/*!40000 ALTER TABLE `heroi_habilidade` DISABLE KEYS */;
/*!40000 ALTER TABLE `heroi_habilidade` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mandado_prisao`
--

DROP TABLE IF EXISTS `mandado_prisao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mandado_prisao` (
  `mandado_prisao_id` int NOT NULL AUTO_INCREMENT,
  `motivo` text NOT NULL,
  `data_emissao` date NOT NULL,
  `status` enum('Ativo','Cumprido','Cancelado') NOT NULL,
  `heroi_id` int DEFAULT NULL,
  PRIMARY KEY (`mandado_prisao_id`),
  KEY `heroi_id` (`heroi_id`),
  CONSTRAINT `mandado_prisao_ibfk_1` FOREIGN KEY (`heroi_id`) REFERENCES `heroi` (`heroi_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mandado_prisao`
--

LOCK TABLES `mandado_prisao` WRITE;
/*!40000 ALTER TABLE `mandado_prisao` DISABLE KEYS */;
/*!40000 ALTER TABLE `mandado_prisao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tornozeleira`
--

DROP TABLE IF EXISTS `tornozeleira`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tornozeleira` (
  `tornozeleira_id` int NOT NULL AUTO_INCREMENT,
  `status` enum('Ativa','Inativa') NOT NULL,
  `data_ativacao` date DEFAULT NULL,
  `data_desativacao` date DEFAULT NULL,
  `heroi_id` int DEFAULT NULL,
  PRIMARY KEY (`tornozeleira_id`),
  KEY `heroi_id` (`heroi_id`),
  CONSTRAINT `tornozeleira_ibfk_1` FOREIGN KEY (`heroi_id`) REFERENCES `heroi` (`heroi_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tornozeleira`
--

LOCK TABLES `tornozeleira` WRITE;
/*!40000 ALTER TABLE `tornozeleira` DISABLE KEYS */;
/*!40000 ALTER TABLE `tornozeleira` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'vingadores_db'
--

--
-- Dumping routines for database 'vingadores_db'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-04 13:43:13
