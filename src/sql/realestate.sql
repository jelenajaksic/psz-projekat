-- db.realestate definition

CREATE TABLE `realestate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `property_type` enum('a','h') DEFAULT NULL,
  `location` char(50) DEFAULT NULL,
  `add_type` enum('r','s') DEFAULT NULL,
  `size` float DEFAULT NULL,
  `year` int(11) DEFAULT NULL,
  `area` float DEFAULT NULL,
  `storey` int(11) DEFAULT NULL,
  `total_storeys` int(11) DEFAULT NULL,
  `registered` tinyint(1) DEFAULT NULL,
  `heat_type` char(50) DEFAULT NULL,
  `rooms` float DEFAULT NULL,
  `toiletes` int(11) DEFAULT NULL,
  `parking` tinyint(1) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `other` char(100) DEFAULT NULL,
  `url` char(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25408 DEFAULT CHARSET=utf8mb4;