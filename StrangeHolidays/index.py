#!/usr/bin/env python3

import datetime
from dateutil.parser import parse

from holiday import Holiday

print("")
#Look up if there are any holidays today
today = datetime.date.today()
h = Holiday(today.strftime('%B'), today.day)
print("")
print("")


while True:
  lookup_date = input('Date: ')
  print("")
  if 'q' in str(lookup_date.lower()):
    exit()
  else:
    newday = parse(lookup_date)
    h = Holiday(newday.strftime('%B'), newday.day)
  print("")
  print("")