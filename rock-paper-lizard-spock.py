# """"Scissors decapitate Scissors cuts paper, paper covers rock,
#  rock crushes lizard, lizard poisons Spock, Spock smashes scissors, 
#  scissors decapitates lizard, lizard eats paper, paper disproves Spock,
#  Spock vaporizes rock, and as it always has, rock crushes scissors.""""


from random import randint


choices = ['rock', 'paper', 'scissors','lizard','spock']

def rock_paper_scissors_lizard_spock():

    while True:
        
        computer = choices[randint(0, 4)]
        player = input("Let's play rock, paper, scissors, lizard or spock! Or, type 'quit' to exit the game.\nWhat's your move?\n").lower()
    
        if player == 'quit':
            print("Thanks for playing!")
            break

        elif player == computer:
            print(f"Game Tied! Computer also chose {computer} Try again!")

        elif player == 'rock':
            if computer == 'paper':
                print(f"You lose! {computer} Covers Rock!")
            elif computer == 'lizard':
                print(f"You Win! Rock crushes {computer}!")
            elif computer == 'spock':
                print(f"You Lose! {computer} Vaporizes Rock!")
            elif computer == 'rock':
                print(f"You win! Rock smashes {computer}!")
            
        elif player == 'paper':
            if computer == 'scissors':
                print(f"You lose! {computer} cuts paper!")
            elif computer == 'rock':
                print(f'You win! {computer} covers rock!')
            elif computer == "lizard":
                print(f"You lose! {computer} eats paper!")
            elif computer == 'spock':
                print(f"You win! {computer} disproves Spock!")

        elif player == 'scissors':
            if computer == 'rock':
                print(f"You lose! {computer} crushes scissors!")
            elif computer == 'paper':
                print(f"You win! Paper cuts {computer}!")
            elif computer =='lizard':
                print(f"You win! scissors decapitates {computer}!")
            elif computer == 'spock':
                print(f"You lose! {computer} smashes scissors!")

        elif player == 'lizard':
            if computer == 'rock':
                print(f"You lose! {computer} crushes lizard!")
            elif computer == 'paper':
                print(f"You win!  lizard eats {computer}!")
            elif computer == "scissors":
                print(f"You lose! {computer} decapitates lizard!")
            elif computer == "spock":
                print(f"You win! lizard poisons {computer}!")
        elif player == 'spock':
            if computer == 'rock':
                print(f"You win! Spock vaporizes {computer}!")
            elif computer == 'paper':
                print(f"You lose! {computer} disproves Spock!")
            elif computer == 'scissors':
                print(f"You win! Spock smashes {computer}")
            elif computer == 'lizard':
                print(f"You lose! {computer} poisons Spock!")
        else:
            print("That doesn't seem to be an option. Try Again! So Rock, Paper, Scissors, Lizard or Spock? :")


rock_paper_scissors_lizard_spock()
