import json

def get_all_users():
    with open("./data/users.json", encoding='utf-8') as jsonFile:
        data = json.load(jsonFile)
    return data

def get_user(pid):
    with open("./data/users.json", encoding='utf-8') as jsonFile:
        data = json.load(jsonFile)
    return data[pid - 1]

def get_orders():
    with open("./data/orders.json", encoding='utf-8') as jsonFile:
        data = json.load(jsonFile)
    return data

def get_order(pid):
    with open("./data/orders.json", encoding='utf-8') as jsonFile:
        data = json.load(jsonFile)
    return data[pid - 1]

def get_offers():
    with open("./data/offers.json", encoding='utf-8') as jsonFile:
        data = json.load(jsonFile)
    return data

def get_offer(pid):
    with open("./data/offer.json", encoding='utf-8') as jsonFile:
        data = json.load(jsonFile)
    return data[pid - 1]

def create_user(data, pid):
    
    pass
def delete_user():
    pass
    #todo