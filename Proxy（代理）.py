import urllib.request
enable_proxy = True
proxy_handler = urllib.request.ProxyHandler({"http" : '61.135.217.7:80'})
null_proxy_handler = urllib.request.ProxyHandler({})
if enable_proxy:
    opener = urllib.request.build_opener(proxy_handler)
    print("chenggong")
else:
    opener = urllib.request.build_opener(null_proxy_handler)
urllib.request.install_opener(opener)
response = urllib.request.urlopen('http://www.baidu.com',timeout=10)
