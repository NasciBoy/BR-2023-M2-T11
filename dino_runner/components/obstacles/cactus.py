import random

from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS
from dino_runner.components.obstacles.obstacle import Obstacle


class Cactus(Obstacle):  #Cactus Herda de Obstacle

    CACTUS = [
        (LARGE_CACTUS, 460),
        (SMALL_CACTUS, 450),
    ]

    def __init__(self):
        image, cactus_pos = self.CACTUS[random.randint(0, 1)]
        self.type = random.randint(0, 2)
        super().__init__(image, self.type) #Chama da superclasse
        self.rect.y = cactus_pos