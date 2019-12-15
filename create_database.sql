CREATE TABLE Category (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    name VARCHAR(150) NOT NULL,
    PRIMARY KEY (id)
)
ENGINE=INNODB;

CREATE TABLE Product (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    product_name VARCHAR(150) NOT NULL,
    nutriscore CHAR(1) NOT NULL,
    palm_oil BOOLEAN NOT NULL, # yes or no
    gluten BOOLEAN NOT NULL, # yes or no
    url VARCHAR(150),
    PRIMARY KEY (id)
)
ENGINE=INNODB;

CREATE TABLE Product_category (
    category_id INT UNSIGNED,
    product_id INT UNSIGNED,
    PRIMARY KEY (category_id, product_id)
)
ENGINE=INNODB;

CREATE TABLE Ingredients (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    ingredient_name VARCHAR(150) NOT NULL,
    PRIMARY KEY (id)
)
ENGINE=INNODB;

CREATE TABLE Product_ingredients (
    product_id INT UNSIGNED,
    ingredient_id INT UNSIGNED,
    PRIMARY KEY (product_id, ingredient_id)
)
ENGINE=INNODB;

CREATE TABLE Selling_location (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    location_name VARCHAR(150) NOT NULL,
    PRIMARY KEY (id)
)
ENGINE=INNODB;

CREATE TABLE Product_selling_location (
    product_id INT UNSIGNED,
    location_id INT UNSIGNED,
    PRIMARY KEY (product_id, location_id)
)
ENGINE=INNODB;