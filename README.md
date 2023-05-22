# progWeb-m2-backend
Link para o Figma: https://www.figma.com/file/eX6HxXcOHGVOiMZ59TbYnw/Uni-Ride-DataBase?type=whiteboard&node-id=0-1&t=0RM6ONR0pRRlq53S-0

Trabalho feito com objetivo de obter nota parcial da segunda média da disciplina de Programação Web. 
Consiste em um Backend produzido com base em um protótipo feito em um trabalho anterior, para isso foram feitos endpoints para 3 CRUDS de tabelas presentes no protótipo. 

Link para o Figma: https://www.figma.com/file/eX6HxXcOHGVOiMZ59TbYnw/Uni-Ride-DataBase?type=whiteboard&node-id=0-1&t=0RM6ONR0pRRlq53S-0

Executar os seguintes comandos para criar a o banco: 

CREATE DATABASE `uniride` ;

CREATE TABLE `uniride`.`usuario` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(255) NOT NULL,
  `senha` VARCHAR(20) NOT NULL,
  `data_nasc` DATE NOT NULL,
  `sexo` INT NOT NULL,
  `cidade` VARCHAR(255) NOT NULL,
  `bairro` VARCHAR(255) NOT NULL,
  `insta` VARCHAR(255) NULL,
  `email` VARCHAR(255) NOT NULL,
  `telefone` VARCHAR(255) NOT NULL,
  `foto` VARCHAR(255) NOT NULL,
  `nota` FLOAT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;

CREATE TABLE `uniride`.`motorista` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `carro` VARCHAR(45) NOT NULL,
  `placa` VARCHAR(45) NOT NULL,
  `usuario_id` INT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;

CREATE TABLE `uniride`.`carona` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `cidade` VARCHAR(255) NOT NULL,
  `bairro` VARCHAR(255) NOT NULL,
  `obs` VARCHAR(255) NOT NULL,
  `horario` TIME NOT NULL,
  `dias` VARCHAR(10) NOT NULL,
  `motorista_id` INT NOT NULL,
  `passageiro_id1` INT NOT NULL,
  `passageiro_id2` INT NOT NULL,
  `passageiro_id3` INT NOT NULL,
  `passageiro_id4` INT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;
