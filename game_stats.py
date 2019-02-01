class GameStats():
    '''Track statistics for Alien Invasion'''

    def __init__(self, ai_settings):
        '''Initiliaze statistics'''
        self.ai_settings = ai_settings
        self.reset_stats()

        # start Alien Invasion in an innactive state
        self.game_active = False

    def reset_stats(self):
        '''Initiliaze statistics that can change during the game'''
        self.ships_left = self.ai_settings.ship_limit