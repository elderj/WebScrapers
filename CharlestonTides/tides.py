#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

response = requests.get('http://charlestongateway.com/tide-charts/')
html = response.content
response=True

if response:
  print('Success!')
  soup = BeautifulSoup(html, "lxml")
  rows = soup.find_all("tr")

  for row in rows:
    if (set(['level0','Day']).issubset( row['class'] )):
      print("MONTH:", row.th.contents[0])
    elif (set(['level1','Day']).issubset( row['class'] )):
      print("  DAY:", row.th.contents[0])
    else:
      event = ""
      for i in row.contents:
        event = event +" "+i.contents[0].contents[0]
      print("    -",event) 
else:
  print('No reponse ')
