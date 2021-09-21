import random
def win(user1,user2):
    if (user1==1 and user2==3)or(user1==2 and user2==1)or (user1==3 and user2==2):
        return True
        
while True:
    print('Winning Rules Of Game::\n'+'Rock Vs Paper-->Paper Wins\n'+'Rock Vs Scissor-->Rock Wins\n'+'Paper Vs Scissor-->Scissor Wins/n')
    user=int(input("Enter Choice\n'1'for rock,'2'for paper,'3'for scissor"))
    computer=random.choice([1,2,3])
    if user>3 or user<1:
        print('wrong input')
    else:
        print("Your choice is ",user)
        print("computer choice is",computer)
        if user==computer:
            print( 'It\'s a tie')
        elif win(user,computer):
            print('You Won')
        else:
            print('you Lose')
        print("Do you want to play again1!(y/n)")
        ans=input()
        if ans=='n' or ans=='N':
            break
print("\n Thanks for playng!!!")

