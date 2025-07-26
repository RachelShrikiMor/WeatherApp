import requests

def get_data_visitor_ip(ip):
    """
    this function fey a data of web visitor by ip address
    return value from function can be None or
    {'ip': '2a0d:6fc2:4570:8800:7d25:29c8:77d2:7cbe', 'network': '2a0d:6fc2:4540::/42', 'version': 'IPv6', 'city': 'Rishon LeTsiyyon', 'region': 'Central District', 'region_code': 'M', 'country': 'IL', 'country_name': 'Israel', 'country_code': 'IL', 'country_code_iso3': 'ISR', 'country_capital': 'Jerusalem', 'country_tld': '.il', 'continent_code': 'AS', 'in_eu': False, 'postal': None, 'latitude': 31.9642, 'longitude': 34.7876, 'timezone': 'Asia/Jerusalem', 'utc_offset': '+0300', 'country_calling_code': '+972', 'currency': 'ILS', 'currency_name': 'Shekel', 'languages': 'he,ar-IL,en-IL,', 'country_area': 20770.0, 'country_population': 8883800, 'asn': 'AS12400', 'org': 'Partner Communications Ltd.'}
    """
    #response = requests.get("https://ipapi.co/json/")
    response = requests.get(f"https://ipapi.co/{ip}/json/")

    if response.status_code == 200:
        data = response.json()
        if data:
            # print(data)
            return data
        else:
            return None
    else:
        return None
