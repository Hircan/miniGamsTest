import asyncio
import pygame
import pygame_gui
import sys, os, random, time
from pygame.locals import *
import tetris, miniGameList


# 게임 경로 설정하기
GAME_ROOT_FOLDER = os.path.dirname(__file__)
IMAGE_FOLDER = os.path.join(GAME_ROOT_FOLDER, "Images")

# 이미지 가져오기
START_PAGE = pygame.image.load(os.path.join(IMAGE_FOLDER, "startPage.png"))
START_PAGE = pygame.transform.scale(START_PAGE, (1024, 768))

# 게임 화면 초기화하기
screen = pygame.display.set_mode(START_PAGE.get_size())



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


# 게임 리스트 화면
def MiniGames(screen):
    MINIGAMELIST = pygame.image.load(os.path.join(IMAGE_FOLDER, "minigameList.png"))
    miniGameScreen = pygame.display.set_mode(MINIGAMELIST.get_size())
    miniGameScreen.blit(MINIGAMELIST, (0, 0))
    print("MINIGAMES")

    # 메인 게임 루프
    while True:
        # 이벤트 확인하기
        for event in pygame.event.get():
            # 플레이어가 게임을 그만두는지?
            if event.type == K_q:
                # 게임 끝내기
                pygame.quit()
                sys.exit()
            if event.type == K_h:
                print("test")


        # 화면 업데이트하기
        pygame.display.update()

async def main(screen):
    # 게임 시작은 이곳에서
    # 파이게임 초기화하기
    pygame.init()
    
    # 프레임 매니저 초기화하기
    clock = pygame.time.Clock()

    # 프레임 레이트 설정하기
    clock.tick(60)

    # 제목 표시줄 설정하기
    pygame.display.set_caption("Mini Games")
    screen.blit(START_PAGE,(0,0))
    # 메인 게임 루프
    while True:
        # 이벤트 확인하기
        for event in pygame.event.get():
            # 플레이어가 게임을 그만두는지?
            if event.type == QUIT:
                # 게임 끝내기
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_m:
                    print("test1")
                    #MiniGames(screen)
                    #screen.blit(START_PAGE,(0,0))
                    miniGameList.main()


        # 화면 업데이트하기
        pygame.display.update()
        await asyncio.sleep(0)  # very important, and keep it 0

asyncio.run( main(screen) )
