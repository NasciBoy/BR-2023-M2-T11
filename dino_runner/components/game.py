import pygame
import pygame.mixer

from dino_runner.utils.constants import BG, BG2, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, MUSIC_THEME, CLOUD
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.utils.text_utils import draw_message_component
from dino_runner.components.power_ups.power_up_manager import PowerUpManager


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.score = 0
        self.death_count = 0
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 410
        self.x_pos_cloud = 1280 # 
        self.y_pos_cloud = 80 # 
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        

    def execute(self):
        self.running = True
        pygame.mixer.music.load(MUSIC_THEME) # Carregar a música
        pygame.mixer.music.play(-1)  # -1 para reproduz em loop
        while self.running:
            if not self.playing:
                self.show_menu()
                pygame.mixer.music.stop() # Parar a música

        pygame.display.quit()
        pygame.quit()
    
    def run(self):
        self.playing = True
        pygame.mixer.music.stop()      # Parar a música
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.game_speed = 20
        self.score = 0
        pygame.mixer.music.play(-1)    # reiniciar a música
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()
        self.power_up_manager.update(self.score, self.game_speed, self.player)
        
    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 5

    def draw(self):
        self.clock.tick(FPS)
        #self.screen.fill((230, 255, 230))
        self.screen.blit((BG2), (0, 0))
        self.draw_background()
        self.draw_score()
        self.draw_power_up_time()
        self.draw_cloud()          # Médoto da nuvem
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    # método que desenha a nuvem na tela
    def draw_cloud(self):              
        cloud_img = CLOUD.get_width()
        self.screen.blit(CLOUD, (cloud_img + self.x_pos_cloud, self.y_pos_cloud))
        self.x_pos_cloud -= self.game_speed // 4  
        self.screen.blit(CLOUD, (cloud_img + self.x_pos_cloud, self.y_pos_cloud))
        if self.x_pos_cloud < -cloud_img:
            self.x_pos_cloud = SCREEN_WIDTH

    def draw_score(self):
        draw_message_component(
            f"pontos: {self.score}",
            self.screen,
            pos_x_center = 1000,
            pos_y_center = 50
        )

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                draw_message_component(
                    f"{self.player.type.capitalize()} enable for {time_to_show} seconds",
                    self.screen,
                    font_size = 18,
                    pos_x_center = 500,
                    pos_y_center = 40
                )
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

            elif event.type == pygame.KEYDOWN:
                self.run()

    def show_menu(self):
        self.screen.fill((220, 230, 255))
        #self.screen.blit(pygame.image.load('C:/Users/Vinícius/OneDrive/Área de Trabalho/João/MODULO II/Repositório clone/Repositorio do DINO/Dino-Joao/dino_runner/assets/Imagem/imagem.png'), (0, 0))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width =  SCREEN_WIDTH // 2
        
        if self.death_count == 0:
            draw_message_component("Pressione qualquer tecla para iniciar o jogo!!!", self.screen)
        else:
            draw_message_component("Pressione qualquer tecla para reiniciar o jogo!!!", self.screen, pos_y_center = half_screen_height + 140)
            draw_message_component(
                f"Sua pontuação: {self.score}",
                self.screen,
                pos_y_center=half_screen_height - 150
            )
            draw_message_component(
                f"Contagem de vida: {self.death_count}",
                self.screen,
                pos_y_center=half_screen_height - 100
            )
            self.screen.blit(ICON, (half_screen_width - 40, half_screen_height - 30))

        pygame.display.flip()
        self.handle_events_on_menu()



    



