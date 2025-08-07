import random
player = input("Please enter your name:")
print("1)Rock✊\n2)Paper✋\n3)Scissors✌\n4)Lizard🦎\n5)Spock🖖") 
p_score=0
c_score=0
for i in range (5):
    computer = random.randint(1,5)
    op = int(input("Select what you want"))
    if op==1 and computer==1:
      print("You chose : ✊ \n Computer chose : ✊  \n It's a tie!"  )
      p_score+=0
      c_score+=0
    elif op==2 and computer==2:
      print("You chose : ✋ \n Computer chose :  ✋   \nIt's a tie!" )
      p_score+=0
      c_score+=0
    elif op==3 and computer==3:
      print("You chose : ✌️ \n Computer chose : ✌️ \n It's a tie!")
      p_score+=0
      c_score+=0
    elif op==4 and computer==4:
      print("You chose : 🦎 \nComputer chose : 🦎 \n It's a tie!")
      p_score+=0
      c_score+=0
    elif op==5 and computer==5:
      print("You chose :  🖖 \nComputer chose :  🖖\n It's a tie!")
      p_score+=0
      c_score+=0
    elif op==1 and computer==2:
      print("You chose : ✊\n Computer chose : ✋ \nComputer wins!")
      c_score+=1
    elif op==1 and computer==3:
      print("You chose : ✊\n Computer chose : ✌️")
      print(player, " wins!")
      p_score+=1
    elif op==1 and computer==4:
      print("You chose : ✊\n Computer chose :  🦎")
      print(player, " wins!")
      p_score+=1
    elif op==1 and computer==5:
      print("You chose : ✊ \nComputer chose :  🖖 \n Computer wins")
      c_score+=1
    elif op==2 and computer==1:
      print("You chose : ✋ \n Computer chose :  ✊\nComputer wins!")
      c_score+=1
    elif op==2 and computer==3:
      print("You chose : ✋ \n Computer chose :  ✌️")
      print(player, " wins!" )
      p_score+=1
    elif op==2 and computer==4:
      print("You chose : ✋ \nComputer chose:  🦎 \nComputer wins! ")
      c_score+=1
    elif op==2 and computer==5:
      print("You chose : ✋ \nComputer chose :  🖖")
      print(player, " wins!")
      p_score+=1
    elif op==3 and computer==1:
      print("You chose : ✌️ \n Computer chose : ✊️ \nComputer wins")
      c_score+=1
    elif op==3 and computer==2:
      print("You chose : ✌️ \n Computer chose : ✋️ \nComputer wins")
      c_score+=1
    elif op==3 and computer==4:
      print("You chose: ✌️ \nComputer chose :  🦎")
      print(player, " wins!")
      p_score+=1
    elif op==3 and computer==5:
      print("You chose: ✌️ \nComputer chose:  🖖\nComputer wins!")
      c_score+=1
    elif op==4 and computer==1:
      print("You chose :  🦎 \nComputer chose: ✊ \nComputer wins!")
      c_score+=1
    elif op==4 and computer==2:
      print("You chose : 🦎 \nComputer chose: ✋")
      print(player, " wins!")
      p_score+=1
    elif op==4 and computer==3:
      print("You chose : 🦎 \nComputer chose: ✌️ \n Computer wins!")
      c_score+=1
    elif op==4 and computer==5:
      print("You chose : 🦎 \nComputer chose:  🖖 \nComputer wins!")
      c_score+=1
    elif op==5 and computer==1:
      print("You chose :  🖖 \nComputer chose : ✊")
      print(player, " wins!")
      p_score+=1
    elif op==5 and computer==2:
      print("You chose :  🖖 \nComputer chose : ✋\nComputer wins!")
      c_score+=1
    elif op==5 and computer==3:
      print("You chose :  🖖 \nComputer chose : ✌️")
      print(player, " wins!")
      p_score+=1
    elif op==5 and computer==4:
      print("You chose :  🖖 \nComputer chose :  🦎")
      print(player, " wins!")
      p_score+=1
    else:
      print("Wrong inputa")
      
print("Total score for ", player, " is ", p_score)
print("Total score for computer is ", c_score)