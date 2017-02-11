DROP TABLE IF EXISTS `articles`;
CREATE TABLE `articles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(45) NOT NULL,
  `body` varchar(255) NOT NULL,
  `url` varchar(255) NOT NULL,
  `thumbnail` varchar(255) DEFAULT NULL,
  KEY `id` (`id`)
);
LOCK TABLES `articles` WRITE;

INSERT INTO `articles` (`id`, `title`, `body`, `url`, `thumbnail`)
VALUES
(1, 'タイトル1', 'ボディー1', 'google.com', NULL),
(2, 'タイトル2', 'ボディー2', 'yahoo.com', NULL);
