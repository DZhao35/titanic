
def exData(blist,num):
    for r in range (1,num):
        line = blist[r]
        temp = line.split(",") # "1,0,3,Braund,male" split up by comma
        print(temp[3] + " survived? " + temp[1] + " m/f? "  + temp[5])

# file input

fi = open("titanic.csv","r") #read-only, write
biglist = fi.readlines()
fi.close()

print(len(biglist))# len tells you #s in list
print(biglist[0]) # print column names
exData(biglist,10) # send # list up to function
