# REST-API-using-FLASK-and-MONGODB
Its a basic flask API which performs the CRUD function and few range operations and uses mongodb as a database and deploy the API Locally using using docker and hosting the database on **MongoDB Atlas** clusture and for Client we use **MongoDB Compass**.
FAQ regarding the Project 
<h3>How to deploy the docker container </h3>
You must have Docker setup on your System secondly Create the Dockerfile in the directory which contain your project .
Check out the Dockerfile uploaded in the main branch .
run the following command to Containerize the API -<br>
STEP 1 :<code>docker build --tag flask-demo .</code>
<br>the output should look something similar to this -<br>

<br>[+] Building 43.6s (9/9) FINISHED                                                                            
<br> => [internal] load build definition from Dockerfile                                                           1.5s
<br>=>  transferring dockerfile: 32B                                                                                0.2s
<br> => [internal] load .dockerignore                                                                               0.9s
<br> =>  transferring context: 2B                                                                                    0.1s
<br> => [internal] load metadata for docker.io/library/python:3                                                      4.7s
<br>=> [internal] load build context                                                                                 0.6s
<br>=>  transferring context: 391B                                                                                  0.2s
<br>=> CACHED [1/4] FROM docker.io/library/python:3@sha256:73cc381fa0fe5e6d5dd38f1397da28c70096519d8818c2249f       0.0s
<br>=> [2/4] COPY requirements.txt .                                                                                 1.0s
<br> => [3/4] RUN pip3 install  -r requirements.txt                                                                   29.0s
<br>=> [4/4] COPY . .                                                                                                 1.6s
<br>=> exporting to image                                                                                             4.1s
<br> =>  exporting layers                                                                                            3.3s
<br>=>  writing image sha256:d293d8687cc4371c1934dac035c98cb034cfbc4e3f3d1f3cb471f1                                  0.1s
<br>=>  naming to docker.io/library/flask-demo 
 
 <br>**STEP 2 :**<code>docker run --name flask-demo -p 5000:5000 flask-demo</code>
 <br>the output should look something similar to this -<br>
 
<br>  * Running on all addresses.
 <br>  WARNING: This is a development server. Do not use it in a production deployment.
 <br> * Running on http://IP:5000/ (Press CTRL+C to quit)
 <br> * Restarting with stat
 <br> * Serving Flask app 'app' (lazy loading)
 <br> * Environment: production
 <br>   WARNING: This is a development server. Do not use it in a production deployment.
 <br>   Use a production WSGI server instead.
 <br>  * Debug mode: on
 <br> * Debugger is active!
 <br> * Debugger PIN: 123-456-789
 
 <br>**STEP 3 :** 
 <br>after starting on browser -
 <br>visit localhost:5000 and check 
 <br>the terminal will show a log like this -
 <br><code>172.17.0.1 - - [03/Jun/2021 09:37:09] "GET / HTTP/1.1" 200 - </code>
 
 
<h3>How to access APIs on localhost. </h3>
To access API on localhost, Flask engine by default uses the 5000 port and for running ont he localhost you can directly run by specifying the parameter such as hsotname in app.run()
<br>
<code>
<br>app = Flask(__name__) </code>
<br><code>if __name__ == '__main__': </code>
<br><code>    app.run(host= "0.0.0.0" port=5000 debug=True)
</code>

<h3>How to use these APIs to list, add, delete or update products. </h3>
The List of routes to use and Method they use -- <br> 
<ol>
<li>/add uses the POST Method to add the Product to the productlist collection and Productdb Database.use ex - localhost:5000/add </li>
<li>/get uses the GET Method to get the list of all the products in the collection productlist . use ex - localhost:5000/get </li>
<li>/get/product_name uses the GET Method to get the specific product that they want and related details to that product . use ex- localhost:5000/get/jelly cat</li>
<li>/update/product_name uses the PUT Method and update the infomraiton passed of the specific product name mentioned use ex- localhost:5000/update/jelly cat</li>
<li>/delete/product_name uses the DELETE Method to delete the specidic product name to delete the record matchin with the specific product name use ex- localhost:5000/delete/jelly cat </li>
</ol>



 
