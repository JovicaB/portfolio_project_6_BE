CREATE TABLE `login` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `user_mail` varchar(45) DEFAULT NULL,
  `user_name` varchar(45) DEFAULT NULL,
  `test_duration` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
