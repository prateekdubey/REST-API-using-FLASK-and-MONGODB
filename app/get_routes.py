from flask import jsonify , request

def get_AllProduct(collection_name):
    productlist = collection_name
    output = []
    try:
        # we loop over the data to fetch the result 
        for i in productlist.find():
            output.append({'name': i['name'],
                           "brand_name": i['brand_name'],
                           "regular_price_value":i["regular_price_value"],
                           "offer_price_value":i["offer_price_value"],
                           "currency":i["currency"],
                           "classification_l1":i["classification_l1"],
                           "classification_l2":i["classification_l2"],
                           "classification_l3":i["classification_l3"],
                           "classification_l4":i["classification_l4"],
                           "image_url":i["image_url"]})

        #return the output in json format
        return jsonify({'result':output})
    except :
        return not_found()
    
def getOne_product(collection_name,name):
    productlist = collection_name
    try :
        q = productlist.find_one({'name':name})
        if q :
            output = {"name" : q["name"],
                      "brand_name": q["brand_name"],
                      "regular_price_value":q["regular_price_value"],
                      "offer_price_value":q["offer_price_value"],
                      "currency":q["currency"],
                      "classification_l1":q["classification_l1"],
                      "classification_l2":q["classification_l2"],
                      "classification_l3":q["classification_l3"],
                      "classification_l4":q["classification_l4"],
                      "image_url":q["image_url"]}
        else :
            output = "No result found"
        return jsonify({'result': output})
    except :
        return not_found()

def uniqueProduct_list(collection_name):
    productlist = collection_name
    try :
        output = {"Number of unique product" : len(productlist.distinct('brand_name',{'brand_name':{'$ne' : "" }})),"List of unique brands" : productlist.distinct('brand_name',{'brand_name':{'$ne' : "" }})}
        return jsonify({'result':output})
    except:
        return not_found()
    
def higher_offerProduct(collection_name):
    productlist = collection_name
    try :
        output = productlist.find({'offer_price_value':{'$gt' : 300}}).count()
        return jsonify({'result':output})
    except:
        return not_found()
    
def discountedProduct(collection_name):
    productlist = collection_name
    try:
        output = []
        for i in productlist.find():
            if i['offer_price_value'] < i['regular_price_value'] :
                output.append({'_id':i['_id']})
        
        return jsonify({'result':len(output)})
    except:
        return not_found()
    
def high_DiscountedProduct(collection_name):
    productlist = collection_name
    try:
        output = []
        for i in productlist.find():
            discount = float(i['regular_price_value']) - float(i['offer_price_value']) 
            discount_percent = discount / float(i['regular_price_value'])
            if discount_percent > 0.30 :
                output.append({'_id':i['_id']})
        return jsonify({'result':len(output)})
    except :
        return not_found()

def not_found(error = None):
    output = {'Status code': 404 ,'Message': 'Not found Error Occured' + request.url}
    return jsonify({'Error':output})


