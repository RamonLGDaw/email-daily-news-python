import requests

API_KEY = '57a06ffc360b459ba2139a3fedc98704'
url = f'https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey={API_KEY}'
#https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey=57a06ffc360b459ba2139a3fedc98704

#? Make request
request = requests.get(url)

#? Get a dictionary with data
content = request.json()

#? Access the article titles and description
for article in content['articles']:
    print(f"Title ==> {article['title']}")
    print(f"Description ==> {article['description']}")