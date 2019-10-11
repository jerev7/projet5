CREATE TABLE Products1 (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    category VARCHAR(100) NOT NULL,
    brand VARCHAR(100), 
    conditioning VARCHAR(100),
    labels VARCHAR(100),
    ingredients_origin VARCHAR(100),
    manufacturing_place VARCHAR(100),
    PRIMARY KEY (id)

    )
ENGINE=INNODB;