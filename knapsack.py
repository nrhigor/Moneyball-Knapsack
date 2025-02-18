import numpy as np
from player import Player

def calculate_knapsack(budget: int, players_list: list[Player]) -> list[Player]:
    """
        Uses the Knapsack algorithm based on:
            * the market value of all players,
            * the global factor of each player,
            * the club's budget.
    """
    # ---| Variables
    players_qtd        = len(players_list)
    calculation_matrix = np.zeros((players_qtd+1, budget+1), dtype=int)

    # ---| Builds the Knapsack matrix
    for i in range(1, len(players_list) + 1):
        for j in range(1, budget+1):
            if players_list[i - 1].market_value > j:
                calculation_matrix[i, j] = calculation_matrix[i - 1, j]
            else:
                case1 = calculation_matrix[i - 1, j]
                case2 = calculation_matrix[i - 1, j - players_list[i - 1].market_value] + players_list[i - 1].get_players_global_factor()
                calculation_matrix[i, j] = max(case1, case2)

    # ---| Extracts selected players
    i = players_qtd
    j = budget

    while calculation_matrix[i, j] > 0:
        if calculation_matrix[i - 1, j] != calculation_matrix[i, j]:
            players_list[i - 1].add_to_bag()
            j -= players_list[i - 1].market_value
        i -= 1

    return [player for player in players_list if player.in_bag]