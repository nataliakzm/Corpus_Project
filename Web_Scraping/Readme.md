Here, me (Natalia Kuzminykh) with a motivational help of Sabahat Javed Khan try to make the most efficient way to build a corpus from the web.
*This repository is going to be updated with the tools that we used to analyse corpora.

The idea of the project is to crawl the web media sources to build a corpus by using Python packages (e.g. Justext or BeautifulSoup). Here are scripts that can be useful for this:

1) Building_Script.py - this script will extract only text from a webpage.
   However, you will need to update the link and the output filename for each link mannualy.
   Prerequisites: pip install lxml justext requests

2) Multiple_Parsing.py - This is an extended version of the previous script, it can work with 10 different links and provides the output .txt for each. However, you still will need to update the link and the output filename for each link mannualy.
   Prerequisites: pip install lxml justext requests

3) Reading_txt.py - works more efficiently. It analyses a text input file that should be located in your working directory and contains all your urls an then gives one txt file that contains text info from all webpages. It also uses another parser (Beautifulsoup), so the provided output requires proofreading.
*One can encounter that the parser doesn't recognize a text on a webpage. In this case it will skip a link and goes to a next one (going to be solved in future).
   Prerequisites: pip install lxml bs4 requests sys webbrowser codecs

For getting links more efficiently, you can use following scripts:
1)Links_crawler.py - extracts external (and internal) links from a provided webpage.
  However, there will be lots of "noise" in the output
   Prerequisites: pip install requests, urllib.parse colorama bs4
   For running the script: python Links_crawler.py https://www.bbc.co.uk/news/world-europe-26606097

2)Scraper_google.py - extracts output url from a google search. But the output info will be mixed with text info.
   Prerequisites: pip install requests, urllib bs4
 
   







