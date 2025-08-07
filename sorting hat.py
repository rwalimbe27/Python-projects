print("These are the four houses:")
print("Gryffindor")
print("Ravenclaw")
print("Hufflepuff")
print("Slytherin")
Gryffindor=0
Ravenclaw=0
Slytherin=0
Hufflepuff=0

print("Q1) Do you like Dawn or Dusk? \n 1)Dawn \n2)Dusk")
q1=int(input("Answer the option number :"))
if q1 == 1:
  Gryffindor=Gryffindor+1
  Ravenclaw=Ravenclaw+1
elif q1 == 2:
  Hufflepuff=Hufflepuff+1
  Slytherin=Slytherin+1
else:
  print("Wrong input")

print(" Q2) When I’m dead, I want people to remember me as: \n1) The Good \n2) The Great \n3) The Wise \n4)The Bold")
q2=int(input("Answer the optionnumber :"))
if q2 == 1:
  Hufflepuff+=2
elif q2 == 2:
  Slytherin+=2
elif q2 == 3:
  Ravenclaw+=2
elif q2 == 4:
  Gryffindor+=2
else:
  print(" Wrong input")

print("Q3) Which kind of instrument most pleases your ear? \n1) The violin \n 2) The trumpet \n3) The piano \n 4) The drum")
q3=int(input("Answer the option number: "))
if q3==1:
  Slytherin+=4
elif q3==2:
  Hufflepuff+=4
elif q3==3:
  Ravenclaw+=4
elif q3==4:
  Gryffindor+=4
else:
  print("Wrong input")

print("Gryffindor", Gryffindor)
print("Ravenclaw", Ravenclaw)
print("Hufflepuff", Hufflepuff)
print("Slytherin", Slytherin)