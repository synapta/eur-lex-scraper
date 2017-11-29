import csv
import json
import requests
import time
import urllib


csv_file = 'test.csv'

# Replace this with you dandelion api token. 
# Register here: https://dandelion.eu/accounts/register/?next=/semantic-text/entity-extraction-demo/
TOKEN = "4688681ade124a338ca8e9de3b07a548" 

# opens the csv file
with open(csv_file, 'r') as f:

  # Create a csv reader that gives you a dictionary for each line created with the header row
  # csv.DictReader gives you a iterable
  csv_reader = csv.DictReader(f)
  
  # Iterating over the lines of the file
  for line in csv_reader:
    
    # Setting a sleep timeout between each request
    time.sleep(1)
    
    print "We are processing this line:"
    print line

    print "This is the string we are going to enrich"
    print line['Title']

    # Creating the get request to dandelion
    response = requests.get("https://api.dandelion.eu/datatxt/nex/v1/?text=" + urllib.quote(line['Title'])  + "&include=types%2Cabstract%2Ccategories&token=" + TOKEN )

    # Loading response as a python dict
    returned_object = json.loads(response.text)
    
    # Printing only organizations
    for entity in returned_object['annotations']:
      if 'http://dbpedia.org/ontology/Organisation' in entity['types']:
        print "Found: " + entity['label']

    print
