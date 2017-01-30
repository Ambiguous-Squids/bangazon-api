===============
bangazon-api
===============

##Description

This is a REST API created for the Bangazon LLC. The API will be used to house and track customers, products, product types, orders, and payment types for Bangazon LLC. Customers of Bangazon LLC can be create and/or order products.

##Installation

1.  Make sure you have Python 3.6.0 installed. See instructions for download here:
    https://www.python.org/downloads/

2.  Virtualenv is probably what you want to use during development, and if you have shell access to your production
    machines, you’ll probably want to use it there, too.

3.  Requirements.txt contains all the external dependencies for the api.

4.  Go into the project's root folder and follow the "How to Run" instructions below.

##Requirements
    * Django==1.10.5
    * djangorestframework==3.5.3

##How to Run

###MAC
Create a virtual environment
```
python -m venv venv
```
Activate the virtual environment
```
source venv/bin/activate
```
Install all dependencies in requirements.txt
```
pip install -r requirements.txt
```
To deactivate the virtual environment
```
deactivate
```

###WINDOWS
Install virtual env and wrapper
```
pip install virtualenvwrapper-win
```
Create a virtual environment
```
mkvirtualenv myproject
```
Activate the virtual environment
```
workon myproject
```
Install all dependencies in requirements.txt
```
pip install -r requirements.txt
```
To deactivate the virtual environment
```
deactivate
```

###After creating a virtualenv
Change into the bangazon directory
```
cd bangazon/
```
Make the migrations script in the migrations folder for each app
```
./manage.py makemigrations
```
Run the migrations script to create the database
```
./manage.py migrate
```
Now, run the server
```
./manage.py runserver
```
> Performing system checks...<br><br>
> System check identified no issues (0 silenced).<br>
> Django version 1.10.5, using settings 'bangazon.settings'<br>
> Starting development server at http://127.0.0.1:8000/<br>
> Quit the server with CONTROL-C.<br>

Go to localhost in browser
```
http://127.0.0.1:8000/
```
To login as admin
```
username: admin
password: password123
```

##How to use

###Collections
```
* GET - http://127.0.0.1:8000/products          returns all products
* GET - http://127.0.0.1:8000/customers         returns all customers
* GET - http://127.0.0.1:8000/orders            returns all orders
* GET - http://127.0.0.1:8000/payment_types     returns all payment types
* GET - http://127.0.0.1:8000/product_types     returns all product types
```

###Members
```
* GET - http://127.0.0.1:8000/products/<id>          returns a product by id
* GET - http://127.0.0.1:8000/customers/<id>         returns a customer by id
* GET - http://127.0.0.1:8000/orders/<id>            returns an order by id
* GET - http://127.0.0.1:8000/payment_types/<id>     returns a payment type by id
* GET - http://127.0.0.1:8000/product_types/<id>     returns a product type by id
```

| *Parameters* | *Valid Options* | *Description*              |
|------------|---------------|--------------------------|
| format     | json          | the data type to return. |

##Example
```
// http://127.0.0.1:8000/product_types/1/?format=json

{
  "url": "http://127.0.0.1:8000/product_types/1/?format=json",
  "category": "Baseball"
}
```

##Contributors
- [Nick Chemsak](https://github.com/nchemsak)
- [Alex Simonian](https://github.com/asimonia)
- [Matt McCord](https://github.com/mccordgh)
- [Richard Whitfield](https://github.com/rwhitfield84)
- [Dani Adkins](https://github.com/itsdanirenae)

