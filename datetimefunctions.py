__author__ = 'akatla'

import time
import datetime

print 'time now in epoch' , time.time()

print "Current date and time is ", datetime.datetime.now()

print str(datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S'))

print "Month of year: ", datetime.date.today().strftime("%B")

print "Week number of the year: ", datetime.date.today().strftime("%W")

print "Day of year: ", datetime.date.today().strftime("%y%j")

print "Day of the month : ", datetime.date.today().strftime("%d")

print "Day of week: ", datetime.date.today().strftime("%A")

print "logfile date " , datetime.date.today().strftime('%d-%m-%Y')

mydate = datetime.date(1985,12,26)
print mydate.strftime("%A")