CREATE TABLE `p6_results` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_identifier` varchar(45) CHARACTER SET utf8 DEFAULT NULL,
  `pi_code` varchar(5) CHARACTER SET utf8 DEFAULT NULL,
  `examinee_name` varchar(45) CHARACTER SET utf8 DEFAULT NULL,
  `results` text CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=387 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
