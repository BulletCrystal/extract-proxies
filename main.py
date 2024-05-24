import requests
from get_proxies import proxies_list
def get_proxies():
    proxies = []
    url = 'https://ipecho.net/plain'
    l = len(proxies_list)
    i = 0
    p =[]
    # Iterate the proxies and check if it is working. 
    for proxy in proxies_list:
        print(l-i,f"/{l}, Remaining... with {i} done")
        i+=1
        try: 

            page = requests.get( 
            url, proxies={"http": proxy, "https": proxy}) 

            # Prints Proxy server IP address if proxy is alive 
            print("Status OK, Output:", page.text)
            with open('test.txt', 'r') as tr:
                p = tr.readlines()
                p.append(proxy)
                p.append('\n')
                with open('test.txt','w') as tw:
                    tw.writelines(p)
            proxies.append(page.text)
        except OSError as e: 
            # Proxy returns Connection error 
            print("Status BAD : ",proxy)
    with open('proxies.txt','w') as wd:
        wd.writelines(proxies)


get_proxies()
