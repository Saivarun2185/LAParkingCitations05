#Aawaj Raj Joshi

#Creating the Reducer

#Open file, read-only 
n = open("o.txt","r") 

#Open file for writing
s = open("s.txt", "w") 

#Reading the lines from n
lines = n.readlines()

#Sorting the lines
lines.sort()

#Writing the files 
for line in lines:
	s.write(line)

#Closing the files
n.close()
s.close()
