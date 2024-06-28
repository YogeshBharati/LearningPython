import datetime
import datetime_nepali

year = int(input("Enter English year:"))
month = int(input("Enter English month:"))
day = int(input("Enter English day:"))
 
#date = datetime_nepali.date(year,month,day).to_datetime_date()
date = datetime_nepali.date.from_datetime_date(datetime.date(year, month, day))
print(f"Nepali date is :{date}")