import maumau


def main():
    amount_of_players = int(input("Amount of players: "))
    game = maumau.Maumau(amount_of_players)
    print("======")
    print("Amount of Cards left in Deck: ", str(len(game.deck_of_cards)))
    print("======")

    for player in game.players:
        print(player)

main()
