import pygame
import os

pygame.mixer.init()  # Iniciador do mixer de som

# Constantes globais
TITLE = "Luigi Runner"
SCREEN_HEIGHT = 600     
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")  # Constante de busca no diretório

# Imagens gerais
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))
JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))
JUMPING_ICE = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpIce.png"))
CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png')) 
ICE = pygame.image.load(os.path.join(IMG_DIR, 'Other/flower.png'))
BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))
BG2 = pygame.image.load(os.path.join(IMG_DIR, 'Imagem/back.jpg'))
BG3 = pygame.image.load(os.path.join(IMG_DIR, 'Imagem/start.jpg'))

# Imagems das ações no jogo e obstáculos
RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Shield.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Hammer.png")),
]

RUNNING_ICE = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Ice.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Ice.png")),
]

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Shield.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Hammer.png")),
]

DUCKING_ICE = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Ice.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Ice.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

# Sons do jogo
SHIELD_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/Shield.mp3'))      
JUMP_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/Jump.wav'))          
END_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/Game_Over.wav'))       
HIT_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/Hit.wav'))           
HAMMER_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/hammer.mp3'))
ICE_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/hammer.mp3'))

MUSIC_THEME = "C:/Users/Vinícius/OneDrive/Área de Trabalho/João/MODULO II (TURBO)/Dino-Teste/dino_runner/assets/Sounds/music_theme.mp3"

pygame.mixer.music.load
# Constantes de tipo
DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = "hammer"
ICE_TYPE = "ice"