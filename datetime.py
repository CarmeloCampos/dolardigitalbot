from datetime import datetime

# current date and time# Converting datetime object to string
dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("(%d/%b/%Y %H:%M:%S)")
print('Current Timestamp : ', timestampStr)