from game.screen import get_image

BIRD_UP = {'x': 708, 'y': 31, 'w': 84, 'h': 52}
BIRD_DOWN = {'x': 708, 'y': 85, 'w': 84, 'h': 60}
CACTUS = {'x': 70, 'y': 31, 'w': 46, 'h': 92}
CACTUS_DOUBLE_A = {'x': 118, 'y': 31, 'w': 64, 'h': 66}
CACTUS_DOUBLE_B = {'x': 184, 'y': 31, 'w': 80, 'h': 92}
CACTUS_TRIPLE = {'x': 266, 'y': 31, 'w': 82, 'h': 66}
CLOUD = {'x': 794, 'y': 31, 'w': 92, 'h': 28}
DINO_STILL = {'x': 350, 'y': 31, 'w': 80, 'h': 86}
DINO_LEFT = {'x': 432, 'y': 31, 'w': 80, 'h': 86}
DINO_RIGHT = {'x': 514, 'y': 31, 'w': 80, 'h': 86}
DINO_DUCK_LEFT = {'x': 596, 'y': 31, 'w': 110, 'h': 52}
DINO_DUCK_RIGHT = {'x': 596, 'y': 85, 'w': 110, 'h': 52}
GROUND = {'x': 0, 'y': 2, 'w': 2400, 'h': 28}
REPLAY_ICON = {'x': 0, 'y': 31, 'w': 68, 'h': 60}

BIRD_UP_IMG = get_image(**BIRD_UP)
BIRD_DOWN_IMG = get_image(**BIRD_DOWN)
CACTUS_IMG = get_image(**CACTUS)
CACTUS_DOUBLE_A_IMG = get_image(**CACTUS_DOUBLE_A)
CACTUS_DOUBLE_B_IMG = get_image(**CACTUS_DOUBLE_B)
CACTUS_TRIPLE_IMG = get_image(**CACTUS_TRIPLE)
CLOUD_IMG = get_image(**CLOUD)
DINO_STILL_IMG = get_image(**DINO_STILL)
DINO_LEFT_IMG = get_image(**DINO_LEFT)
DINO_RIGHT_IMG = get_image(**DINO_RIGHT)
DINO_DUCK_LEFT_IMG = get_image(**DINO_DUCK_LEFT)
DINO_DUCK_RIGHT_IMG = get_image(**DINO_DUCK_RIGHT)
GROUND_IMG = get_image(**GROUND)
REPLAY_ICON_IMG = get_image(**REPLAY_ICON)