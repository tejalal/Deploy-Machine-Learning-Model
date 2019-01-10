import requests
sl=5
sw=3.3
pl=1.4
pw=0.2
newdata={'sepallength':sl, 'sepalwidth':sw, 'petallength':pl, 'petalwidth':pw}
 
url= 'http://127.0.0.1:5000/predict'
response = requests.get(url, params=newdata)# pass the url and query string data
print(response.url) # print the URL path
print (response.json()) # print the predicted class returned from the API
#print (response.text)
