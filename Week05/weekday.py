#This program outputs whether or not today is a weekday.
#author:Regina Fennessy

#This works out all days as a numerica value 'Monday=0, Tuesday=1 ...'
from datetime import datetime
wk = datetime.today().weekday()

#If your Week day is >4 'Friday' then its the weekend otherwise its a weekday
if wk > 4: 
 print("It is the weekend, yay!")

else:
 print("Yes, unfortunately today is a weekday.")



