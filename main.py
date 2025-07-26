import app_requests.api_requests as api_requests
import streamlit as st

print("weather app")
ip = "2a0d:6fc2:4570:8800:7d25:29c8:77d2:7cbe"
visitor_data =  api_requests.get_data_visitor_ip(ip)
#print(visitor_data)

# change color
latitude = visitor_data["latitude"]
longitude = visitor_data["longitude"]
country_capital = visitor_data["country_capital"]
country_name = visitor_data["country_name"]
city = visitor_data["city"]


