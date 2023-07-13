import pandas as pd
import timeit as t

def getPandas(df,sex):
    if (sex != " "):
        numsurv = df[df.Sex == sex].Survived.value_counts()
        print(numsurv)
    else:
        #newdf = df.dropna() # drop all records with an empty col
        newdf = df[df['Age'].notna()]
        print(len(newdf))
        numsurv = newdf[newdf.Age < 16].Survived.value_counts()
        print(numsurv)
    return (numsurv[1] / (numsurv[0] + numsurv[1])) * 100
    
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
def vanilla():
    file = open("titanic.csv","r") # r is read only
    cols = file.readline() # gets first line of data
    data = file.readlines() # all 891 rows into a variable called "data"
    file.close()

    print("This is vanilla")
    w = getGrp(data,"female")
    m = getGrp(data,"male")
    k = getKidz(data)
    print(w,k,m)
    
def usepandas():
    df = pd.read_csv("titanic.csv")
    print("This is pandas")
    w = getPandas(df,"female")
    m = getPandas(df,"male")
    k = getPandas(df," ")
    print(w,k,m)

print(t.timeit(vanilla,number=1))
print(t.timeit(usepandas,number=1))
    
'''
fo = open("index.html","w")
fo.write("<html>"
fo.write("<hl>Women and Children first?</hl>")
fo.write("<p>Here are the results of my Titanic analysis.</p>")
fo.write("<img src='titanic.jpg' width='700px'>")
fo.write("<br>")
fo.write("<h2>Study Conclusion</h2>")
fo.write("<svg width='800' height='500'>")
fo.write("<rect width='740' height='100' fill='#d9854a'></rect>")
fo.write("<text x='25' y='25' fill='white'>Women</text>")
fo.write("<rect y='100' width='590' height='100' fill='green'></rect>")
fo.write("<rect y='200' width='190' height='100' fill='blue'></rect>")
fo.write("</html>")
fo.close()
'''

