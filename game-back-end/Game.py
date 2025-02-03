from random import shuffle,randint

players = {'player_one': 'Emma', 'player_two': 'Camilo', 'player_three': 'Jose', 'player_four': 'Luis'}

card_values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
card_suits = ['H', 'D', 'C', 'S']

initial_cards = [f'{value}{suit}' for suit in card_suits for value in card_values]

def shuffle_cards(cards):
        shuffle(cards)

def assign_cards(players):
        cards = shuffle_cards(initial_cards)

        for player in players:
            print(player)
                
assign_cards(players)

        