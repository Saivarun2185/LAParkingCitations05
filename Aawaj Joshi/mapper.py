#Aawaj Raj Joshi

#Creating the Mapper

#Open file for reading(only)
f = open("parking-citations.csv","r")  

#Open file for writing
o = open("o.txt", "w") 

#Splitting the line by ','
for line in f:  
    data = line.strip().split(",") 

#Getting black colors and their fine amounts
    if len(data)==19:
     if data[10] ==("BK"):        
        color = data[10]
        fine = data[16]
        if fine !="":
          o.write("{0}\t{1}\n".format(color, fine))

#Closing files
f.close()
o.close()

