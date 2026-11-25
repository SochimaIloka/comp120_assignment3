# Encapsulation: Protects score and lives using private attributes and controlled methods
class ScoreManager:
    def __init__(self, initial_lives=3):
        self.__score = 0
        self.__lives = initial_lives

    def add_points(self, points=10):
        if points > 0:
            self.__score += points

    def lose_life(self):
        if self.__lives > 0:
            self.__lives -= 1

    def get_score(self):
        return self.__score

    def get_lives(self):
        return self.__lives

    def is_game_over(self):
        return self.__lives <= 0
