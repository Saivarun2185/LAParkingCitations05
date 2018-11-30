#Aawaj Raj Joshi

#Creating the Reducer

#Open file, read-only 
s = open("s.txt","r") 

#Open file for writing
r = open("r.txt", "w")   

thisKey = ""
thisValue = 0.0
count = 0.0

for line in s:
 data = line.strip().split('\t')
 color, year, fine = data

 if year != thisKey:
   if thisKey:
     
     r.write(thisKey + '\t' + str(thisValue/count)+'\n')
     print(thisKey + '\t' + str(thisValue)+'\n')

   #Changing the keys
   thisKey = year
   thisValue = 0.0
   count = 0.0

 thisValue += float(fine)

 count += 1

#Writing the average in file
r.write(thisKey + '\t' + str(thisValue/count) + '\n')

#Printing the average on console
print("The average fine for a white colored vehicle in LA is: $" + str(thisValue/count)+'\n')

s.close()
r.close()