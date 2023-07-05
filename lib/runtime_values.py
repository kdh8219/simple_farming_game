import os
import platform
from typing import Tuple

import pygame

from lib import player
from lib.logger import logger

version_type = Tuple[str, int, int, int]
version: version_type = ("beta", 1, 0, 3)

pcInfo = {
    "core": os.cpu_count(),
    "os": platform.system(),
    "processor": platform.processor(),
    "osvar": platform.version(),
}

setting = {}
lang = {}


window_size = (960, 640)
screen = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()

logs = logger()

running: bool

players: list[player.player] = []
my_dir: player.Direction = player.Direction.STOP
fps: int = 100

on_setting = False
font = pygame.font.Font("assets/font/Galmuri.ttf", 20)

SKYBLUE = pygame.Color(113, 199, 245)
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
BLUE = pygame.Color(61, 139, 255)
