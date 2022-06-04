import flask 
import os 
import uuid
import json
from flask import request ,jsonify
import redis
from flask import Response

hostname=os.getenv('HOSTNAME', '0.0.0.0')
port= os.getenv('PORT','7474')
redis_port = os.getenv('REDIS_PORT','6379')
redis_host = os.getenv('REDIS_HOST','192.168.0.110')
redis_password = os.getenv('REDIS_PASSWORD','secret_password')

app= flask.Flask(__name__)
app.config['DEBUG'] = True

PREF='KEY-'

@app.route('/health',methods=['GET'])
def server():
    return "<H1>Server is at Good Health </H1>"


@app.route('/api/v1/resources/address',methods=['GET'])
def api_all():
    try:
      
      redis_connection  = redis.Redis(host=redis_host,port=int(redis_port),password=redis_password)
      listOfAddress = []
      for key in redis_connection.keys(PREF+'*'):
          address_object = redis_connection.get(key)
          address_object_json = json.loads(address_object)
          listOfAddress.append(address_object_json)

      redis_connection.close()
      print('get all executed')
      return Response(str(listOfAddress), status=200, mimetype='application/json')
    except Exception as e:
      print(e)
      return Response("{\"error\":\"Unable To Get All Address '"+str(e)+"\"}", status=400, mimetype='application/json')


@app.route('/api/v1/resources/address/<address_key>',methods=['PUT'])
def api_update(address_key):
    try:

      print("Request Received")
      requestJson = request.get_json(force=True)
      content = json.loads(requestJson)
  
      print("Content Recieved ",content)

      address_object = {}
      address_object['name'] = content['name']
      address_object['phonno'] = content['phonno']
      address_object['address'] = content['address']
      
      redis_connection  = redis.Redis(host=redis_host,port=int(redis_port),password=redis_password)
      address_object_json = redis_connection.get(address_key)
      read_address_object = json.loads(address_object_json)
      read_address_object['name'] = address_object['name']
      read_address_object['phoneno'] = address_object['phonno']
      read_address_object['address'] = address_object['address']

      address_object_json = json.dumps(read_address_object)
      redis_connection.set(address_key,address_object_json)
      redis_connection.close()
      return Response("{\"updated\":\""+address_key+"\"}", status=200, mimetype='application/json')

    except Exception as e:
      print(e)
      return Response("{\"error\":\"Unable To Update\""+str(e)+"\"}", status=400, mimetype='application/json')

@app.route('/api/v1/resources/address/<address_key>',methods=['GET'])
def api_id(address_key):
    try:
      print('Asking for a single Address...')
      redis_connection  = redis.Redis(host=redis_host,port=int(redis_port),password=redis_password)
      address_object = redis_connection.get(address_key)
      redis_connection.close()
      address_object_json = json.loads(address_object)
      print(address_object_json)
      return Response(str(address_object_json), status=200, mimetype='application/json')
    except Exception as e:
      print(e)
      return Response("{\"error\":\"Unable To GET\""+address_key+"\"}", status=400, mimetype='application/json')

@app.route('/api/v1/resources/address/<address_key>',methods=['DELETE'])
def api_delete(address_key):
    try:
      redis_connection  = redis.Redis(host=redis_host,port=int(redis_port),password=redis_password)
      redis_connection.delete(address_key)
      redis_connection.close()
      return Response("{\"status\":\"OK\"}", status=200, mimetype='application/json')
    except Exception as e:
      print(e)
      return Response("{\"error\":\"Unable To Delete "+address_key+"\"}", status=400, mimetype='application/json')

@app.route('/api/v1/resources/address/create',methods=['POST'])
def save():
    try:
      print("Request Received")
      requestJson = request.get_json(force=True)
      content = json.loads(requestJson)
      print("Content Recieved ",content)
      
      address_object = {}
      address_object['name'] = content['name']
      address_object['phonno'] = content['phonno']
      address_object['address'] = content['address']
      address_object['serialno'] = PREF+ str(uuid.uuid1())
    
      address_object_json = json.dumps(address_object)
      print("Saved Data ",address_object_json)
      #fetching the jsons object
      redis_connection  = redis.Redis(host=redis_host,port=int(redis_port),password=redis_password)
      redis_connection.set(address_object['serialno'],address_object_json)

      redis_connection.close()

      print("Successfully commited one record into ADDRESS table...")
      responseCorrect = {}
      responseCorrect['id_created'] = address_object['serialno']
      jsonResponse = json.dumps(responseCorrect)
      return Response(jsonResponse, status=200, mimetype='application/json')
    except Exception as e:
      print(e)
      print("REDIS Connection have been closed ")
      return Response("{\"error\":\"Unable To Create "+str(e)+"\"}", status=400, mimetype='application/json')


app.run(host=hostname,port=int(port))

