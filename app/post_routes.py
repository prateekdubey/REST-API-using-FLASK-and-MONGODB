from flask import jsonify,request




def add_OneProduct(collection_instance):
    #fetching the collection instance in an object
    productlist = collection_instance
    #fetching and validating the json send by user
    #fields under this try block are the required (compulsory) feilds
    try :
        name = request.json['name']                     
        brand_name = request.json['brand_name']         
        regular_price_value = request.json['regular_price_value']   
        offer_price_value = request.json['offer_price_value']
        currency = request.json['currency']
        image_url = request.json['image_url']
    except :
        return not_found()
     #In case any of the fields are missing this function will return a 404 error with message
    #fields under this try block's are non-complusory fields and may be entered by the users
    try :
        classification_l1 = request.json['classification_l1']
    except :
        classification_l1 = ""                             # In case the value of classification_l1 is not entered we give it no value by default 
    try :
        classification_l2 = request.json['classification_l2']
    except :
        classification_l2 = ""                             # In case the value of classification_l1 is not entered we give it no value by default
    try :
        classification_l3 = request.json['classification_l3']
    except :
        classification_l3 = ""                              # In case the value of classification_l1 is not entered we give it no value by default
    try :
        classification_l4 = request.json['classification_l4']
    except :
        classification_l4 = ""                              # In case the value of classification_l1 is not entered we give it no value by default
        
    #Insert the data into the database which will return the unique id 
    product_id = productlist.insert({"name": name ,
                                     "brand_name" : brand_name ,
                                     "regular_price_value" : regular_price_value ,
                                     "offer_price_value": offer_price_value,
                                     "currency" : currency,
                                     "classification_l1":classification_l1,
                                     "classification_l2":classification_l2,
                                     "classification_l3":classification_l3,
                                     "classification_l4":classification_l4,
                                     "image_url":image_url})
    #Find the recently inserted data into the database by the unique id for displaying in the output
    new_product = productlist.find_one({'_id': product_id})

    #fetch the fields from the 
    output = {"name":new_product["name"],
              "brand_name": new_product["brand_name"],
              "regular_price_value":new_product["regular_price_value"],
              "offer_price_value":new_product["offer_price_value"],
              "currency":new_product["currency"],
              "classification_l1":new_product["classification_l1"],
              "classification_l2":new_product["classification_l2"],
              "classification_l3":new_product["classification_l3"],
              "classification_l4":new_product["classification_l4"],
              "image_url":new_product["image_url"]}
    
    # return the output in a json format 
    return jsonify({'result':output,
                    'Status code':200,
                    'Message':'Product succesfully added'})

def not_found(error = None):
    output = {'Status code': 404 ,'Message': 'Not found Error Occured'+request.url}
    return jsonify({'Error':output})
    
    
