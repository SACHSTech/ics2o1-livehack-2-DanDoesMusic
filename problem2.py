###so it takes the 3 side mesures and it adds all the combinations together if any 1 of them adds up to 2 of the others it is a triangle###

print("welcome to the triangle checker")
adj = float(input("what is the lenght of the adjacent side: "))
opp = float(input("what is the lenght of the opposite side: "))
hyp = float(input("what is the lenght of the hypotenouse: "))
###this takes the 3 mesurments down###

if (adj + opp) >= hyp : 
  print("this is a triangle")
elif (hyp + opp) >= adj : 
  print("this is a triangle")
elif (adj + hyp) >= opp : 
  print("this is a triangle")
else :
  print("this is not a triangle")
print("have a nice day")
###this is the maths part of my code###



###it just works###