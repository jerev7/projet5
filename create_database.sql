ENGINE=INNODB;

CREATE TABLE Category (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    name VARCHAR(150) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE Product (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    product_name VARCHAR(150) NOT NULL,
    nutriscore CHAR(1) NOT NULL,
    palm_oil VARCHAR(3) NOT NULL, # yes or no
    gluten VARCHAR(3) NOT NULL, # yes or no
    PRIMARY KEY (id)
);

CREATE TABLE Product_category (
    category_id INT UNSIGNED,
    product_id INT UNSIGNED,
    PRIMARY KEY (category_id, product_id)
);

CREATE TABLE Ingredients (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    ingredient_name VARCHAR(150) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE Product_ingredients (
    product_id INT UNSIGNED,
    ingredient_id INT UNSIGNED,
    PRIMARY KEY (product_id, ingredient_id)
);

CREATE TABLE Selling_location (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    location_name VARCHAR(150) NOT NULL,
);

CREATE TABLE Product_selling_location (
    product_id INT UNSIGNED,
    location_id INT UNSIGNED,
    PRIMARY KEY (product_id, location_id)
);
