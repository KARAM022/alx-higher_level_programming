-- 5. Full description
SELECT CONCAT('first_tableCREATE TABLE `first_table` (\n',
             ' `id` int NOT NULL AUTO_INCREMENT,\n',
             ' `name` varchar(128) DEFAULT NULL,\n',
             ' `c` char(1) DEFAULT NULL,\n',
             ' `created_at` date DEFAULT NULL,\n',
             ' PRIMARY KEY (`id`)\n',
             ') ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci') AS CreateTable
FROM information_schema.tables
WHERE table_schema = 'hbtn_0c_0' AND table_name = 'first_table';
