
# function to find kids % survived
# 1. loop through all data
# 2. if person < 16 count them
# 3. did they survive? count them
# 4. return kidsurvive / totalkids * 100 >> % survived
# pid,surv,class,name,age

def kidz(data):
    numkidz = 0
    kidzlive = 0
    for r in data:
        temp = r.split(",")
        if (temp[6] != ""):
            if (float(temp[6]) < 16.0):
                numkidz = numkidz + 1
                if (temp[1] == "1"):
                        kidzlive = kidzlive + 1
    return round((kidzlive / numkidz) * 100,1)


file = open("titanic.csv","r")
cols = file.readline() # grab first line, reposition pointer
data = file.readlines()# grab all remaining data >> list
file.close()

print(cols)
print(data[0])
print(str(kidz(data)) + "% survived")

