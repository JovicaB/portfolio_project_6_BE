CREATE TABLE `p6_random_url` (
  `id` int NOT NULL AUTO_INCREMENT,
  `random_url` varchar(45) DEFAULT NULL,
  `url_expiration` varchar(45) DEFAULT NULL,
  `user_identifier` varchar(45) DEFAULT NULL,
  `pi_code` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
