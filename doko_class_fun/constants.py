import pygame

WIDTH, HEIGHT = 1100,950

image = pygame.image.load('cards/AC.png')
img_size = image.get_rect().size
RESIZE_CARD = (WIDTH//11, round(img_size[1]/img_size[0]*(WIDTH//11)))

PAD_CARDOVERLAP = (round(HEIGHT*0.04), round(WIDTH*0.03))

PAD_SIDE = round(WIDTH*0.045)
CHOSEN = round(WIDTH*0.014)

PAD_STACK = (RESIZE_CARD[0] + round(WIDTH*0.02), RESIZE_CARD[0] + round(HEIGHT*0.02), RESIZE_CARD[0] + round(WIDTH*0.02), RESIZE_CARD[0] - round(HEIGHT*0.02))

# SCREEN_COLOR
GREEN = (0,50,0)

# BUTTON_COLOR
BUTTON_COLOR = {
    'SOLO': (0,0,230),
    'WED_POV': (0,0,25),
    'HEALTHY': (128,0,128),
    'THROW': (0,0,0),
    'CALL': [(255,0,0),(205,0,0),(155,0,0),(105,0,0),(55,0,0)],
    'POSSIBLE_GAME': (220,220,220)
}

BUTTON_PAD = (round(WIDTH*0.01), round(HEIGHT*0.01))

BUTTON_POSITION = {
    'RE_CONTRA':     (WIDTH//2 - WIDTH*0.264, HEIGHT - PAD_SIDE + BUTTON_PAD[1], WIDTH*0.045, PAD_SIDE - 2*BUTTON_PAD[1]),
    'WEDDING':       (WIDTH//2 - WIDTH*0.182, HEIGHT - PAD_SIDE + BUTTON_PAD[1], WIDTH*0.073, PAD_SIDE - 2*BUTTON_PAD[1]),
    'POVERTY':       (WIDTH//2 - WIDTH*0.1,   HEIGHT - PAD_SIDE + BUTTON_PAD[1], WIDTH*0.073, PAD_SIDE - 2*BUTTON_PAD[1]),
    'HEALTHY':       (WIDTH//2,               HEIGHT - PAD_SIDE + BUTTON_PAD[1], WIDTH*0.073, PAD_SIDE - 2*BUTTON_PAD[1]),
    'QUEEN_SOLO':    (WIDTH//2 + WIDTH*0.11,  HEIGHT - PAD_SIDE + BUTTON_PAD[1], WIDTH*0.073, PAD_SIDE - 2*BUTTON_PAD[1]),
    'JACK_SOLO':     (WIDTH//2 + WIDTH*0.19,  HEIGHT - PAD_SIDE + BUTTON_PAD[1], WIDTH*0.073, PAD_SIDE - 2*BUTTON_PAD[1]),
    'MEATLESS_SOLO': (WIDTH//2 + WIDTH*0.27,  HEIGHT - PAD_SIDE + BUTTON_PAD[1], WIDTH*0.073, PAD_SIDE - 2*BUTTON_PAD[1]),
    'THROW':         (WIDTH//2 + WIDTH*0.35,  HEIGHT - PAD_SIDE + BUTTON_PAD[1], WIDTH*0.073, PAD_SIDE - 2*BUTTON_PAD[1]),
    'TAKE_POVERTY':  (WIDTH//2 + WIDTH*0.05, HEIGHT//2, WIDTH*0.073, HEIGHT*0.047),
    'PASS_POVERTY':  (WIDTH//2 - WIDTH*0.073 - WIDTH*0.05, HEIGHT//2, WIDTH*0.073, HEIGHT*0.047),
    'BACK_POVERTY':  (WIDTH//2 - (WIDTH*0.073)//2, HEIGHT//2, WIDTH*0.073, HEIGHT*0.047)
}

CUR_GAME_POSITION =      [(WIDTH//2 - WIDTH*0.264,                               HEIGHT - 2*PAD_SIDE - RESIZE_CARD[1] + BUTTON_PAD[1],  WIDTH*0.055,   PAD_SIDE - 2*BUTTON_PAD[1]), 
                          (PAD_SIDE + RESIZE_CARD[1] + BUTTON_PAD[0],            HEIGHT//2 - HEIGHT*0.211,                              WIDTH*0.055,   PAD_SIDE - 2*BUTTON_PAD[0]), 
                          (WIDTH//2 + WIDTH*0.182,                               PAD_SIDE + RESIZE_CARD[1] + BUTTON_PAD[1],             WIDTH*0.055,   PAD_SIDE - 2*BUTTON_PAD[1]), 
                          (WIDTH - PAD_SIDE - RESIZE_CARD[1] - WIDTH*0.055 - BUTTON_PAD[0],  HEIGHT//2 + HEIGHT*0.158,                              WIDTH*0.055,   PAD_SIDE - 2*BUTTON_PAD[0])]
CUR_CALL_POSITION =      [(WIDTH//2 - WIDTH*0.182,                               HEIGHT - 2*PAD_SIDE - RESIZE_CARD[1] + BUTTON_PAD[1],  WIDTH*0.055,   PAD_SIDE - 2*BUTTON_PAD[1]), 
                          (PAD_SIDE + RESIZE_CARD[1] + BUTTON_PAD[0],            HEIGHT//2 - HEIGHT*0.158,                              WIDTH*0.055,   PAD_SIDE - 2*BUTTON_PAD[0]), 
                          (WIDTH//2 + WIDTH*0.264,                               PAD_SIDE + RESIZE_CARD[1] + BUTTON_PAD[1],             WIDTH*0.055,   PAD_SIDE - 2*BUTTON_PAD[1]), 
                          (WIDTH - PAD_SIDE - RESIZE_CARD[1] - WIDTH*0.055 - BUTTON_PAD[0],  HEIGHT//2 + HEIGHT*0.211,                              WIDTH*0.055,   PAD_SIDE - 2*BUTTON_PAD[0])]
POSSIBLE_GAME_POSITION = [(WIDTH//2,                                             HEIGHT - 2*PAD_SIDE - RESIZE_CARD[1] - BUTTON_PAD[1],  WIDTH*0.091,   PAD_SIDE - 2*BUTTON_PAD[1]),
                          (PAD_SIDE + RESIZE_CARD[1] + 3*BUTTON_PAD[0],          HEIGHT//2,                                             WIDTH*0.091,   PAD_SIDE - 2*BUTTON_PAD[0]),  
                          (WIDTH//2,                                             PAD_SIDE + RESIZE_CARD[1] + 3*BUTTON_PAD[1],           WIDTH*0.091,   PAD_SIDE - 2*BUTTON_PAD[1]),
                          (WIDTH - PAD_SIDE - RESIZE_CARD[1] - WIDTH*0.091 - 3*BUTTON_PAD[0],  HEIGHT//2,                               WIDTH*0.091,   PAD_SIDE - 2*BUTTON_PAD[0])]


MOVE_STEPS = 14

BACK = pygame.transform.scale(pygame.image.load('cards/gray_back.png'), RESIZE_CARD) 

CARDS = {
    "Ace_Clubs": pygame.transform.scale(pygame.image.load('cards/AC.png'), RESIZE_CARD),
    "King_Clubs": pygame.transform.scale(pygame.image.load('cards/KC.png'), RESIZE_CARD),
    "Queen_Clubs": pygame.transform.scale(pygame.image.load('cards/QC.png'), RESIZE_CARD),
    "Jack_Clubs": pygame.transform.scale(pygame.image.load('cards/JC.png'), RESIZE_CARD),
    "Ten_Clubs": pygame.transform.scale(pygame.image.load('cards/10C.png'), RESIZE_CARD),
    "Nine_Clubs": pygame.transform.scale(pygame.image.load('cards/9C.png'), RESIZE_CARD),
    
    "Ace_Spades": pygame.transform.scale(pygame.image.load('cards/AS.png'), RESIZE_CARD),
    "King_Spades": pygame.transform.scale(pygame.image.load('cards/KS.png'), RESIZE_CARD),
    "Queen_Spades": pygame.transform.scale(pygame.image.load('cards/QS.png'), RESIZE_CARD),
    "Jack_Spades": pygame.transform.scale(pygame.image.load('cards/JS.png'), RESIZE_CARD),
    "Ten_Spades": pygame.transform.scale(pygame.image.load('cards/10S.png'), RESIZE_CARD),
    "Nine_Spades": pygame.transform.scale(pygame.image.load('cards/9S.png'), RESIZE_CARD),
    
    "Ace_Hearts": pygame.transform.scale(pygame.image.load('cards/AH.png'), RESIZE_CARD),
    "King_Hearts": pygame.transform.scale(pygame.image.load('cards/KH.png'), RESIZE_CARD),
    "Queen_Hearts": pygame.transform.scale(pygame.image.load('cards/QH.png'), RESIZE_CARD),
    "Jack_Hearts": pygame.transform.scale(pygame.image.load('cards/JH.png'), RESIZE_CARD),
    "Ten_Hearts": pygame.transform.scale(pygame.image.load('cards/10H.png'), RESIZE_CARD),
    "Nine_Hearts": pygame.transform.scale(pygame.image.load('cards/9H.png'), RESIZE_CARD),
    
    "Ace_Diamonds": pygame.transform.scale(pygame.image.load('cards/AD.png'), RESIZE_CARD),
    "King_Diamonds": pygame.transform.scale(pygame.image.load('cards/KD.png'), RESIZE_CARD),
    "Queen_Diamonds": pygame.transform.scale(pygame.image.load('cards/QD.png'), RESIZE_CARD),
    "Jack_Diamonds": pygame.transform.scale(pygame.image.load('cards/JD.png'), RESIZE_CARD),
    "Ten_Diamonds": pygame.transform.scale(pygame.image.load('cards/10D.png'), RESIZE_CARD),
    "Nine_Diamonds": pygame.transform.scale(pygame.image.load('cards/9D.png'), RESIZE_CARD),
}

VALUES = {
    "Ace_Clubs": 11,
    "King_Clubs": 4,
    "Queen_Clubs": 3,
    "Jack_Clubs": 2,
    "Ten_Clubs": 10,
    "Nine_Clubs": 0,
    
    "Ace_Spades": 11,
    "King_Spades": 4,
    "Queen_Spades": 3,
    "Jack_Spades": 2,
    "Ten_Spades": 10,
    "Nine_Spades": 0,
    
    "Ace_Hearts": 11,
    "King_Hearts": 4,
    "Queen_Hearts": 3,
    "Jack_Hearts": 2,
    "Ten_Hearts": 10,
    "Nine_Hearts": 0,
    
    "Ace_Diamonds": 11,
    "King_Diamonds": 4,
    "Queen_Diamonds": 3,
    "Jack_Diamonds": 2,
    "Ten_Diamonds": 10,
    "Nine_Diamonds": 0,
    }

ORDER_NORM = ['Ten_Hearts',
              'Queen_Clubs','Queen_Spades','Queen_Hearts','Queen_Diamonds',
              'Jack_Clubs','Jack_Spades','Jack_Hearts','Jack_Diamonds',
              'Ace_Diamonds','Ten_Diamonds','King_Diamonds','Nine_Diamonds',
              'Ace_Clubs','Ten_Clubs','King_Clubs','Nine_Clubs',
              'Ace_Spades','Ten_Spades','King_Spades','Nine_Spades',
              'Ace_Hearts','King_Hearts','Nine_Hearts']

ORDER_PIGLET = ['Ace_Diamonds','Ten_Hearts',
              'Queen_Clubs','Queen_Spades','Queen_Hearts','Queen_Diamonds',
              'Jack_Clubs','Jack_Spades','Jack_Hearts','Jack_Diamonds',
              'Ten_Diamonds','King_Diamonds','Nine_Diamonds',
              'Ace_Clubs','Ten_Clubs','King_Clubs','Nine_Clubs',
              'Ace_Spades','Ten_Spades','King_Spades','Nine_Spades',
              'Ace_Hearts','King_Hearts','Nine_Hearts']

ORDER_QUEEN_SOLO = ['Queen_Clubs','Queen_Spades','Queen_Hearts','Queen_Diamonds',
              'Ace_Clubs','Ten_Clubs','King_Clubs','Jack_Clubs','Nine_Clubs',
              'Ace_Spades','Ten_Spades','King_Spades','Jack_Spades','Nine_Spades',
              'Ace_Hearts','Ten_Hearts','King_Hearts','Jack_Hearts','Nine_Hearts',
              'Ace_Diamonds', 'Ten_Diamonds','King_Diamonds','Jack_Diamonds','Nine_Diamonds']

ORDER_JACK_SOLO = ['Jack_Clubs','Jack_Spades','Jack_Hearts','Jack_Diamonds',
              'Ace_Clubs','Ten_Clubs','King_Clubs','Queen_Clubs','Nine_Clubs',
              'Ace_Spades','Ten_Spades','King_Spades','Queen_Spades','Nine_Spades',
              'Ace_Hearts','Ten_Hearts','King_Hearts','Queen_Hearts','Nine_Hearts',
              'Ace_Diamonds', 'Ten_Diamonds','King_Diamonds','Queen_Diamonds','Nine_Diamonds']

ORDER_MEATLESS_SOLO = ['Ace_Clubs','Ten_Clubs','King_Clubs','Queen_Clubs','Jack_Clubs','Nine_Clubs',
              'Ace_Spades','Ten_Spades','King_Spades','Queen_Spades','Jack_Spades','Nine_Spades',
              'Ace_Hearts','Ten_Hearts','King_Hearts','Queen_Hearts','Jack_Hearts','Nine_Hearts',
              'Ace_Diamonds', 'Ten_Diamonds','King_Diamonds','Queen_Diamonds','Jack_Diamonds','Nine_Diamonds']





