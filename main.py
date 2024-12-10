import requests
from send_email import sending_email
import os


API_KEY = str(os.getenv('API_KEY'))
url = f'https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey={API_KEY}'


#? Make request
request = requests.get(url)

#? Get a dictionary with data
content = request.json()
text = ''
#? Access the article titles and description
for article in content['articles']:
    text = text + str(article["title"]) + '\n' + str(article["description"]) + 2*'\n'

sending_email(message=text)
