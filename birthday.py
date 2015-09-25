print "Enter your birthday: "
bdyear=int(input("Year: "))
bdmonth=int(input("Month (Enter as num): "))
bdday=int(input("Date: "))

from datetime import datetime
now = datetime.today ()

age = datetime(int(bdyear), int(bdmonth), int(bdday))
print ("Your age is " + str(now-age))
