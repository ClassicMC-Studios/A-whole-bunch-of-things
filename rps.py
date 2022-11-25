import random,os
def main():
    player1String = "something unintelligable"
    player2String = "something unintelligable"
    os.system('cls' if os.name == 'nt' else 'clear')
    player1 = input("Choose\n 1) Rock\n 2) Paper\n 3)Scissors\n")
    if player1 == str(1):
        player1String = "Rock"
    if player1 == str(2):
        player1String = "Paper"
    if player1 == str(3):
        player1String = "Scissors"
    os.system('cls' if os.name == 'nt' else 'clear')
    player2 = input("Choose\n 1) Rock\n 2) Paper\n 3)Scissors\n")
    if player2 == str(1):
        player2String = "Rock"
    if player2 == str(2):
        player2String = "Paper"
    if player2 == str(3):
        player2String = "Scissors"
    win = False
    draw = False
    if player1 == str(1) and player2 == str(3) or player1 == str(2) and player2 == str(1) or player1 == str(3) and player2 == str(2):
        print(f"Player 1 won with {player1String}! Player 2 chose {player2String}.")
    elif player2 == str(1) and player1 == str(3) or player2 == str(2) and player1 == str(1) or player2 == str(3) and player1 == str(2):
        print(f"Player 2 won with {player2String}! Player 1 chose {player1String}.")
    else:
        if player1String == player2String:
            print(f"You drawed. You both picked {player1String}")
        else:
            print("Only one of you picked something intelligable.")
    again = input("Play again y/n\n")
    if again == "y":
        main()
main()