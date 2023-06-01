import random

from dino_runner.utils.constants import BIRD
from dino_runner.components.obstacles.obstacle import Obstacle


class Bird(Obstacle):      # A classe Bird herda de Obstacle
    def __init__(self):
        super().__init__(BIRD, 0)
        self.rect.y = random.randint(240, 270) 
        self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image[self.step_index // 5], self.rect)  #O contador index é dividido em valor inteiro p/ controlar a img
        self.step_index += 1

        if self.step_index >= 9:  # Step_index não pode ser 10 senão dá erro
            self.step_index = 0      # Pois 10 // 5 = 2 ERRO somente 0 ou 1
                                        # 9 // 5 = 1 