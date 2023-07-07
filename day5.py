
def getKidz(data):
    # the math numsurv / numkids * 100
    numkids = 0
    numsurv = 0
    for p in data:
        temp = p.split(",")
        if (temp[6] != ""): # error check for missing data
            if (float(temp[6]) < 16.0):
                numkids = numkids + 1
                if (temp[1] == "1"):
                        numsurv = numsurv + 1
    return (numsurv / numkids) * 100

#copy and paste same function but change for male/female

def getGrp(data,sex):
    # the math numsurv / numkids * 100
    numgrp = 0
    numsurv = 0
    for p in data:
        temp = p.split(",")
        if (temp[5] == sex):
                numgrp = numgrp + 1
                if (temp[1] == "1"):
                        numsurv = numsurv + 1
    return (numsurv / numgrp) * 100
        

# open our titanic database
file = open("titanic.csv","r") # r is read only
cols = file.readline() # gets first line of data
data = file.readlines() # all 891 rows into a variable called "data"
file.close()

# create 'game loop' using while

keepgoing = True
while (keepgoing == True):
    key = input("w for female, k for kids, m for men, q for quit")
    if (key =="q"):
        keepgoing = False
        print ("ok ciao!")
    elif (key =="w"):
        k = getGrp(data,"female")
        print ("The % of women that survived is: " + str(round(k,1)))
    elif (key =="m"):
        k = getGrp(data,"male")
        print ("The % of men that survived is: " + str(round(k,1)))
    elif (key =="k"):
        k = getKidz(data)
        print ("The % of kids that survived is: " + str(round(k,1)))
    else:
        print("hit the right key goofy")


k = getKidz(data)
print(round(k,1))
k = getGrp (data, "female")
print(round(k,1))
k = getGrp (data, "male")
print(round(k,1))
