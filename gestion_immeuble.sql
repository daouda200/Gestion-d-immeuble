CREATE database Gestion_Immeuble;

use Gestion_Immeuble;


CREATE TABLE IF NOT EXISTS `Gestion_Immeuble`.`immeuble` (
  `id_immeuble` INT NOT NULL AUTO_INCREMENT,
  `nom` VARCHAR(45) ,
  `adresse` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id_immeuble`))
ENGINE = InnoDB;



CREATE TABLE IF NOT EXISTS `Gestion_Immeuble`.`Etage` (
  `id_etage` INT NOT NULL AUTO_INCREMENT,
  `numeroetage` INT NOT NULL,
  `Immeuble_id_immeuble` INT NOT NULL,
  PRIMARY KEY (`id_etage`),
  INDEX `fk_Etage_Immeuble_idx` (`Immeuble_id_immeuble` ASC) VISIBLE,
  CONSTRAINT `fk_Etage_Immeuble`
    FOREIGN KEY (`Immeuble_id_immeuble`)
    REFERENCES `Gestion_Immeuble`.`immeuble` (`id_immeuble`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `Gestion_Immeuble`.`Locataire` (
  `id_locataire` INT NOT NULL AUTO_INCREMENT,
  `nom` VARCHAR(45) NOT NULL,
  `prenom` VARCHAR(45) NOT NULL,
  `telephone` VARCHAR(15) NOT NULL,
  `email` VARCHAR(100) NULL,
  `date_debut` DATE NOT NULL,
  `date_fin` DATE NULL,
  `montant_Loyer` FLOAT NOT NULL,
  PRIMARY KEY (`id_locataire`))
ENGINE = InnoDB;



CREATE TABLE IF NOT EXISTS `Gestion_Immeuble`.`Appartement` (
  `id_appartement` INT NOT NULL AUTO_INCREMENT,
  `numero_appartement` INT NOT NULL,
  `surface_m2` FLOAT NULL,
  `nombre_chambre` INT NOT NULL,
  `Etage_id_etage` INT NOT NULL,
  `Locataire_id_locataire` INT NULL,
  PRIMARY KEY (`id_appartement`),
  CONSTRAINT `fk_Appartement_Etage1`
    FOREIGN KEY (`Etage_id_etage`)
    REFERENCES `Gestion_Immeuble`.`Etage` (`id_etage`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Appartement_Locataire1`
    FOREIGN KEY (`Locataire_id_locataire`)
    REFERENCES `Gestion_Immeuble`.`Locataire` (`id_locataire`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `Gestion_Immeuble`.`Chambre` (
  `id_chambre` INT NOT NULL AUTO_INCREMENT,
  `numero_chambre` VARCHAR(10) NULL,
  `surface_m2` FLOAT NULL,
  `Appartement_id_appartement` INT NOT NULL,
  `Locataire_id_locataire` INT NULL,
  PRIMARY KEY (`id_chambre`),
  CONSTRAINT `fk_Chambre_Appartement1`
    FOREIGN KEY (`Appartement_id_appartement`)
    REFERENCES `Gestion_Immeuble`.`Appartement` (`id_appartement`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Chambre_Locataire1`
    FOREIGN KEY (`Locataire_id_locataire`)
    REFERENCES `Gestion_Immeuble`.`Locataire` (`id_locataire`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

insert into immeuble(nom,adresse) VALUES ("Sokhna Anta","dakar centre ville");
insert into immeuble(nom,adresse) VALUES ("Ndiougua kebe","elton mermoz");

insert into etage(numeroetage,Immeuble_id_immeuble) VALUES (1,3);
insert into etage(numeroetage,Immeuble_id_immeuble) VALUES (2,3);
insert into etage(numeroetage,Immeuble_id_immeuble) VALUES (3,3);

INSERT INTO `gestion_immeuble`.`appartement` (`numero_appartement`, `surface_m2`, `nombre_chambre`, `Etage_id_etage`) VALUES ('1', '100', '4', '2');
INSERT INTO `gestion_immeuble`.`appartement` (`numero_appartement`, `surface_m2`, `nombre_chambre`, `Etage_id_etage`) VALUES ('2', '75', '3', '2');
INSERT INTO `gestion_immeuble`.`appartement` (`numero_appartement`, `surface_m2`, `nombre_chambre`, `Etage_id_etage`) VALUES ('3', '80', '4', '3');
INSERT INTO `gestion_immeuble`.`appartement` (`numero_appartement`, `surface_m2`, `nombre_chambre`, `Etage_id_etage`) VALUES ('4', '150', '7', '4');

INSERT INTO `gestion_immeuble`.`chambre` (`numero_chambre`, `surface_m2`, `Appartement_id_appartement`) VALUES ('1', '5', '4');
INSERT INTO `gestion_immeuble`.`chambre` (`numero_chambre`, `surface_m2`, `Appartement_id_appartement`) VALUES ('2', '8', '4');
INSERT INTO `gestion_immeuble`.`chambre` (`numero_chambre`, `surface_m2`, `Appartement_id_appartement`) VALUES ('3', '10', '4');

select * from locataire,appartement where locataire.id_locataire=appartement.Locataire_id_locataire;

alter table locataire ADD libelle_contrat TEXT;
