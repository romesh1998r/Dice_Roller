import random

def main():
    Player1=0
    Player2=0
    Player1wins=0
    Player2wins=0
    rounds=1

    while rounds !=10:

   
        print("ROUND" +str(rounds))
        Player1=dice_roll()
        Player2=dice_roll()
        print("Player1 Roll:"+ str(Player1))
        print("Player2 Roll:"+ str(Player2))

    

        if Player1 == Player2:

            print("Draw")
            
        elif Player1 > Player2:

            Player1wins=Player1wins+1
            print("Player1 win!")


        else:

            Player2wins=Player2wins+1
            print("Player2 win!")

            
        rounds= rounds + 1


        if Player1wins == Player2wins:

            print("Draw")

        elif Player1wins > Player2wins:

            print("Player1 win! - Round won:" + str(Player1wins))


        else:

            print("Player2 win! - Round won:" + str(Player2wins))    
        






def dice_roll():

    D=random.randint(1,6)
    return D

main()
