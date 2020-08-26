#videoclasshelper version W0.0.2P by sudo-nano
#Licensed under CC BY-NC-SA 4.0

import sys
import webbrowser
from datetime import datetime, timedelta, date, time


now = datetime.now()
daynow = date.weekday(datetime.now())
hour = now.hour
minute = now.minute
print("Today is " + str(now))
webbrowser.register('firefox', None, webbrowser.GenericBrowser('firefox'))

#For user configurable WHS versions, have fixed schedules and prompt user for links to save to a file. 
#For user configurable non WHS versions, have the program check the folder it's in for config files. 
#If none exist, prompt user for schedules and class links. 

#Add the links to your video meets for class periods between the quotation marks below. 

p0 = ""
p1 = ""
p2 = ""
p3 = ""
p4 = ""
p5 = ""
p6 = ""
p7 = ""

#Add links as property of period objects later, or don't. 

def chkinterval(period_hour, period_minute):
	period = timedelta(hours = period_hour, minutes = period_minute)
	end_time = period - add10
	begin_time = period + add10
	check_time = timedelta(hours = now.hour, minutes = now.minute)
	if begin_time < end_time:
		if begin_time < check_time:
			if end_time > check_time:
				return(bool(1))
			else:
				return(bool(0))
		else:
			return(bool(0))
	else:
		print("Error: invalid interval")
		return(bool(0))


sub10 = timedelta(
	minutes = 10
	)
add10 = timedelta(
	minutes = -10
	)


if daynow == 0 or daynow == 4 :
	print("Today is Monday/Thursday with periods 0, 1, 3, and 5.")
	p0s = time(hour = 7, minute = 30)
	p1s = time(hour = 9)
	p3s = time(hour = 10, minute = 30)
	p5s = time(hour = 12, minute = 30)

	if chkinterval(p0s.hour, p0s.minute):
		print("Launching period 0")
		webbrowser.open(p0)
	if chkinterval(p1s.hour, p1s.minute):
		print("Launching period 1")
		webbrowser.open(p1)
	if chkinterval(p3s.hour, p3s.minute):
		print("Launching period 3")
		webbrowser.open(p3)
	if chkinterval(p5s.hour, p5s.minute):
		print("Launching period 5")
		webbrowser.open(p5)


if daynow == 2 :
	print("Today is Wednesday, with all periods.")

	p1s = time(hour = 10, minute = 15)
	p2s = time(hour = 10, minute = 55)
	p3s = time(hour = 11, minute = 35)
	p4s = time(hour = 12, minute = 25)
	p5s = time(hour = 13, minute = 45)
	p6s = time(hour = 14, minute = 25)

	if chkinterval(p1s.hour, p1s.minute):
		print("Launching period 1")
		webbrowser.open(p1)
	if chkinterval(p2s.hour, p2s.minute):
		print("Launching period 2")
		webbrowser.open(p2)
	if chkinterval(p3s.hour, p3s.minute):
		print("Launching period 3")
		webbrowser.open(p3)
	if chkinterval(p4s.hour, p4s.minute):
		print("Launching period 4")
		webbrowser.open(p4)
	if chkinterval(p5s.hour, p5s.minute):
		print("Launching period 5")
		webbrowser.open(p5)
	if chkinterval(p6s.hour, p6s.minute):
		print("Launching period 6")
		webbrowser.open(p6)


if daynow == 1 or daynow == 5 :
	print("Today is Tuesday/Friday with periods 7, 2, 4, and 6")
	p7s = time(hour = 7, minute = 30)
	p2s = time(hour = 9)
	p4s = time(hour = 10, minute = 30)
	p6s = time(hour = 12, minute = 30)

	if chkinterval(p7s.hour, p7s.minute):
		print("Launching period 7")
		webbrowser.open(p7)
	if chkinterval(p2s.hour, p2s.minute):
		print("Launching period 2")
		webbrowser.open(p2)
	if chkinterval(p4s.hour, p4s.minute):
		print("Launching period 4")
		webbrowser.open(p4)
	if chkinterval(p6s.hour, p6s.minute):
		print("Launching period 6")
		webbrowser.open(p6)

