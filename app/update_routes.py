from  flask import jsonify,request

def product_update(collection_name,name):
    productlist = collection_name
    try:
        try:
            brand_name = request.json['brand_name']
            regular_price_value = request.json['regular_price_value']
            offer_price_value = request.json['offer_price_value']
            currency = request.json['currency']
            image_url = request.json['image_url']
            classification_l1 = request.json['classification_l1']
            classification_l2 = request.json['classification_l2']
            classification_l3 = request.json['classification_l3']
            classification_l4 = request.json['classification_l4']
        except:
            return not_found()
            
        if brand_name and regular_price_value and offer_price_value and currency and image_url and classification_l1 and classification_l2 and classification_l3 and classification_l4 and request.method == 'PUT' :
            productlist.update_one({'name':product_name},{'$set':{'brand_name':brand_name,'regular_price_value':regular_price_value,'offer_price_value':offer_price_value,'currency':currency,'image_url':image_url,'classification_l1':classification_l1,'classification_l2':classification_l2,'classification_l3':classification_l3,'classification_l4':classification_l4}})
            output = {'Status code': 200 ,'Message': 'Product successfully updated'}
            return jsonify({'result':output})
        else:
            return not_found()
    except:
        return not_found()
        
def not_found():
    output = {'Status code': 404 ,'Message': 'Not found Error Occured'+request.url}
    return jsonify({'Error':output})
