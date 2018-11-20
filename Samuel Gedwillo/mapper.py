#goes through each line of the .csv
for line in sys.stdin:
	#strips each line of spaces and splits each value by a comma
	line = line.strip()
	line = line.split(",")

	#if the line isn't the header line
	if line[2] != 'Issue_time':
		#set time variable to the third value on each line
		time = line[2]
		if len(time) < 1:
			time = 0
		if len(time) == 4:
			time = int(time[0:2])
			print '%d\t%d' % (time, 1)
		else:
			time = int(time[0:1])
			#prints every time with the pair of 1
			print '%d\t%d' % (time, 1)
		