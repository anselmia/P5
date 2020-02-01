-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema databaseName
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema databaseName
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `databaseName` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;

-- -----------------------------------------------------
-- Table `databaseName`.`category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `databaseName`.`category` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` TEXT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `databaseName`.`product`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `databaseName`.`product` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,
  `brands` VARCHAR(500) NULL DEFAULT NULL,
  `url` VARCHAR(500) NOT NULL,
  `nutrition_grade` CHAR(1) NULL DEFAULT NULL,
  `fat` FLOAT NULL DEFAULT NULL,
  `saturated_fat` FLOAT NULL DEFAULT NULL,
  `sugar` FLOAT NULL DEFAULT NULL,
  `salt` FLOAT NULL DEFAULT NULL,
  `id_category` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `id_idx` (`id_category` ASC) VISIBLE,
  CONSTRAINT `id`
    FOREIGN KEY (`id_category`)
    REFERENCES `databaseName`.`category` (`id`)
    ON DELETE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `databaseName`.`substitute`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `databaseName`.`substitute` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `id_product` INT NOT NULL,
  `id_substitute` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  UNIQUE INDEX `ucCodes` (`id_product` ASC, `id_substitute` ASC) VISIBLE,
  INDEX `id_product_idx` (`id_product` ASC) VISIBLE,
  INDEX `id_substitute_idx` (`id_substitute` ASC) VISIBLE,
  CONSTRAINT `id_product`
    FOREIGN KEY (`id_product`)
    REFERENCES `databaseName`.`product` (`id`),
  CONSTRAINT `id_substitute`
    FOREIGN KEY (`id_substitute`)
    REFERENCES `databaseName`.`product` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
