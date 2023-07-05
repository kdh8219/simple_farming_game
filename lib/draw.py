import pygame

from lib import farm
from lib import imgs
from lib.block import block_list
from lib.plants import plants_list
from lib.runtime_values import players

ground_images: dict[farm.Tiles, pygame.Surface] = {
    farm.Tiles.DIRT: pygame.image.load("assets/img/ground/dirt.png"),
    farm.Tiles.FARMLAND: pygame.image.load("assets/img/ground/farmland.png"),
    farm.Tiles.WATER_FARMLAND: pygame.image.load(
        "assets/img/ground/water_farmland.png"
    ),
}


def draw_ground(screen: pygame.Surface):
    tilePos = pygame.math.Vector2(0, 0)
    for line in farm.tileMap:
        for tile in line:
            if isinstance(tile, plants_list.plants_list) and not tile.water:  # type: ignore
                screen.blit(ground_images[farm.Tiles.FARMLAND], tilePos)
            elif isinstance(tile, plants_list.plants_list) and tile.water:  # type: ignore
                screen.blit(ground_images[farm.Tiles.WATER_FARMLAND], tilePos)
            elif not tile in plants_list.plants_list:
                try:
                    if tile in farm.Tiles:
                        screen.blit(ground_images[tile], tilePos)  # type: ignore
                except:
                    draw_block(screen, tilePos)
            tilePos.y += 32
        tilePos.x += 32
        tilePos.y = 0


def draw_plants():
    for line in farm.tileMap:
        for tile in line:
            if isinstance(tile, plants_list.plants_list):  # type: ignore
                tile.draw()  # type: ignore


def draw_block(screen, tilePos):
    for line in farm.tileMap:
        for tile in line:
            if isinstance(tile, block_list.block_list):  # type: ignore
                screen.blit(ground_images[farm.Tiles.DIRT], tilePos)
                tile.draw()  # type: ignore


def draw_players():
    for player in players:
        player.draw()


emoji_list = ["smile", "angry"]


def draw_text_with_border(
    screen: pygame.Surface,
    font: pygame.font.Font,
    text: str,
    inside_color: pygame.Color,
    border_color: pygame.Color,
    border_size: float,
    positon: pygame.math.Vector2,
):
    new_text = text
    for i in emoji_list:
        for _ in range(text.count(f"<{i}>")):
            smile_msg_pos = text.find(f"<{i}>")
            new_text = text.replace(f"<{i}>", "  ")

            no_smile_one = font.render(text.split(f"<{i}>")[0], True, inside_color)

            smile_pos = positon.x + no_smile_one.get_width()

            if smile_msg_pos != -1:
                screen.blit(imgs.emojis[f"{i}"], [smile_pos, positon.y])

    inside = font.render(new_text, True, inside_color)
    border = font.render(new_text, True, border_color)

    screen.blit(border, pygame.math.Vector2(positon.x - border_size, positon.y))
    screen.blit(border, pygame.math.Vector2(positon.x + border_size, positon.y))
    screen.blit(border, pygame.math.Vector2(positon.x, positon.y - border_size))
    screen.blit(border, pygame.math.Vector2(positon.x, positon.y + border_size))
    screen.blit(inside, positon)

    return inside


def process(screen: pygame.Surface):
    draw_ground(screen)
    draw_plants()
    draw_players()
