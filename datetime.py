from datetime import datetime

# current date and time# Converting datetime object to string
dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("(%d_%b_%Y_%H_%M)")
print('Current Timestamp : ', timestampStr)