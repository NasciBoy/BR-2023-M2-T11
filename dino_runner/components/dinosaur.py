import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, DEFAULT_TYPE, SHIELD_TYPE, DUCKING_SHIELD, JUMPING_SHIELD, RUNNING_SHIELD, JUMP_SOUND, HAMMER_TYPE, DUCKING_HAMMER, JUMPING_HAMMER, RUNNING_HAMMER, SCREEN_WIDTH, ICE_TYPE, RUNNING_ICE, JUMPING_ICE, DUCKING_ICE

DUCK_IMG = { DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER, ICE_TYPE: DUCKING_ICE}
JUMP_IMG = { DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE:JUMPING_HAMMER, ICE_TYPE: JUMPING_ICE}
RUN_IMG = { DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER, ICE_TYPE: RUNNING_ICE}
X_POS = 80
Y_POS = 450
Y_POS_DUCK = 500
JUMP_VEL = 8.5

pygame.mixer.init()    

class Dinosaur(Sprite):
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False
        self.dino_jump_vel = JUMP_VEL
        self.setup_state()
        self.jump_sound_playing = False  ##
        self.move_x = X_POS ## tentar mover a direita

    def setup_state(self):
        self.has_power_up = False
        self.shield = False
        self.hammer = False #
        self.ice = False #
        self.show_text = False
        self.shield_time_up = 0

    def update(self, user_input):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()

        if user_input[pygame.K_UP]:          
            if not self.jump_sound_playing:   ##
                JUMP_SOUND.play()              ##
                self.jump_sound_playing = True  ##
            if user_input[pygame.K_UP] and not self.dino_jump:
                self.dino_run = False
                self.dino_jump = True
                self.dino_duck = False

        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = False
            self.dino_duck = True

        elif not self.dino_jump and not self.dino_duck:
            self.dino_run = True
            self.dino_jump = False
            self.dino_duck = False

        else:                                 # importante estar nessa posição antes do index
            self.jump_sound_playing = False 

        if user_input[pygame.K_LEFT]:       # left
            self.move_x -= 15
            if self.move_x <= 0: 
                self.move_x = 0
        elif user_input[pygame.K_RIGHT]:     #right
            self.move_x += 15
            if self.move_x >= SCREEN_WIDTH - 100: 
                self.move_x = SCREEN_WIDTH - 100
        else:
            self.x_vel = 0     
        
        if self.step_index >= 9:
            self.step_index = 0
        
    
    def run(self):
        self.image = RUN_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.move_x #### Permite se movimentar
        self.dino_rect.y = Y_POS
        self.step_index += 1

    def jump(self):
        self.image = JUMP_IMG[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.dino_jump_vel * 6 # aumento do pulo
            self.dino_jump_vel -= 0.8
            self.dino_rect.x = self.move_x  # Move no ar
        if self.dino_jump_vel < -JUMP_VEL:
            self.dino_rect_y = Y_POS
            self.dino_rect.x = self.move_x  # mover caindo
            self.dino_jump= False
            self.dino_jump_vel = JUMP_VEL

    def duck(self):
        self.image = DUCK_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.move_x - 60  # Permite ficar abaixado se movendo
        self.dino_rect.y = Y_POS_DUCK
        self.step_index += 1
        self.dino_duck = False

    def reset_pos_x(self):
        if self.dino_run == False and self.dino_jump == False and self.dino_duck == True:
            self.move_x = X_POS
    

    def draw(self,screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
