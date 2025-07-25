import requests

def get_data_visitor_ip():
    response = requests.get("https://ipapi.co/json/")
    data = response.json()
    return data
    #print(data)