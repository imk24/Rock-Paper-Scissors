#Game of Rock Paper and Scissors against the Computer
import random

def game():

    counter = 3
    amount = 1

#Defines rules and user input
    while counter > 0:
        user = input("Rules Type: 'rock' for rock, 'paper' for paper, and 'scissors' for scissors ")
        
        while user != 'rock' and user != 'paper' and user != 'scissors':
            user = input("Enter either: 'rock', 'paper', or 'scissors' ")
            
        
        comp = random.choice(['rock', 'paper', 'scissors'])
    
        if user == comp:
            if counter > 2:
                print("You Tied, you have", counter - 1, "more attempts")
            elif counter > 1:
                print("You Tied, you have",counter - 1, "more attempt")
                  
            else:
                print("You Tied")
            
        else:
            def winner(user, comp):
                if (user == 'rock' and comp == 'scissors') or (user == 'scissors' and comp == 'paper') or (user == 'paper' and comp == 'rock'):
                    return True
        
            if winner(user, comp):
                if amount == 1:
                    return print("You Won, it took you",amount , "attempt")
                else:
                    return print("You Won, it took you", amount, "attempts")
    
            if not winner(user, comp):
                if counter > 2:
                    print("You Lost, you have", counter - 1, "more attempts")
                elif counter > 1:
                    print("You Lost, you have",counter - 1, "more attempt")
                  
                else:
                    print("You Lost")
        counter -= 1
        amount += 1
    
    if counter == 0:
        print('End')
game()





