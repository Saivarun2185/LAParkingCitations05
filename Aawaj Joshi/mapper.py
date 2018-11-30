#Aawaj Raj Joshi

#Creating the Mapper

from datetime import datetime
#Open file for reading(only)
f = open("parking-citations.csv","r")  

#Open file for writing
o = open("o.txt", "w") 

#Splitting the line by ','
for line in f:  
    data = line.strip().split(",") 

#Getting black colors and their fine amounts
    if len(data)==19:
      Ticket_number,Issue_Date,Issue_time,Meter_Id,Marked_Time,RP_State_Plate,Plate_Expiry_Date,VIN,Make,Body_Style,Color,Location,Route,Agency,Violation_code,Violation_Description,Fine_amount,Latitude,Longitude, = data

      if Color == ("BK"):
        dt = datetime.strptime(Issue_Date, '%Y-%m-%dT%H:%M:%S')        
        color = Color
        fine = Fine_amount
        if fine !="":
          o.write("{0}\t{1}\t{2}\n".format(color, dt.year, fine))

#Closing files
f.close()
o.close()

