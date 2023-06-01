import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus 
from dino_runner.components.obstacles.bird import Bird 


class ObstacleManager: 
        def __init__(self): 
                self.obstacles = [] 

        def update(self, game):
                obstacle_type = [      # Lista de tipo do obstáculo Bird ou Cactus
                        Cactus(), 
                        Bird(), 
                ] 
                
                if len(self.obstacles) == 0:      #verifica a quantidade de itens na lista e se não tive nenhum ele add
                        self.obstacles.append(obstacle_type[random.randint(0,1)]) #não add apenas Cactus, agora add o tipo em random

                for obstacle in self.obstacles:                            # Procura em obstacle dados de obstacles 
                        obstacle.update(game.game_speed, self.obstacles) 
                        if game.player.dino_rect.colliderect(obstacle.rect): 
                                pygame.time.delay(500)
                                game.playing = False
                                break
                       
        def draw(self, screen): 
                for obstacle in self.obstacles: 
                        obstacle.draw(screen)
        
        def reset_obstacles(self):
                self.obstacles = []