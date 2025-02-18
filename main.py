import pandas as pd

from player import Player
from knapsack import calculate_knapsack
from pathlib import Path

BUDGET = 100 # consider value in millions of US$

if __name__ == '__main__':
    print('----------| Moneyball Knapsack |----------')
    print(f'Budget: US${BUDGET}.000.000')

    # Points to the files inside the input folder
    input_path = Path('input')
    _, _, files = list(input_path.walk())[0]

    for index, file in enumerate(files):
        players_list = list()
        file_path    = input_path / file
        df           = pd.read_csv(file_path, delimiter=';')

        for _, row in df.iterrows():
            players_list.append(Player(
                name              = row['name'],
                market_value      = row['market_value'],
                position          = row['position'],
                injury_tolerance  = row['injury_tolerance'],
                extrafield_factor = row['extrafield_factor'],
                overall           = row['overall']
            ))
        
        selected_players = calculate_knapsack(BUDGET, players_list)

        print()
        print(f'---| Selected Players from List {index+1} (Total spent: US${sum([player.market_value for player in selected_players])}.000.000) |---')
        for player in selected_players: print(player.__str__())

        