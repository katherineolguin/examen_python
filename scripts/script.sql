-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema examen_python
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema examen_python
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `examen_python` DEFAULT CHARACTER SET utf8mb3 ;
USE `examen_python` ;

-- -----------------------------------------------------
-- Table `examen_python`.`clientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `examen_python`.`clientes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL DEFAULT NULL,
  `numero_cuenta` INT NULL DEFAULT NULL,
  `saldo` INT NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `examen_python`.`retiros`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `examen_python`.`retiros` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `retiro` INT NULL,
  `detalle` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `cliente_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_retiros_clientes_idx` (`cliente_id` ASC) VISIBLE,
  CONSTRAINT `fk_retiros_clientes`
    FOREIGN KEY (`cliente_id`)
    REFERENCES `examen_python`.`clientes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
