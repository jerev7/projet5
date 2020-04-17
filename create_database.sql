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
    stores VARCHAR(150) NOT NULL,
    url VARCHAR(150) NOT NULL,
    PRIMARY KEY (id)
)
ENGINE=INNODB;

CREATE TABLE Product_category (
    category_id INT UNSIGNED,
    product_id INT UNSIGNED,
    PRIMARY KEY (category_id, product_id)
)
ENGINE=INNODB;

CREATE TABLE Product_saved (
    product_selected_id INT UNSIGNED,
    substitution_product_id INT UNSIGNED,
    PRIMARY KEY (product_selected_id, substitution_product_id)
)
ENGINE=INNODB;
