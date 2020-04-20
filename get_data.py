import requests
import mysql.connector

"""
This module is used to get all data we need from Openfoodfacts API
and insert them into our database.
"""

response = requests.get('https://fr.openfoodfacts.org/categories.json')
my_categories = response.json()["tags"]


french_cat_list = []

for cat in my_categories:
    name = (cat['name'])
    name_list = list(name)
    if len(name_list) > 2:
        if name_list[2] != ":":  # We get only french categories
            french_cat_list.append(name)


class Product:
    """
    This class will add products to our final_list.
    """
    def __init__(self, url, final_list, category):
        response2 = requests.get(url)
        my_products = response2.json()["products"]
        for prod in my_products:
            if 'product_name' in prod:
                new_entry = {}
                new_entry["name"] = prod['product_name']
                new_entry["category"] = category
                if 'ingredients_from_or_that_may_be_from_palm_oil_n' in prod:
                    palm_oil_value =
                    prod['ingredients_from_or_that_may_be_from_palm_oil_n']
                    new_entry["palm_oil"] = palm_oil_value
                else:
                    new_entry["palm_oil"] = 0
                if 'traces' in prod:
                    traces_value = prod['traces']
                    if "gluten" in traces_value:
                        new_entry["gluten"] = 1
                    else:
                        new_entry["gluten"] = 0
                else:
                    new_entry["gluten"] = 0
                if 'url' in prod:
                    new_entry["url"] = prod['url']
                else:
                    new_entry["url"] = "no url found"
                if 'stores' in prod:
                    new_entry["stores"] = prod['stores']
                else:
                    new_entry["stores"] = "no stores found"
                final_list.append(new_entry)


final_list = []
pages = range(1, 2)  # Number products page per category
for category in french_cat_list[:12]:  # Number of categories used
    for page in pages:
        url = 'https://fr.openfoodfacts.org/categorie/' +\
             category + '/' + str(page) + '.json'
        products = Product(url, final_list, category)

# Database connection information
mydb = mysql.connector.connect(
  host="localhost",
  user="jerev7",
  passwd="Sally_95540",
  database="openfoodfacts"
)

mycursor = mydb.cursor()

"""
We insert all product data in our database.
"""
sql1 = """INSERT INTO Product (product_name,
          nutriscore, palm_oil, gluten, stores, url)
          VALUES (%s, %s, %s, %s, %s, %s)"""
sql2 = "INSERT INTO Category (name) VALUES (%s)"
sql3 = """INSERT INTO Product_category (category_id, product_id)
          VALUES (%s, %s)"""

val1 = []
val2 = []
for product in final_list[:300]:
    nutriscore = (0 + (int(product["palm_oil"])) + (int(product["gluten"])))
    product_result = (product["name"], nutriscore, product["palm_oil"],
                      product["gluten"], product["stores"], product["url"])
    category = (product["category"],)
    if product_result[0] != "":
        val1.append(product_result)
    if cate not in val2:
        val2.append(category)

insert_ids_p = []
insert_ids_c = []
for value in val1:
    mycursor.execute(sql1, value)
    insert_ids_p.append(mycursor.lastrowid)
for value in val2:
    mycursor.execute(sql2, value)
    insert_ids_c.append(mycursor.lastrowid)

val3 = []
for product, idp in zip(final_list[:300], insert_ids_p):
    numero_cat = val2.index((product["category"],))
    idc = insert_ids_c[numero_cat]
    val3.append((idc, idp))

mycursor.executemany(sql3, val3)
mydb.commit()
