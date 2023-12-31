import asyncio
import pygame
import pygame_gui
import sys, os, random, time
from pygame.locals import *
import tetris

# 게임 색상 정의하기
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)

# 게임 변수 초기화하기
startSpeed = 5
moveSpeed = startSpeed
maxSpeed = 10
score = 0
eNum = -1
paused = False
textFonts = ['comicsansms','arial']
textSize = 48

# 게임 경로 설정하기
GAME_ROOT_FOLDER = os.path.dirname(__file__)
IMAGE_FOLDER = os.path.join(GAME_ROOT_FOLDER, "Images")

# 이미지 가져오기
IMG_ROAD = pygame.image.load(os.path.join(IMAGE_FOLDER, "Road.png"))
IMG_PLAYER = pygame.image.load(os.path.join(IMAGE_FOLDER, "Player.png"))
IMG_ENEMIES = []
IMG_ENEMIES.append(pygame.image.load(os.path.join(IMAGE_FOLDER, "Enemy.png")))
IMG_ENEMIES.append(pygame.image.load(os.path.join(IMAGE_FOLDER, "Enemy2.png")))
IMG_ENEMIES.append(pygame.image.load(os.path.join(IMAGE_FOLDER, "Enemy3.png")))
IMG_ENEMIES.append(pygame.image.load(os.path.join(IMAGE_FOLDER, "IceCube.png")))

MAIN_HOMT = pygame.image.load(os.path.join(IMAGE_FOLDER, "mainHome.jpg"))

# 게임 화면 초기화하기
screen = pygame.display.set_mode(MAIN_HOMT.get_size())



# 게임 끝내기 함수
def GameOver(time_delta, manager):
    global screen
    global IMG_ROAD
    #global manager
    
    # 게임 끝내기 문자열 만들기
    fontGameOver = pygame.font.SysFont(textFonts, textSize)
    textGameOver = fontGameOver.render("Game Over!", True, RED)
    rectGameOver = textGameOver.get_rect()
    rectGameOver.center = (IMG_ROAD.get_width()//2,
                           IMG_ROAD.get_height()//2)
    
    fontGameOver2 = pygame.font.SysFont(textFonts, textSize//2)
    textGameOver2 = fontGameOver2.render("Score " + str(score), True, RED)
    rectGameOver2 = textGameOver2.get_rect()
    rectGameOver2.center = (IMG_ROAD.get_width()//2,
                           IMG_ROAD.get_height()//2 + 80)
    # 검은색 배경에 게임 오버 메시지 출력하기
    screen.fill(BLACK)
    screen.blit(textGameOver, rectGameOver)       
    screen.blit(textGameOver2, rectGameOver2)                                                                                                                                            



    replay_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                             text='REPLAY',
                                             manager=manager)
    mainhome_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((650, 275), (300, 50)),
                                             text='MAIN_HOME',
                                             manager=manager) 


    # 이벤트 확인하기
    while (True):
        for event in pygame.event.get():
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == replay_button:
                    #startButton = True
                    print('test')
                    replay_button.kill()
                if event.ui_element == mainhome_button:
                    print('test2')
                    mainhome_button.kill()
                    tetris.game_start()
            manager.process_events(event)

        manager.update(time_delta)
        manager.draw_ui(screen)

        pygame.display.update()
    

    # 출력 업데이트하기
    

    

    # 일시 정지하기
    #time.sleep()

    # 게임 끝내기 
    #pygame.quit()
    #sys.exit()

async def main():
    global startSpeed
    global moveSpeed
    global maxSpeed
    global score
    global eNum
    global paused
    global textFonts
    global textSize

    # 이미지 가져오기
    global IMG_ROAD
    global IMG_PLAYER
    global IMG_ENEMIES

    # 게임 화면 초기화하기
    global screen

    # 게임 시작은 이곳에서
    # 파이게임 초기화하기
    pygame.init()

    manager = pygame_gui.UIManager(MAIN_HOMT.get_size())
    
    hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                             text='Game Start',
                                             manager=manager)
    
    # 프레임 매니저 초기화하기
    clock = pygame.time.Clock()

    # 프레임 레이트 설정하기
    clock.tick(60)

    # 제목 표시줄 설정하기
    pygame.display.set_caption("Crazy Driver")

    # 게임 객체 만들기
    # 플레이어 초기 위치 계산하기
    h = IMG_ROAD.get_width()//2
    v = IMG_ROAD.get_height() - (IMG_PLAYER.get_height()//2)
    # player 스프라이트 만들기
    player = pygame.sprite.Sprite()
    player.image = IMG_PLAYER
    player.surf = pygame.Surface(IMG_PLAYER.get_size())
    player.rect = player.surf.get_rect(center = (h, v))

    startButton = False

    # 메인 게임 루프
    while True:
        time_delta = clock.tick(60)/1000.0
        # 제목 표시줄 점수 업데이트하기
        pygame.display.set_caption("Crazy Driver - Score " + str(score))

        # 메인 화면
        screen.blit(MAIN_HOMT, (0, 0))
        
        if startButton == True:
            # 배경 두기
            screen.blit(IMG_ROAD, (0, 0))
            #screen.blit(MAIN_HOMT, (0, 0))

            # 플레이어 화면에 두기
            screen.blit(player.image, player.rect)

            # 적이 있는지 확인하기
            if eNum == -1:
                # 무작위로 적 발생시키기
                eNum = random.randrange(0, len(IMG_ENEMIES))
                # 적 초기 위치 계산하기
                hl = IMG_ENEMIES[eNum].get_width()//2
                hr = IMG_ROAD.get_width() - (IMG_ENEMIES[eNum].get_width()//2)
                h = random.randrange(hl, hr)
                v = 0
                # enemy 스프라이트 만들기
                enemy = pygame.sprite.Sprite()
                enemy.image = IMG_ENEMIES[eNum]
                enemy.surf = pygame.Surface(IMG_ENEMIES[eNum].get_size())
                enemy.rect = enemy.surf.get_rect(center = (h, v))


            # 키보드를 눌렀을 때
            keys = pygame.key.get_pressed()

            # 일시 정지인지?
            if paused:
                # 스페이스 키 확인하기
                if not keys[K_SPACE]:
                    # 일시 정지 끄기
                    # 이전 속도로 되돌리기
                    moveSpeed = tempSpeed
                    # 일시 정지 아니라고 표시하기
                    paused = False
            else:
                # 왼쪽 화살표 키인지 확인하기
                if keys[K_LEFT] and player.rect.left > 0:
                    # 왼쪽으로 움직이기
                    player.rect.move_ip(-moveSpeed, 0)
                    # 너무 왼쪽으로 가지 않도록 하기
                    if player.rect.left < 0:
                        # 너무 갔다면 되돌리기
                        player.rect.left = 0
                # 오른쪽 화살표 키인지 확인하기
                if keys[K_RIGHT] and player.rect.right < IMG_ROAD.get_width():
                    # 오른쪽으로 움직이기
                    player.rect.move_ip(moveSpeed, 0)
                    # 너무 오른쪽으로 가지 않도록 하기
                    if player.rect.right > IMG_ROAD.get_width():
                        # 너무 갔다면 되돌리기
                        player.rect.right = IMG_ROAD.get_width()
                # 스페이스 키 확인하기 key
                if keys[K_SPACE]:
                    # 일시 정지 켜기
                    # 게임 속도 저장하기
                    tempSpeed = moveSpeed
                    # 속도를 0으로 설정하기
                    moveSpeed = 0
                    # 일시 정지 중이라 표시하기
                    paused = True

            # 적 화면에 두기
            screen.blit(enemy.image, enemy.rect)

            # 적을 아래쪽으로 움직이기       
            enemy.rect.move_ip(0, moveSpeed)

            # 화면 밖으로 나갔는지 확인하기
            if (enemy.rect.bottom > IMG_ROAD.get_height()):
                # enemy 객체 없애기
                enemy.kill()
                # 적 없음
                eNum = -1
                # 점수 올리기
                score += 1
                # 속도 올리기
                moveSpeed += 1
                # 속도 올리기
                if moveSpeed < maxSpeed:
                    moveSpeed += 1

            # 충돌 확인하기
            if eNum >= 0 and pygame.sprite.collide_rect(player, enemy):
                # 적 번호가 3인지?
                if eNum == 3:
                    # 얼음덩어리라면 속도 되돌리기
                    moveSpeed = startSpeed
                else:
                    # 충돌! 게임 오버
                    GameOver(time_delta, manager)

        # 이벤트 확인하기
        for event in pygame.event.get():
            # 플레이어가 게임을 그만두는지?
            if event.type == QUIT:
                # 게임 끝내기
                pygame.quit()
                sys.exit()
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == hello_button:
                    print("test")
                    startButton = True
                    hello_button.kill()

            manager.process_events(event)

        manager.update(time_delta)

        manager.draw_ui(screen)

        # 화면 업데이트하기
        pygame.display.update()
        await asyncio.sleep(0)  # very important, and keep it 0

asyncio.run( main() )
