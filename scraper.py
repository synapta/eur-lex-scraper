import requests
import re
from time import sleep
import os

save_dir = 'docs/'
domain = 'http://eur-lex.europa.eu/'
page_base_url = 'http://eur-lex.europa.eu/search.html?instInvStatus=ALL&qid=1407932788225&DTS_DOM=EU_LAW&type=advanced&lang=en&SUBDOM_INIT=EU_CASE_LAW&DTS_SUBDOM=EU_CASE_LAW&page='
hook_text = './legal-content/EN/TXT/HTML/?'
html_link_re = re.compile(r'./legal-content/EN/TXT/HTML/[^"]*')

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

for i in range(1,10000):
  response = requests.get(page_base_url + str(i))
  for path in  re.findall(html_link_re, response.text):
    sleep(1)
    continua = 1

    url = domain + path[2:]
    print "Downloading " + url

    while continua:
      try:
        page = requests.get(url)
        continua = 0
      except:
        continua = 1

    celex = re.search("uri=([A-Z0-9:\(\)]+)", path).group(1)

    with open(save_dir + celex, 'w') as page_file: 
      page_file.write(page.text.encode('utf-8'))
