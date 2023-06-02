import random
import pygame

from pygame import mixer
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.ice import Ice


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0 
        self.its_hammer = False
        self.its_shield = False
        self.its_ice = False  
    
    def generate_power_up(self, score):
        if len(self.power_ups) == 0 and self.when_appears == score:
            self.when_appears += random.randint(480, 530)

           
            if random.randint(0, 2) == 0:
                self.power_ups.append(Hammer())
                self.its_hammer = True
                self.its_shield = False
                self.its_ice = False
            elif random.randint(0, 2) == 1:
                self.power_ups.append(Shield())
                self.its_shield = True
                self.its_hammer = False
                self.its_ice = False
            else:
                self.power_ups.append(Ice())  
                self.its_ice = True
                self.its_shield = False
                self.its_hammer = False
    
    def update(self, score, game_speed, player):
        self.generate_power_up(score)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect): 
                efects = mixer.Sound(power_up.sound) 
                efects.play()
                power_up.start_time = pygame.time.get_ticks()
                if self.its_shield:
                    player.shield = True
                    player.hammer = False
                    player.ice = False  
                if self.its_hammer:
                    player.hammer = True
                    player.shield = False
                    player.ice = False  
                if self.its_ice:
                    player.ice = True  
                    player.shield = False
                    player.hammer = False
                player.has_power_up = True
                player.type = power_up.type
                player.power_up_time = power_up.start_time + (power_up.duration * 1000)
                self.power_ups.remove(power_up)
    
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
            
    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(490, 530)
