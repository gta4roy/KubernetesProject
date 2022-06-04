import requests
import json

server_ip = "127.0.0.1"
port = "7474"

def getAllAddress():
    get_all_url = "http://"+server_ip+":"+port+"/api/v1/resources/address"
    res = requests.get(get_all_url)
    if res.ok:
        print(res.json())
        jsonResponse = json.loads(res.json())
        return jsonResponse
    else:
        print("Request is failed")
        print(res.json())

def getAddress(addressKey):
    get_all_url = "http://"+server_ip+":"+port+"/api/v1/resources/address/"+addressKey
    res = requests.get(get_all_url)
    if res.ok:
        print(res.json())
        jsonResponse = json.loads(res.json())
        return jsonResponse
    else:
        print("Request is failed")
        print(res.json())

def deleteAddress(addressKey):
    get_all_url = "http://"+server_ip+":"+port+"/api/v1/resources/address/"+addressKey
    res = requests.delete(get_all_url)
    if res.ok:
        print(res.json())
    else:
        print("Request is failed")
        print(res.json())


def updateAddress(addressKey):

    address_object = {}
    address_object['name'] = 'Updated Name'
    address_object['phonno'] = '7829712286'
    address_object['address'] = '41/39 saket palli narhi '
    address_object_json = json.dumps(address_object)
    get_all_url = "http://"+server_ip+":"+port+"/api/v1/resources/address/"+addressKey
    res = requests.put(get_all_url,json=address_object_json)
    if res.ok:
        print(res.json())
    else:
        print("Request is failed")
        print(res.json())

def createAddress():
    address_object = {}
    address_object['name'] = 'Abhijit'
    address_object['phonno'] = '7829712286'
    address_object['address'] = '41/39 saket palli narhi '
    address_object_json = json.dumps(address_object)
    save_url = "http://"+server_ip+":"+port+"/api/v1/resources/address/create"
    res = requests.post(save_url, json=address_object_json)
    if res.ok:
        print(res.json())
        jsonResponse = res.json()
        AddressID = jsonResponse["id_created"]
        return AddressID
    else:
        print("Request is failed")
        print(res.json())



addressKey = createAddress()
#getAllAddress()

print('Asking for Address:')
#getAddress(addressKey)

updateAddress(addressKey)



