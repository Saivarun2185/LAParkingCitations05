# Implementing a mapper to read the input file and all of its contents. Also for sorting the output and for obtaining the Key-value pairs.
from datetime import datetime
f = open("../parking-citations.csv","r")  # open file, read-only raw data
o = open("./mapout.txt", "w") # open file, write - just our key, value pairs
# count = 0  # Code for printing the output on the console.
for line in f:
    data = line.strip().split(",")
    if len(data) == 19:
        # print data
        Ticket_number,Issue_Date,Issue_time,Meter_Id,Marked_Time,RP_State_Plate,Plate_Expiry_Date,VIN,Make,Body_Style,Color,Location,Route,Agency,Violation_code,Violation_Description,Fine_amount,Latitude,Longitude, = data
        if Violation_Description == "NO STOP/STAND AM":             # Code for checking if the data belongs to fine type "NO STOP/STAND AM"
            # 2015-12-22T00:00:00
            dt = datetime.strptime(Issue_Date, '%Y-%m-%dT%H:%M:%S')  # Code for dividing the given date into standard format of '%Y-%m-%dT%H:%M:%S'
            o.write("{0}\t{1}\n".format(dt.year, Fine_amount))       # Code for writing the output into mapout.txt
            # count = count + 1                                      # Code for printing the output on the console.
            # if count < 10:                                         # Code for printing the output on the console.
            #     print("{0}\t{1}\n".format(dt.year, Fine_amount))   # Code for printing the output on the console.
print "done"
f.close()
o.close()