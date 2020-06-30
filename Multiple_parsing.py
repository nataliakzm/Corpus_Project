import justext
import requests
page1 = requests.get('https://www.bbc.co.uk/news/world-europe-26606097').text.encode('utf-8') #insert a link  for the extracting here
page2 = requests.get('https://www.bbc.co.uk/news/world-europe-26644082').text.encode('utf-8') #insert a link  for the extracting here
page3 = requests.get('https://www.bbc.co.uk/news/world-europe-26436291').text.encode('utf-8') #insert a link  for the extracting here
page4 = requests.get('https://www.bbc.co.uk/news/world-europe-26686949').text.encode('utf-8') #insert a link  for the extracting here
page5 = requests.get('https://www.bbc.co.uk/news/world-europe-26686949').text.encode('utf-8') #insert a link  for the extracting here
page6 = requests.get('https://www.bbc.co.uk/news/magazine-26610276').text.encode('utf-8')     #insert a link  for the extracting here
page7 = requests.get('https://www.bbc.co.uk/news/world-europe-26411396').text.encode('utf-8') #insert a link  for the extracting here
page8 = requests.get('https://www.bbc.co.uk/news/uk-politics-26415789').text.encode('utf-8')  #insert a link  for the extracting here
page9 = requests.get('https://www.bbc.co.uk/news/world-europe-26433309').text.encode('utf-8') #insert a link  for the extracting here
page10 = requests.get('https://www.bbc.co.uk/news/world-europe-26400035').text.encode('utf-8')#insert a link  for the extracting here

paragraphs = justext.justext(page1, justext.get_stoplist('English'))
for paragraph in paragraphs:
    if paragraph['class'] == 'good':
#        print(paragraph['text'])        
        with open("BBC_1.txt", "a") as myfile: #change the name of an output .txt file
            myfile.write(paragraph['text'])
    
paragraphs = justext.justext(page2, justext.get_stoplist('English'))
for paragraph in paragraphs:
    if paragraph['class'] == 'good':
#        print(paragraph['text'])        
        with open("BBC_2.txt", "a") as myfile: #change the name of an output .txt file
            myfile.write(paragraph['text'])

paragraphs = justext.justext(page3, justext.get_stoplist('English'))
for paragraph in paragraphs:
    if paragraph['class'] == 'good':
#        print(paragraph['text'])        
        with open("BBC_3.txt", "a") as myfile: #change the name of an output .txt file
            myfile.write(paragraph['text'])


paragraphs = justext.justext(page4, justext.get_stoplist('English')) 
for paragraph in paragraphs:
    if paragraph['class'] == 'good':
#        print(paragraph['text'])        
        with open("BBC_4.txt", "a") as myfile: #change the name of an output .txt file
            myfile.write(paragraph['text'])

paragraphs = justext.justext(page5, justext.get_stoplist('English'))
for paragraph in paragraphs:
    if paragraph['class'] == 'good':
#        print(paragraph['text'])        
        with open("BBC_5.txt", "a") as myfile: #change the name of an output .txt file
            myfile.write(paragraph['text'])

paragraphs = justext.justext(page6, justext.get_stoplist('English'))
for paragraph in paragraphs:
    if paragraph['class'] == 'good':
#        print(paragraph['text'])        
        with open("BBC_6.txt", "a") as myfile: #change the name of an output .txt file
            myfile.write(paragraph['text'])

paragraphs = justext.justext(page7, justext.get_stoplist('English'))
for paragraph in paragraphs:
    if paragraph['class'] == 'good':
#        print(paragraph['text'])        
        with open("BBC_7.txt", "a") as myfile: #change the name of an output .txt file
            myfile.write(paragraph['text'])

paragraphs = justext.justext(page8, justext.get_stoplist('English'))
for paragraph in paragraphs:
    if paragraph['class'] == 'good':
#        print(paragraph['text'])        
        with open("BBC_8.txt", "a") as myfile: #change the name of an output .txt file
            myfile.write(paragraph['text'])

paragraphs = justext.justext(page9, justext.get_stoplist('English'))
for paragraph in paragraphs:
    if paragraph['class'] == 'good':
#        print(paragraph['text'])        
        with open("BBC_9.txt", "a") as myfile: #change the name of an output .txt file
            myfile.write(paragraph['text'])

paragraphs = justext.justext(page10, justext.get_stoplist('English'))
for paragraph in paragraphs:
    if paragraph['class'] == 'good':
#        print(paragraph['text'])        
        with open("BBC_10.txt", "a") as myfile: #change the name of an output .txt file
            myfile.write(paragraph['text'])