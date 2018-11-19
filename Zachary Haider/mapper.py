f = open("d.csv","r")  # open file, read-only raw data
o = open("o.txt", "w") # open file, write - just our key, value pairs
for line in f:  
    data = line.strip().split(",") 
    #print(data)
    if len(data)==19:
     if data[14] ==("8813B"):        
        color = data[10]
        if color !="":
         o.write("{0}\t1\n".format(color))
f.close()
o.close()
