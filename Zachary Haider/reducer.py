s = open("s.txt","r")   
r = open("r.txt", "w")   

thisKey = ""
thisValue = 0.0
for line in s:
 data = line.strip().split('\t')
 color, amount = data

 if color != thisKey:
   if thisKey:
     # output the last key value pair result
     r.write(thisKey + '\t' + str(thisValue)+'\n')
     print(thisKey + '\t' + str(thisValue)+'\n')
   #changing keys
   thisKey = color
   thisValue = 0.0
 # aggregation
 thisValue += float(amount)

# output the final entry when done (outside for loop)
r.write(thisKey + '\t' + str(thisValue)+'\n')
print(thisKey + '\t' + str(thisValue)+'\n')

s.close()
r.close()

