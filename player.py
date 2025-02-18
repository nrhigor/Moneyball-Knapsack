from dataclasses import dataclass

@dataclass
class Player:
    name:              str
    market_value:      float
    position:          str
    injury_tolerance:  float
    extrafield_factor: float
    overall:           float
    in_bag:            bool = False

    def get_players_global_factor(self) -> int:
        """ 
            The global factor of a player is a made-up calculation that tries to compensate the player's overall
            with factors like extrafield, injury tolerance and its market value.
        """
        return int(round(10*(self.overall/(self.extrafield_factor + self.injury_tolerance + self.market_value*0.5)), 0))

    def add_to_bag(self):
        self.in_bag = True

    def __str__(self):
        return f'\t> Name: {self.name} | Market Value: US${self.market_value}.000.000 | Position: {self.position}'