import justext
import requests
page = requests.get('https://www.bbc.co.uk/news/world-europe-26644082').text.encode('utf-8') #insert a link  for the extracting here

paragraphs = justext.justext(page, justext.get_stoplist('English')) #for corpus in English
for paragraph in paragraphs:
    if not paragraph.is_boilerplate:
#        print(paragraph['text'])        
        with open("BBC.txt", "a") as myfile: #change the name of an output .txt file
            myfile.write(paragraph.text)
