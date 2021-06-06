from flask import jsonify , request

def product_delete(collection_name,name):
    productlist = collection_name
    try :
        query = productlist.delete_one({'name':name})
        output = {'Status code': 200 ,'Message': 'Product successfully deleted'}
        return jsonify({'result':output})
    except :
        return not_found()

def not_found():
    output = {'Status code': 404 ,'Message': 'Not found Error Occured' + request.url}
    return jsonify({'Error':output})
    
    
        
    

    
