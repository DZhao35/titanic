print("yo wagwan world")

age = 17 # "17" integer: no decimal.
pi = 3.14 # float: floating point number with decimal.
name = "Daniel" # string
iscool = True # boolean
height = 183

print (age + pi) #if you combine integer + float, the result is a float.
print (age - pi)
print (age/pi)
print (age*pi)

niceoutput = round(age * pi,1)
print(niceoutput)

print(name + " " + str(age)) #change int to a string


# sequential, selection, repetition


myheight = input("How tall are you?: ")
if(int(myheight) > 183):
    print("You are very tall!")
elif(int(myheight) <=183 and int(myheight) >=175):
    print("You are above average")
else:
    print("Shortie")




