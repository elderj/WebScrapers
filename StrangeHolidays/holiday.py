from bs4 import BeautifulSoup

import requests
import re

class Holiday:
  def __init__(self, month, date):

      #Used for testing
      #contents = open('/home/jelder/Software/Python/2018/Holidays/july.html', 'r').read()
      #contents = open('/home/jelder/Software/Python/2018/Holidays/august.html', 'r').read()

      url="http://www.holidayinsights.com/moreholidays/"+month.lower()+".htm"
      contents = requests.get(url).content
      soup = BeautifulSoup(contents, 'html.parser')

      print("Looking up holidays for "+month,date)

      

      soup = BeautifulSoup(contents, 'html.parser')
      
      #This is that td that contains the info
      alltds = soup.find_all("td")
      contentd="";
      for td in alltds:
        if 'Bizarre and Unique Holidays' in str(td):
          contentd=td

      if len(contentd) == 0:
        exit()

      holiday_dictionary = {}

      for stuff in contentd.find_all("a"):

        dayNumber = str(stuff.previousSibling).strip()
        #Grab only the valid dates from the list
        try:
          float(dayNumber)
          if str(dayNumber) in holiday_dictionary:
            holidayname = str(stuff.text).rstrip('\n')
            holidayname=" ".join(holidayname.split())
            holiday_dictionary[dayNumber] = holiday_dictionary[dayNumber] +'\n--> '+ holidayname
          else:
            holidayname=str(stuff.text).rstrip('\n--> ')
            holidayname=" ".join(holidayname.split())
            holiday_dictionary[dayNumber] = holidayname

        except ValueError:
          pass

      if str(date) in holiday_dictionary:
        print("--> "+holiday_dictionary[str(date)])
      else:
        print("No holidays today :(")
