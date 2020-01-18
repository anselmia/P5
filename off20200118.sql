-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: open_food_fact
-- ------------------------------------------------------
-- Server version	8.0.19

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
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=473 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (3,'Aliments et boissons à base de végétaux'),(4,'Snacks'),(5,'Boissons'),(6,'Snacks sucrés'),(7,'Produits laitiers'),(8,'Viandes'),(9,'Plats préparés'),(10,'Aliments à base de fruits et de légumes'),(11,'Céréales et pommes de terre'),(12,'Produits fermentés'),(13,'Produits laitiers fermentés'),(14,'Produits à tartiner'),(15,'Biscuits et gâteaux'),(16,'Charcuteries'),(17,'Epicerie'),(18,'Petit-déjeuners'),(19,'Fromages'),(20,'Céréales et dérivés'),(21,'Fruits et produits dérivés'),(22,'Desserts'),(23,'Boissons à base de végétaux'),(24,'Produits à tartiner sucrés'),(25,'Sauces'),(26,'Produits de la mer'),(27,'Surgelés'),(28,'Confiseries'),(29,'Conserves'),(30,'Légumes et dérivés'),(31,'Pâtes à tartiner végétales'),(32,'Poissons'),(33,'Boissons alcoolisées'),(34,'Biscuits'),(35,'Volailles'),(36,'Boissons aux fruits'),(37,'Produits à la viande'),(38,'Chocolats'),(39,'Matières grasses'),(40,'Fromages de France'),(41,'Condiments'),(42,'Snacks salés'),(43,'Gâteaux'),(44,'Jus et nectars'),(45,'Confitures et marmelades'),(46,'Boissons avec sucre ajouté'),(47,'Produits déshydratés'),(48,'Frais'),(49,'Yaourts'),(50,'Plats préparés à la viande'),(51,'Pains'),(52,'Confitures'),(53,'Apéritif'),(54,'Fromages de vache'),(55,'Poulets'),(56,'Produits à tartiner salés'),(57,'Confitures de fruits'),(58,'Fruits à coques et dérivés'),(59,'en:fruit-juices-and-nectars'),(60,'Édulcorants'),(61,'Jus de fruits'),(62,'Aliments à base de plantes en conserve'),(63,'Légumineuses et dérivés'),(64,'Boissons chaudes'),(65,'Pâtes alimentaires'),(66,'Matières grasses végétales'),(67,'Vins'),(68,'Graines'),(69,'Aliments à base de plantes séchées'),(70,'Huiles'),(71,'Jambons'),(72,'Viennoiseries'),(73,'Produits de la ruche'),(74,'Céréales pour petit-déjeuner'),(75,'Pâtisseries'),(76,'Légumineuses'),(77,'Desserts glacés'),(78,'Fromages à pâte pressée cuite'),(79,'Miels'),(80,'Desserts lactés'),(81,'Confiseries chocolatées'),(82,'Chocolats noirs'),(83,'Chips et frites'),(84,'Soupes'),(85,'Légumes en conserve'),(86,'Fruits à coques'),(87,'Fruits secs'),(88,'Boissons sans sucre ajouté'),(89,'Saucisses'),(90,'Plats préparés au poisson'),(91,'Glaces et sorbets'),(92,'Fruits'),(93,'Bonbons'),(94,'Chips'),(95,'Boissons gazeuses'),(96,'Saucissons'),(97,'Poissons et viandes et oeufs'),(98,'Biscuits au chocolat'),(99,'Plats à base de pâtes'),(100,'Sirops'),(101,'Plats préparés à réchauffer au micro-ondes'),(102,'Pizzas tartes salées et quiches'),(103,'Bières'),(104,'en:labeled-cheeses'),(105,'Poissons en conserve'),(106,'Thés'),(107,'en:aoc-cheeses'),(108,'Compotes'),(109,'Laits'),(110,'Plats à la volaille'),(111,'Confitures de fruits rouges'),(112,'Filets de poulet'),(113,'Céréales en grains'),(114,'Produits lyophilisés à reconstituer'),(115,'Bonbons de chocolat'),(116,'Vins français'),(117,'Jambons blancs'),(118,'Jus de fruits pur jus'),(119,'Sodas'),(120,'Foies gras'),(121,'Chocolats au lait'),(122,'Cafés'),(123,'Glaces'),(124,'Plats préparés surgelés'),(125,'Yaourts aux fruits'),(126,'Moutardes'),(127,'Terrines'),(128,'Barres'),(129,'Infusions'),(130,'Salades'),(131,'Pickles'),(132,'Rillettes'),(133,'Foies gras de canard'),(134,'Matières grasses à tartiner'),(135,'Tartes'),(136,'Poissons fumés'),(137,'Comté'),(138,'Pâtes sèches'),(139,'Fromages pasteurisés'),(140,'Fromages à pâte pressée non cuite'),(141,'Légumes préparés'),(142,'Thons'),(143,'Brioches'),(144,'Boissons sans alcool'),(145,'Préparations de poisson'),(146,'Réfrigérés'),(147,'Epices'),(148,'Compléments alimentaires'),(149,'Aliments et boissons de Noël'),(150,'Boissons édulcorées'),(151,'Charcuteries diverses'),(152,'Saumons'),(153,'Saucisses françaises'),(154,'Sauces tomate'),(155,'Sirops aromatisés'),(156,'Biscuits apéritifs'),(157,'Sandwichs'),(158,'Flocons'),(159,'Pizzas'),(160,'Aliments pour bébé'),(161,'Flocons de céréales'),(162,'Bœuf'),(163,'Compotes de pomme'),(164,'Salades composées'),(165,'Dindes'),(166,'Filets de poissons'),(167,'Pâtes à tartiner'),(168,'Soupes de légumes'),(169,'Tomates et dérivés'),(170,'Légumineuses en conserve'),(171,'Fromages italiens'),(172,'Aliments à base de plantes frais'),(173,'Eaux'),(174,'Plats préparés frais'),(175,'Plantes condimentaires'),(176,'Graines de légumineuses'),(177,'en:preparations-made-from-fish-meat'),(178,'Gâteaux au chocolat'),(179,'Biscuits sablés'),(180,'Matières grasses animales'),(181,'Fromages à pâte molle à croûte fleurie'),(182,'Légumes secs'),(183,'Substitut du lait'),(184,'Chips de pommes de terre'),(185,'Boissons végétales'),(186,'Porc'),(187,'Madeleines'),(188,'Mueslis'),(189,'Nectars de fruits'),(190,'Plats au poulet'),(191,'Plats préparés en conserve'),(192,'Milkfat'),(193,'Plats au bœuf'),(194,'Saucissons secs'),(195,'Beurres'),(196,'Produits laitiers à tartiner'),(197,'Sardines'),(198,'Plats préparés réfrigérés'),(199,'Jambons crus'),(200,'Vinaigres'),(201,'Riz'),(202,'Aliments à base de plantes surgelés'),(203,'Pâtes farcies'),(204,'Œufs'),(205,'Olives'),(206,'Boissons instantanées'),(207,'Produits panés'),(208,'Emmentals'),(209,'Saumons fumés'),(210,'Farines'),(211,'Sardines en conserve'),(212,'Légumes frais'),(213,'Pâtes de blé'),(214,'Jus de pomme'),(215,'Mayonnaises'),(216,'Boissons lactées'),(217,'Pâtes de blé dur'),(218,'Cream cheeses'),(219,'Charcuteries cuites'),(220,'Eaux de sources'),(221,'Foies gras entiers'),(222,'Jambons secs'),(223,'Cookies'),(224,'Crèmes glacées en pot'),(225,'Mélanges de flocons de céréales'),(226,'Plats au porc'),(227,'Légumes-feuilles'),(228,'Crêpes et galettes'),(229,'Escalopes de dinde'),(230,'Fromages de chèvre'),(231,'Vins rouges'),(232,'Cuisses de poulet'),(233,'Légumes surgelés'),(234,'Crèmes'),(235,'Desserts au chocolat'),(236,'Aides culinaires'),(237,'Nouilles'),(238,'Pâtés végétaux'),(239,'Fromages de brebis'),(240,'Plats à base de riz'),(241,'Rillettes de viande'),(242,'Laits homogénéisés'),(243,'Pains de mie'),(244,'Confitures de fraises'),(245,'Laits demi-écrémés'),(246,'Produits artisanaux'),(247,'Laits UHT'),(248,'Miels de fleurs'),(249,'Eaux minérales'),(250,'Barres chocolatées'),(251,'Fromages au lait cru'),(252,'Yaourts natures'),(253,'Substituts de viande'),(254,'Confiseries de Noël'),(255,'Pâtes à tartiner au chocolat'),(256,'Rillettes de poissons'),(257,'Crèmes dessert'),(258,'Fromages blancs'),(259,'Sucres'),(260,'Fruits tropicaux'),(261,'Biscuits fourrés'),(262,'Farines de céréales'),(263,'Beignets sucrés'),(264,'Amandes'),(265,'Jus multifruits'),(266,'Steaks de bœuf'),(267,'Préparations de viande'),(268,'Champignons et produits dérivés'),(269,'Steaks'),(270,'Cafés en dosettes'),(271,'Bonbons gélifiés'),(272,'Pains spéciaux'),(273,'Poulets cuisinés'),(274,'Veloutés'),(275,'Steaks hachés'),(276,'Steaks de bœuf hachés'),(277,'Pâtes à tartiner aux noisettes'),(278,'Sorbets'),(279,'Yaourts sucrés'),(280,'Bières blondes'),(281,'Riz long grain'),(282,'Bloc de foie gras'),(283,'Additifs alimentaires'),(284,'Tartes sucrées'),(285,'Olives vertes'),(286,'Chipolatas'),(287,'Boissons fermentées'),(288,'Thés verts'),(289,'Sauces salades'),(290,'Cacaos et chocolats en poudre'),(291,'Galettes de céréales soufflées'),(292,'Panettone'),(293,'Boudins'),(294,'Veloutés de légumes'),(295,'Bouillons'),(296,'Thés glacés'),(297,'Légumes tiges'),(298,'Touron'),(299,'Boissons lactées fermentées'),(300,'Compléments pour le Bodybuilding'),(301,'Pains au chocolat'),(302,'Plats au canard'),(303,'Biscuits secs'),(304,'Crustacés'),(305,'Ravioli'),(306,'Barres de céréales'),(307,'Champignons'),(308,'Sodas au cola'),(309,'Boissons au thé'),(310,'Fruits à coques décortiqués'),(311,'Pâtés de porc'),(312,'Crêpes'),(313,'Donuts'),(314,'Moulages en chocolat'),(315,'Alcools artisanaux'),(316,'Sels'),(317,'Terrines de campagne'),(318,'Viandes fraîches'),(319,'Pâtes à tartiner aux noisettes et au cacao'),(320,'Fromages à pâte persillée'),(321,'Fromages à pâte filée'),(322,'Œufs de poules'),(323,'Yaourts brassés'),(324,'Jus de fruits à base de concentré'),(325,'Aliments de Pâques'),(326,'Fromages râpés'),(327,'Céréales au chocolat'),(328,'Pommes de terre préfrites surgelées'),(329,'Ketchup'),(330,'Rillettes de viande blanche'),(331,'Sauces Pesto'),(332,'Pizzas et tartes surgelées'),(333,'Produits de montagne'),(334,'Lentilles'),(335,'Fruits en conserve'),(336,'Sauces pour pâtes'),(337,'Pâtés de campagne'),(338,'Beurres de fruits à coques'),(339,'Rillettes de volaille'),(340,'Chewing-gum'),(341,'Miels français'),(342,'Plantes aromatiques'),(343,'Yaourts à boire'),(344,'Fromages des Pays-Bas'),(345,'Taboulés'),(346,'Vinaigrettes'),(347,'Gaufres'),(348,'Thons en conserve'),(349,'Sirops simples'),(350,'Fromages à tartiner'),(351,'Maquereaux'),(352,'Tapenades'),(353,'Fromages industriels'),(354,'Jus de pommes pur jus'),(355,'Plats préparés déshydratés'),(356,'Tomates'),(357,'Soupes de poissons'),(358,'Spaghetti'),(359,'Gratins'),(360,'Purées'),(361,'Oignons et dérivés'),(362,'Bières artisanales'),(363,'Margarines'),(364,'Alcools forts'),(365,'Chips de pommes de terre aromatisées'),(366,'Macarons'),(367,'Crevettes'),(368,'Bières françaises'),(369,'Galettes des rois'),(370,'Tartelettes'),(371,'Foies gras de canard entiers'),(372,'Yaourts aromatisés'),(373,'Non alimentaire'),(374,'Yaourts à la grecque'),(375,'Beurres demi-sel'),(376,'Chips de maïs'),(377,'Entrées'),(378,'Abats'),(379,'Mozzarella'),(380,'Cidres'),(381,'Boudins blancs'),(382,'Houmous'),(383,'Mollusques'),(384,'Chocolats en poudre'),(385,'Mueslis aux fruits'),(386,'Aiguillettes de poulet'),(387,'Pâtes à tarte'),(388,'Fromages à pâte persillée français'),(389,'Pizzas surgelées'),(390,'Pains grillés'),(391,'Pickles de légumes'),(392,'Fruits au sirop'),(393,'Yaourts au lait de vache'),(394,'Filets de maquereaux'),(395,'Emmentals français'),(396,'Thons au naturel'),(397,'Vinaigres balsamiques'),(398,'Préparations de viande bovine'),(399,'Yaourts entiers'),(400,'Boissons light'),(401,'Vins blancs'),(402,'Tartes salées'),(403,'Cacahuètes'),(404,'Reblochons'),(405,'Noix de cajou'),(406,'Pâtes fraîches'),(407,'Lasagnes préparées'),(408,'Riz parfumés'),(409,'Confitures de framboises'),(410,'Desserts végétaliens'),(411,'Cookies au chocolat'),(412,'Farines de blé'),(413,'Camemberts'),(414,'Allumettes de porc'),(415,'Terrines de volailles'),(416,'Nougats'),(417,'Eaux-de-vie'),(418,'Confitures multifruits'),(419,'Biscuits au chocolat au lait'),(420,'Galettes de riz soufflé'),(421,'Haricots verts'),(422,'Bordeaux'),(423,'Nouilles instantanées'),(424,'Herbes aromatiques'),(425,'Chocolats aux noisettes'),(426,'Fromages en tranches'),(427,'Préparations pour desserts'),(428,'Riz de variété indica'),(429,'Croûtons'),(430,'Canards'),(431,'Sodas aux fruits'),(432,'Viandes séchées'),(433,'Yaourts au lait de brebis'),(434,'Parmigiano Reggiano'),(435,'Assortiments de bonbons de chocolat'),(436,'Goudas'),(437,'Sodas light'),(438,'Lardons de porc'),(439,'Soupes déshydratées'),(440,'Jambons Serrano'),(441,'Chocolats blancs'),(442,'Biscottes'),(443,'Bananes'),(444,'Pizzas au fromage'),(445,'Caramels'),(446,'Goûters et desserts pour bébé'),(447,'Chocolats fourrés'),(448,'Croissants'),(449,'Haricots'),(450,'Moutardes de Dijon'),(451,'Puddings'),(452,'Beurres de cacahuètes'),(453,'Beurres de légumineuses'),(454,'Viandes surgelées'),(455,'Gnocchi'),(456,'Bouillons déshydratés'),(457,'Spiruline'),(458,'Terrines de canard'),(459,'Surimi'),(460,'Biscuits apéritifs soufflés'),(461,'Crèmes épaisses'),(462,'Plats principaux pour bébé'),(463,'Cassoulets'),(464,'Abricots secs'),(465,'Gaufrettes'),(466,'Barres protéinées'),(467,'Open Beauty Facts'),(468,'Aides à la pâtisserie'),(469,'Fruits rouges'),(470,'Olives dénoyautées'),(471,'Eaux minérales naturelles');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `brands` varchar(500) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `url` varchar(500) NOT NULL,
  `nutrition_grade` char(1) DEFAULT NULL,
  `fat` float DEFAULT NULL,
  `saturated_fat` float DEFAULT NULL,
  `sugar` float DEFAULT NULL,
  `salt` float DEFAULT NULL,
  `id_category` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_idx` (`id_category`),
  CONSTRAINT `id` FOREIGN KEY (`id_category`) REFERENCES `category` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-01-18 11:13:51
