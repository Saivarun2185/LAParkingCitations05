#import to read from system
import sys

#will be used to store every 
time_count = {}

for line in sys.stdin:
	#creates the time and count variable as it reads through every line
	line = line.strip()
	time, count = line.split('\t')
	
	#if the number is already created, increase its value by one
	if time in time_count:
		time_count[time] += 1
	#else, create a new time and increase it by one
	else:
		time_count[time] = 0
		time_count[time] += 1

#print out each value
for time in time_count.keys():
	print '%d\t%d' % (int(time), int(time_count[time]))