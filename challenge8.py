game_state = True
game_options = ["rock", "paper", "scissors"]

print("<---- Play ---->")
print("Options : Rock, Scissors, Paper")

def f_print(player):
    print("Player {} win".format(player))

while game_state :
    player1 = str(input("Player 1: "))
    player2 = str(input("Player 2: "))
    
    if player1.lower() == player2.lower():
        print("Seleccionar nuevamente")
        continue
    elif player1.lower() == "rock" and player2.lower() == "scissors" or player1.lower() == "paper" and player2.lower() == "rock" or player1.lower() == "scissors" and player2.lower() == "paper" :
        f_print(1)
        game_state = False

    else:
        f_print(2)
        game_state = False

    response = str(input("Again?: "))
    if response in ("yes", "y", "ye"):
        game_state = True
    else:
        None
