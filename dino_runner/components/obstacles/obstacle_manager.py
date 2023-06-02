import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus 
from dino_runner.components.obstacles.bird import Bird 
from dino_runner.utils.constants import END_SOUND    ##


class ObstacleManager: 
        def init(self): 
                self.obstacles = []

        def update(self, game):
                obstacle_type = [ 
                        Cactus(), 
                        Bird(), 
                ] 
                
                if len(self.obstacles) == 0:
                        self.obstacles.append(obstacle_type[random.randint(0,1)]) 
                        
                for obstacle in self.obstacles: 
                        obstacle.update(game.game_speed, self.obstacles) 
                        if game.player.dino_rect.colliderect(obstacle.rect): 
                                if not game.player.has_power_up:
                                        pygame.time.delay(500) 
                                        game.playing = False 
                                        END_SOUND.play()          ##
                                        game.death_count += 1 
                                        break 
                                else:
                                        if game.player.hammer == True:
                                                self.obstacles.remove(obstacle)
                                                game.game_speed += 1
                                                game.score += 100
                                        elif game.player.ice == True:
                                                game.game_speed = 30
                                                game.score -= 50
                                                continue
                                        elif game.player.shield == True:
                                                continue
                                                
                                                

                               
        def reset_obstacles(self): 
                self.obstacles = [] 
        def draw(self, screen): 
                for obstacle in self.obstacles: 
                        obstacle.draw(screen)