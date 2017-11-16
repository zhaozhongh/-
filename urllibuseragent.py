import urllib  
import urllib2  
 
url = 'https://www.youtube.com/'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'  
values = {'username' : 'cht980923@gmail.com',  'password' : 'XXXX' }  
headers = { 'User-Agent' : user_agent }  
data = urllib.urlencode(values)  
request = urllib2.Request(url, data, headers)  
response = urllib2.urlopen(request)  
page = response.read()
