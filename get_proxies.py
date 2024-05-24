import requests

url = "https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies"

proxies_txt = requests.get(url).text
proxies_list = proxies_txt.split()