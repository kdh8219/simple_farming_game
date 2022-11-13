import sys
import os
import pygame
import math
import asset.tilemap.farm as farm

print("TESTER : OTTO\nIF MACOS : SYSTEM SETING > KEYBORD > INPUT SOURCE > CAPS LOOK KEY ABC INPUT SOURCE TRANSFORM OFF")

pygame.init()

# 함수

# 변수
var = "alpha"
hw = (960, 640)
running = True
screen = pygame.display.set_mode(hw)
clock = pygame.time.Clock()
# 색변수
SKYBLUE = (113, 199, 245)
BLACK = (255,255,255)
WHITE = (0,0,0)
# 플래이어 변수
playerImg = pygame.image.load("asset/img/player.png")
playerPos = [900,100]
# 타일맵
dirtImg = pygame.image.load("asset/img/dirt.png")
farmlandImg = pygame.image.load("asset/img/farmland.png")
farmRiceImg = pygame.image.load("asset/img/farm_rice_0.png")
# 글시
lsFont = pygame.font.Font( "asset/font/Galmuri.ttf", 20)
# 이미지
selectImg = [pygame.image.load("asset/img/rice_seed.png"), 1]
# 좌표
selectPos = [0,50]

# 세팅
pygame.display.set_caption(f"sfg {var}! - by newkin")

# 게임와일
while running:
    plyerTilePos = [math.trunc(playerPos[0]/32),math.trunc(playerPos[1]/32)]
    verText = lsFont.render(f"SFG {var}!  플래이어 왼쪽위가 기준입니다!                                                          {plyerTilePos}", True, BLACK)
    verTextOutline = lsFont.render(f"SFG {var}!  플래이어 왼쪽위가 기준입니다!                                                          {plyerTilePos}", True, WHITE)

    screen.fill(SKYBLUE) # 화면 채우기
    
    for event in pygame.event.get():  # 키입력 감지
        # 나가기
        if event.type == pygame.QUIT:  # 나가기 버튼 눌럿을때
            running = False  # 와일문 나가기
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dir = "l"
            elif event.key == pygame.K_RIGHT:
                dir = "r"
            elif event.key == pygame.K_UP:
                dir = "u"
            elif event.key == pygame.K_DOWN:
                dir = "d"
            if event.key == pygame.K_f:
                farm.tileMap[plyerTilePos[1]][plyerTilePos[0]] = 2
                print(plyerTilePos)
            if event.key == pygame.K_0:
                selectImg[0] = pygame.image.load("asset/img/none.png")
                selectImg[1] = 0
            elif event.key == pygame.K_1:
                selectImg[0] = pygame.image.load("asset/img/rice_seed.png")
                selectImg[1] = 1
            if event.key == pygame.K_d:
                if (selectImg[1] == 1) and (farm.tileMap[plyerTilePos[1]][plyerTilePos[0]] == 2):
                    farm.tileMap[plyerTilePos[1]][plyerTilePos[0]] = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                dir = ""
            elif event.key == pygame.K_DOWN:
                dir = ""
            elif event.key == pygame.K_LEFT:
                dir = ""
            elif event.key == pygame.K_RIGHT:
                dir = ""   
    # 플래이어
    # 경계
    if playerPos[0] >= hw[0]-32:
        print(playerPos)
        playerPos[0] = hw[0]-33
    if playerPos[0] <= 0:
        print(playerPos)
        playerPos[0] = 1
    if playerPos[1] >= hw[1]-32:
        print(playerPos)
        playerPos[1] = hw[1]-32
    if playerPos[1] <= 1:
        print(playerPos)
        playerPos[1] = 1
    # 움직이기
    speed = 1
    if dir == "l":
        playerPos[0] -= speed
    elif dir == "r":
        playerPos[0] += speed
    elif dir == "u":
        playerPos[1] -= speed
    elif dir == "d":
        playerPos[1] += speed
    # 중심잡기
    
    # 타일맵
    tilePos = [0,0]
    for line in farm.tileMap:
        for tile in line:
            if tile == 1:
                screen.blit(dirtImg, tilePos)
            if tile == 2:
                screen.blit(farmlandImg, tilePos)
            if tile == 3:
                screen.blit(farmRiceImg, tilePos)
            tilePos[0] += 32
        tilePos[1] += 32
        tilePos[0] = 0
    # 밭 갈기 todo: 파이게임 기본 입력 말고 따로 입력받는 라이브러리 불러와서 사용

    
    # 이미지 그리기
    screen.blit(playerImg, playerPos)
    screen.blit(selectImg[0], selectPos)
    screen.blit(verTextOutline, (10+2,10))
    screen.blit(verTextOutline, (10-2,10))
    screen.blit(verTextOutline, (10,10+2))
    screen.blit(verTextOutline, (10,10-2))
    screen.blit(verText, (10,10))

    pygame.display.update() # 화면 업데이트

pygame.quit()