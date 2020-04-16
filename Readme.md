###### Project 5 :

**_Description :_**

We use « Openfoodfacts » API to provide you a list of products. 
After you chose a product, the program will try to find a healthier product to offer you instead.

On the main window click on « Which product would you like to replace ? »
Then you have to select a category, then the product you want and click on "Search a substitution product" 
Below you will see a new table where you can choose a substitution product.
You can then save the result just by clicking the « save result » button.

You can access to all saved products from the main window by clicking on « Saved products »
 
**_Installation instructions :_**

If you don't have python3 installed on your system do it first following this link : https://www.python.org/downloads/
Download all the files then open a terminal, go in the folder where you put the files and run this command :
```
pip install -r requirements.txt
```
You will have to use your own database for this program to work.
First create the SQL database on your system then run the script « create_database.sql »
Then open class_menu.py with a text editor and go to line 17 :
```
	host=here just leave « localhost »
	user=<here put your username>
	passwd=<here goes your password>»
	database=<here put your database name>
```
Save your changes then close the file.
You can now start the program by launching the file « main.py ».

