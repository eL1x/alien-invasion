class GameStats():
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        """Initalize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start Alien Invasion in an inactive state.
        self.game_active = False

        self.load_high_score(ai_settings)
        
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def load_high_score(self, ai_settings):
        with open(ai_settings.high_score_file, "r") as high_score_file:
            self.high_score = high_score_file.read()
            if not self.high_score:
                self.high_score = 0
            else:
                self.high_score = int(self.high_score)
