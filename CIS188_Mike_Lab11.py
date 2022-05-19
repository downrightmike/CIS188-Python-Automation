
import csv
import ezgmail, os
from ping3 import ping
ezgmail.init()
 
exampleFile = open('.\ip.csv')
ipData = list(csv.DictReader(exampleFile))
response = []
bodyMesg = ""
for row in ipData:
   print(row['ip'] + " " + str(ping(row['ip'])))
   response.append(row['ip'] + " " + str(ping(row['ip'])))
 
#print(response)
for row in response:
   #print(row)
   bodyMesg += row + "\n"
#print(bodyMesg)
ezgmail.send('mail@mail', 'List of IPs', bodyMesg)
