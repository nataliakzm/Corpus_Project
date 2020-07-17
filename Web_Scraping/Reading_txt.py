import requests, sys, webbrowser, bs4
import codecs

def get_content(link):
  page = requests.get(link)
  soup = bs4.BeautifulSoup(page.content, 'html.parser')
  all_p = soup.find_all('p')
  content = ''
  for p in all_p:
    content += p.get_text().strip('\n')
  return content

in_path = "input.txt"  #the text should be located in the same directory with a script
out_path = "outputData.txt" 

with open(in_path, 'r') as fin:
  links = fin.read().splitlines()
with open(out_path, 'w') as fout:
  for i, link in enumerate(links):
     fout.write(get_content(link) + '\n')