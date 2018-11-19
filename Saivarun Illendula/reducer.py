# Reducer to convert the output from the mapper using the aggregate function.
s = open("sortout.txt","r")  # open file, read-only
r = open("redout.txt", "w") # open file, write
thisKey = ""
thisValue = 0.0
for line in s:
 data = line.strip().split('\t')      # Code for seperating the output of the reducer by a tab space. 
 year, fine = data

 if year != thisKey:
   if thisKey:
     # output the last key value pair result
     r.write(thisKey + '\t' + str(thisValue)+'\n')
     print(thisKey + '\t' + str(thisValue)+'\n')

   # start over when changing keys
   thisKey = year
   thisValue = 0.0
 # apply the aggregation function
 thisValue += float(fine)
 
r.write(thisKey + '\t' + str(thisValue)+'\n')          # Code for writing the output into the redout.txt
print(thisKey + '\t' + str(thisValue)+'\n')
s.close()
r.close()
