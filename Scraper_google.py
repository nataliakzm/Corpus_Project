import urllib
import requests
from bs4 import BeautifulSoup

# desktop user-agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
# mobile user-agent
MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"

query = "Russia"
query = query.replace(' ', '+')
#insert a link  for the extracting here
URL = f"https://www.google.com/search?q=Russia+site:https://www.bbc.co.uk&lr=lang_en&cr=countryUK%7CcountryGB&newwindow=1&hl=en&as_qdr=all&tbs=lr:lang_1en,ctr:countryUK%7CcountryGB,cdr:1,cd_min:2/20/2014,cd_max:3/26/2014&sxsrf=ALeKk01KKL8apgzhZ6bUteNIBnN7UGMprg:1593430824469&filter=0&biw=1366&bih=652" 

headers = {"user-agent": USER_AGENT}
resp = requests.get(URL, headers=headers)

if resp.status_code == 200:
    soup = BeautifulSoup(resp.content, "html.parser")
    results = []
    for g in soup.find_all('div', class_='r'):
        anchors = g.find_all('a')
        if anchors:
            link = anchors[0]['href']
            title = g.find('h3').text
            item = {
                "title": title,
                "link": link
            }
            results.append(item)
    print(*results)