
import pandas as pd

def pdKidz(data):
    numkids = df[df.Age < 16].Age.count()
    kidsurv = df[df.Age < 16].Survived.value_counts()
    return (kidsurv[1] / (kidsurv[0] + kidsurv[1])) * 100
    print(numkids, kidsurv)

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
#file = open("titanic.csv","r") # r is read only
#cols = file.readline() # gets first line of data
#data = file.readlines() # all 891 rows into a variable called "data"
#file.close()

# pandas data frame is a 2 dim list
df = pd.read_csv("titanic.csv")
print(pdKidz(df))


'''
fo = open("index.html","w")
fo.write("<html>"
fo.write("<hl>Women and Children first?</hl>")
fo.write("<p>Here are the results of my Titanic analysis.</p>")
fo.write("<img src='titanic.jpg' width='700px'>")
fo.write("<br>")
fo.write("<h2>Study Conclusion</h2>")
fo.write("<svg width='800' height='500'>")
fo.write("<rect width='" + str(w * 10) + "' height='100' fill='#d9854a'></rect>")
fo.write("<text x='25' y='25' fill='white'>Women</text>")
fo.write("<rect y='100' width='590' height='100' fill='green'></rect>")
fo.write("<rect y='200' width='190' height='100' fill='blue'></rect>")
fo.write("</html>")
fo.close()
'''

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
