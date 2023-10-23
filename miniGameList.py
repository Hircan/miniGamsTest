import pygame
import sys, os, random, time
from pygame.locals import *
import tetris, racingGame, runner

# 게임 경로 설정하기
GAME_ROOT_FOLDER = os.path.dirname(__file__)
IMAGE_FOLDER = os.path.join(GAME_ROOT_FOLDER, "Images")

# 이미지 가져오기
MINIGAMELIST = pygame.image.load(os.path.join(IMAGE_FOLDER, "minigameList.png"))
MINIGAMELIST = pygame.transform.scale(MINIGAMELIST, (1024, 1024))
# 게임 화면 초기화하기
screen = pygame.display.set_mode(MINIGAMELIST.get_size())

    

# 게임 끝내기 함수
# def GameOver(time_delta, manager):
#     global screen
#     global IMG_ROAD
#     #global manager
    
#     # 게임 끝내기 문자열 만들기
#     fontGameOver = pygame.font.SysFont(textFonts, textSize)
#     textGameOver = fontGameOver.render("Game Over!", True, RED)
#     rectGameOver = textGameOver.get_rect()
#     rectGameOver.center = (IMG_ROAD.get_width()//2,
#                            IMG_ROAD.get_height()//2)
    
#     fontGameOver2 = pygame.font.SysFont(textFonts, textSize//2)
#     textGameOver2 = fontGameOver2.render("Score " + str(score), True, RED)
#     rectGameOver2 = textGameOver2.get_rect()
#     rectGameOver2.center = (IMG_ROAD.get_width()//2,
#                            IMG_ROAD.get_height()//2 + 80)
#     # 검은색 배경에 게임 오버 메시지 출력하기
#     screen.fill(BLACK)
#     screen.blit(textGameOver, rectGameOver)       
#     screen.blit(textGameOver2, rectGameOver2)                                                                                                                                            

def main():
    # 게임 시작은 이곳에서
    # 파이게임 초기화하기
    pygame.init()
    
    # 프레임 매니저 초기화하기
    clock = pygame.time.Clock()

    # 프레임 레이트 설정하기
    clock.tick(60)

    # 제목 표시줄 설정하기
    pygame.display.set_caption("Mini Games")
    screen.blit(MINIGAMELIST, (0, 0))

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
                if event.key == K_1:
                    tetris.game_start()
                if event.key == K_2:
                    racingGame.game_start()
                if event.key == K_3:
                    runner.game_start()
                else:
                    print("test2")



        # 화면 업데이트하기
        pygame.display.update()