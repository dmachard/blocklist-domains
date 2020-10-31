from pybadges import badge
from datetime import date

# create badge pour the date
b1 = badge(left_text='Last updated', 
          right_text="%s" % date.today(),
          right_color='blue')
          
with open("badge_date.svg", "w") as f:
    f.write(b1)
    
# create badge pour the number of hosts
with open("blocklist.txt", "r") as f:
    data = f.read()
domains = data.splitlines()

b2 = badge(left_text='Aggregated hosts', 
           right_text="%s" % len(domains),
           right_color='red')
           
with open("badge_total.svg", "w") as f:
    f.write(b2)