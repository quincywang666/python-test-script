import urllib.request
response = urllib.request.urlopen('https://blog.csdn.net/weixin_43499626')
print(response.read().decode('utf-8'))

