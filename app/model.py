from app import app 
from flask import Flask , jsonify , request
from flask_pymongo import PyMongo
from pymongo import MongoClient
from app import post_routes , get_routes , delete_routes , update_routes

#app.config['MONGO_DBNAME'] = 'Productdb'
#app.config['MONGO_URI'] = "mongodb://localhost:27017/Productdb"

client = MongoClient("mongodb+srv://<username>:<password>@cluster0.zyipb.mongodb.net/Productdb?retryWrites=true&w=majority")
db = client['Productdb']

#mongo = PyMongo(app)

@app.route("/")
def get_initial_response():
    # Welcome message for the API.
    # Message to the user
    message = {
        'apiVersion': 'v1.0',
        'status': '200',
        'message': 'Welcome to the Flask API'
    }
    # Making the message looks good
    response = jsonify(message)
    # Returning the object
    return response




@app.route('/add', methods=['POST'])
def add_product():
    #fetching the collection instance in an object
    productlist = db.productlist
    #fetching and validating the json send by user
    response = post_routes.add_OneProduct(productlist)
    return response

@app.route('/get',methods=['GET'])
def get_ProductList():
    #fetching the collection instance in an object
    productlist = db.productlist
    # we make initialize a  empty list output to store the data fetched
    response = get_routes.get_AllProduct(productlist)
    return response

@app.route('/get/<name>', methods=['GET'])
def get_Oneproduct(name):
    #fetching the collection instance in an object
    productlist = db.productlist
    # fetch the product with the name passed
    response = get_routes.getOne_product(productlist,name)
    return response

@app.route('/delete/<name>', methods=['DELETE'])
def delete_product(name):
    #fetching the collection instance in an object
    product_name = name
    productlist = db.productlist
    #delete the item matching witht the name passed
    response = delete_routes.product_delete(productlist,product_name)
    return response

@app.route('/update/<name>',methods=['PUT'])
def update_product(name):
    product_name = name
    #fetching the collection instance in an object
    productlist = db.productlist
    response = update_routes.product_update(productlist,product_name)
    return response


        
@app.route('/list_unique_brands',methods=['GET'])
def unique_productList():
    productlist = db.productlist
    response = get_routes.uniqueProduct_list(productlist)
    return response



@app.route('/count_high_offer_price', methods=['GET'])
def highofferprice_product():
    productlist = db.productlist
    response = get_routes.higher_offerProduct(productlist)
    return response


@app.route('/count_discounted_products', methods=['GET'])
def discounted_product():
    productlist = db.productlist
    response = get_routes.discountedProduct(productlist)
    return response

@app.route('/count_high_discount', methods=['GET'])
def highDiscount_product():
    productlist = db.productlist
    response = get_routes.high_DiscountedProduct(productlist)
    return response


        

    

     
        
