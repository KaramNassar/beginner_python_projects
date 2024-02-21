from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, letter):
        self.letter = letter

    @abstractmethod
    def get_move(self, game):
        pass
