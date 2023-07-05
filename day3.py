
def exData(blist,num):
    for r in range (1,num):
        line = blist[r]
        temp = line.split(",") # "1,0,3,Braund,male" split up by comma
        print("   m/f:"  + temp[5] + " Class: " + temp[2] + " Name:" + temp[3] + temp[4] + " survived:" + temp[1] + " Ticket: " + temp [9] + " Price: " + temp[10])

# file input

fi = open("titanic.csv","r") #read-only, write
biglist = fi.readlines()
fi.close()

print(len(biglist))# len tells you #s in list
print(biglist[0]) # print column names
exData(biglist,10) # send # list up to function
