import random 

'''
-1 Snake
0 water
1 gun 
'''

computer = random.choice((-1,0,1))
youstr = input("Enter your choice: ")
youDict = {"s":-1,"w":0,"g":1}
reverseDict = {-1:"Snake",1:"Gun",0:"Water"}

you = youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("Its a draw")

else:
    if(computer==-1 and you==1):
        print("You win!")

    elif(computer==-1 and you==0):
        print("You Lose!")

    elif(computer==1 and you==-1):
        print("You Lose!")

    elif(computer==1 and you==0):
        print("You Win!")

    elif(computer==0 and you==-1):
        print("You Win!")

    elif(computer==0 and you==1):
        print("You Lose!")

    else:
        print("Something went wrong!")
