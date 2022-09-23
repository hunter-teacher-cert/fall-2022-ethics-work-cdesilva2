#Game of Nim
#Christopher De Silva
# CSCI 77800 Fall 2022
# collaborators: 

import random #to create a random number for computer

stones = 12
playerturn = True

print("There is a bag containing 12 stones. You can choose 1-3 stones each turn. No more no Less. Can you win?")
while(True):
  userinput = int(input("How many stones do you choose [1-3]: "))
  if userinput > 0 and userinput <= 3 and stones <=12:
    stones -= userinput 
    print("Stones remaining: ", stones)
    playerturn = True
    print()

    if stones <=0 and playerturn == True:
      print("Congratulations Player Won!")
      break

    print("Computer Turn")
    cominput = random.randint(1,3)
    print("Computer Chose: ", cominput)
    stones -= cominput
    print("Stones remaining: ",stones)
    playerturn = False
    print()
    
  elif stones <=0 and playerturn == False: 
    print("Sorry, Computer Wins!")
    break
    
print("Thank you for Playing")
    #loop until game ends
    
      #prompt for user input : num of stones
          