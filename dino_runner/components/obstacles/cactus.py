import random

from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS
from dino_runner.components.obstacles.obstacle import Obstacle


class Cactus(Obstacle):            #Cactus Herda de Obstacle

    CACTUS = [                     # Dicionário de large e small cactus e posição Y
        (LARGE_CACTUS, 325),
        (SMALL_CACTUS, 340),
    ]

    def __init__(self):
        image, cactus_pos = self.CACTUS[random.randint(0, 1)]     # Imagem e posição Y
        self.type = random.randint(0, 2)                          # Random de tipo de cacto
        super().__init__(image, self.type)                        # Chama da superclasse
        self.rect.y = cactus_pos
