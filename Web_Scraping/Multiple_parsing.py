import justext
import requests
page1 = requests.get('https://www.bbc.co.uk/news/health-26681306').text.encode('utf-8') #insert a link  for the extracting here
page2 = requests.get('https://www.bbc.co.uk/news/education-26617395').text.encode('utf-8') #insert a link  for the extracting here
page3 = requests.get('https://www.bbc.co.uk/news/magazine-26472906').text.encode('utf-8') #insert a link  for the extracting here
page4 = requests.get('https://www.bbc.co.uk/news/magazine-26610276').text.encode('utf-8') #insert a link  for the extracting here
page5 = requests.get('https://www.bbc.co.uk/news/magazine-26431858').text.encode('utf-8') #insert a link  for the extracting here
page6 = requests.get('https://www.bbc.co.uk/news/science-environment-26172181?').text.encode('utf-8')     #insert a link  for the extracting here
page7 = requests.get('https://www.bbc.co.uk/news/science-environment-26325934').text.encode('utf-8') #insert a link  for the extracting here
page8 = requests.get('https://www.bbc.co.uk/news/science-environment-26340038').text.encode('utf-8')  #insert a link  for the extracting here
page9 = requests.get('https://www.bbc.co.uk/sport/disability-sport/26591726').text.encode('utf-8') #insert a link  for the extracting here
page10 = requests.get(' https://www.bbc.co.uk/sport/disability-sport/26549695').text.encode('utf-8')#insert a link  for the extracting here

paragraphs = justext.justext(page1, justext.get_stoplist('English'))
for paragraph in paragraphs:
    if not paragraph.is_boilerplate:
#        print(paragraph['text'])        
        with open("BBC_1.txt", "a") as myfile: #change the name of an output .txt file
            myfile.write(paragraph.text)
    
paragraphs = justext.justext(page2, justext.get_stoplist('English'))
for paragraph in paragraphs:
    #if paragraph['class'] == 'good': #old
    if not paragraph.is_boilerplate:
#        print(paragraph['text'])        
        with open("BBC_2.txt", "a") as myfile: #change the name of an output .txt file
            myfile.write(paragraph.text)

paragraphs = justext.justext(page3, justext.get_stoplist('English'))
for paragraph in paragraphs:
    if not paragraph.is_boilerplate:
#        print(paragraph['text'])        
        with open("BBC_3.txt", "a") as myfile: #change the name of an output .txt file
            myfile.write(paragraph.text)


paragraphs = justext.justext(page4, justext.get_stoplist('English')) 
for paragraph in paragraphs:
    if not paragraph.is_boilerplate:
#        print(paragraph['text'])        
        with open("BBC_4.txt", "a") as myfile: #change the name of an output .txt file
            myfile.write(paragraph.text)

paragraphs = justext.justext(page5, justext.get_stoplist('English'))
for paragraph in paragraphs:
    if not paragraph.is_boilerplate:
#        print(paragraph['text'])        
        with open("BBC_5.txt", "a") as myfile: #change the name of an output .txt file
            myfile.write(paragraph.text)

paragraphs = justext.justext(page6, justext.get_stoplist('English'))
for paragraph in paragraphs:
    if not paragraph.is_boilerplate:
#        print(paragraph['text'])        
        with open("BBC_6.txt", "a") as myfile: #change the name of an output .txt file
            myfile.write(paragraph.text)

paragraphs = justext.justext(page7, justext.get_stoplist('English'))
for paragraph in paragraphs:
    if not paragraph.is_boilerplate:
#        print(paragraph['text'])        
        with open("BBC_7.txt", "a") as myfile: #change the name of an output .txt file
            myfile.write(paragraph.text)

paragraphs = justext.justext(page8, justext.get_stoplist('English'))
for paragraph in paragraphs:
    if not paragraph.is_boilerplate:
#        print(paragraph['text'])        
        with open("BDan_8.txt", "a") as myfile: #change the name of an output .txt file
            myfile.write(paragraph.text)

paragraphs = justext.justext(page9, justext.get_stoplist('English'))
for paragraph in paragraphs:
    if not paragraph.is_boilerplate:
#        print(paragraph['text'])        
        with open("BBC_9.txt", "a") as myfile: #change the name of an output .txt file
            myfile.write(paragraph.text)

paragraphs = justext.justext(page10, justext.get_stoplist('English'))
for paragraph in paragraphs:
    if not paragraph.is_boilerplate:
#        print(paragraph['text'])        
        with open("BBC_10.txt", "a") as myfile: #change the name of an output .txt file
            myfile.write(paragraph.text)