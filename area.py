# condition and check whether the area is greater than 19 or not.
# Define variables
room = input("please enter room bed/kit: ")
area = int(input("enetr your area: "))

# if-elif-else construct for room
if room == "kit" :  
    print("looking around in the kitchen.")
elif room == "bed":
    print ("looking around in the bedroom.")
else :
    print ("looking around elsewhere.")

# if-elif-else construct for area
if area > 15 :
    print("big place!")
else :
    print ("pretty small.")
