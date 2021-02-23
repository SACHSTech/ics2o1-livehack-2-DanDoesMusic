###this takes the 2 speeds the limit and the users speed###

speed = int(input("how fast was the diver: "))
limit = int(input("what is the speed limit: "))
###this chacks if they are above the speed limit it took me a bit but i got it working###

if (speed - limit) >= 1 :
  print("your fine is 100$")

elif (speed - limit) >= 21 :
  print("your fine is 270$")

elif (speed - limit) >= 31 :
  print("your fine is 570$")

else :
  print ("you are within the limit")

###it checks to see if you are above 1 u/h or unit per hour then it checks if you are 21 u/h above then 31 or more and determines your fine based on what you cross if you are below or at the limit you are safe###