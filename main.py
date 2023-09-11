import random

while True:
 print("\n\n Enter Your Choice :-")
 print("1.Rock")
 print("2.Paper")
 print("3.Scissor")
 n=int(input("\n\n Enter the number:-"))
 if n==1:
     user_name='Rock'
 elif n==2:
     user_name='Paper'
 else:
     user_name='Scissor'
 print("Your Choice:-",user_name)
 print("\n\nNow,It's computer choice...")
 comp_choice=random.randint(1,3)
 if comp_choice==1:
     comp_name='Rock'
 elif comp_choice==2:
     comp_name='Paper'
 else:
     comp_name='Scissor'
 print("Computer Choice:-",comp_name)
 print(user_name,"VS",comp_name)
 if(n==1 and comp_choice==2):
     print("\nPaper wins")
     print("\nComputer is the Winner")
 elif(n==1 and comp_choice==3):
     print("\nRock wins")
     print("\nYour the Winner")
 elif(n==2 and comp_choice==3):
     print("\nScissor wins")
     print("\nComputer is the Winner")
 elif(n==2 and comp_choice==1):
     print("\nPaper wins")
     print("\nYour the Winner")
 elif(n==3 and comp_choice==1):
     print("\nRock wins")
     print("\nComputer the Winner")
 elif(n==3 and comp_choice==2):
     print("\nScissor wins")
     print("\nYour the Winner")
 else:
     print("\nOhh No Same Choice")
 print("\nYou want to play again(Y/N)")
 ans=input()
 if ans=='N':
     break
print("Thank you for Playing:)!!!")