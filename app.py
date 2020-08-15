import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '__cfduid=df72adfa45d19046504db8000a812e0a51597475274; PHPSESSID=on2hlj8phm26bo73k5dpkg7ba1; slim_session=%7B%22authKey%22%3A%2237e58ea510d9c6232f5be9dbe3391caa%22%2C%22slim.flash%22%3A%5B%5D%7D; _ga=GA1.2.967890707.1597475275; _gid=GA1.2.1581737377.1597475275',
    'Host': 'catfooddb.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
}
response = requests.get('http://catfooddb.com/data/catfood/-by-products?brands=', headers=headers)

jsonObj = response.json()
result = []
for item in jsonObj['items']:
    result.append({
        'img': item['imageUrl'],
        'name': item['displayName'],
        'protein': item['dryPercentages']['protein'],
        'fat': item['dryPercentages']['fat'],
        'carb': item['dryPercentages']['carbohydrates'],
        'ing': item['ingredients']
    })
    # if(item['fat']):
    #     print(item['fat'])
for value in result:
    print(value)
