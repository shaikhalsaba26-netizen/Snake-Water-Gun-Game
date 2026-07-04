'''
water = -1
snake = 1
gun = 0
'''
import random
computer = random.choice([-1, 0, 1])
youstr = input("enter your choice: ")
youdict = {"s":1, "w":-1, "g":0}
computerdict = {1:"snake", -1:"water", 0:"gun"}
you = youdict[youstr]


print(f"computer chose: {computerdict[computer]}  \n you chose: {computerdict[you]}")

if(computer == you):
    print("its a draw! try again..")
else:
 if(computer == -1 and you == 1):
    print("you win!")
 elif(computer == -1 and you == 0):
    print("you lose.")
 elif(computer == 1 and you == -1):
    print("you lose.")
 elif(computer == 1 and you == 0):
    print("you win!")
 elif(computer == 0 and you == -1):
    print("you win!")
 elif(computer == 0 and you == 1):
    print("you lose.")
 else:
    print("oops! something went wrong...")

