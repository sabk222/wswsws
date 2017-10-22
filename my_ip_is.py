import urllib.request,random

iplist = ["114.99.22.145:6890","118.117.137.46:9000","180.118.86.211:9000","121.232.144.13:9000","118.117.139.117:9000"]
proxy = urllib.request.ProxyHandler({"http":random.choice(iplist)})

opener = urllib.request.build_opener(proxy)
urllib.request.install_opener(opener)

url = "http://www.whatismyip.com.tw"
res = urllib.request.urlopen(url)
html = res.read().decode("utf-8")

print(html)
