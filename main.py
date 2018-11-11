import maumau


def main():
    while True:
        try:
            amount_of_players = int(input("How many players are playing(2-4): "))
            if 2 <= amount_of_players <= 4:
                break
            else:
                print("the number has to be between 2 and 4")
        except ValueError:
            print("Your input was not a number, please don't do that again!")
    game = maumau.Maumau(amount_of_players)
    game.start_game()

main()
