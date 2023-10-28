import pygame
import sys, os, random, time
from pygame.locals import *
import tetris, racingGame, runner

# 게임 경로 설정하기
GAME_ROOT_FOLDER = os.path.dirname(__file__)
IMAGE_FOLDER = os.path.join(GAME_ROOT_FOLDER, "Images")
VIDEO_FOLDER = os.path.join(GAME_ROOT_FOLDER, "videos")

# 게임 화면 초기화하기
screen = pygame.display.set_mode((1024, 768))

# 이미지 가져오기
# MINIGAMELIST = pygame.image.load(os.path.join(IMAGE_FOLDER, "minigameList.png")).convert_alpha()
# MINIGAMELIST = pygame.transform.scale(MINIGAMELIST, (1024, 768))
LOBBY = pygame.image.load(os.path.join(IMAGE_FOLDER, "Lobby.png")).convert_alpha()
LOBBY = pygame.transform.scale(LOBBY, (1024, 768))

LOADING = pygame.image.load(os.path.join(IMAGE_FOLDER, "loading.png")).convert_alpha()
#LOADING = pygame.transform.scale(LOADING, (1024, 768))

LEFT_ARROW = pygame.image.load(os.path.join(IMAGE_FOLDER, "Left_Arrow.png")).convert_alpha()
LEFT_ARROW = pygame.transform.scale(LEFT_ARROW, (139, 121))
LEFT_ARROW_GET_RECT = LEFT_ARROW.get_rect(left=50, top=324)

LEFT_ARROW_CLICK = pygame.image.load(os.path.join(IMAGE_FOLDER, "Left_Arrow_Click.png")).convert_alpha()
LEFT_ARROW_CLICK = pygame.transform.scale(LEFT_ARROW_CLICK, (139, 121))

RIGHT_ARROW = pygame.image.load(os.path.join(IMAGE_FOLDER, "Right_Arrow.png")).convert_alpha()
RIGHT_ARROW = pygame.transform.scale(RIGHT_ARROW, (139, 121))
RIGHT_ARROW_GET_RECT = RIGHT_ARROW.get_rect(left=835, top=324)

RIGHT_ARROW_CLICK = pygame.image.load(os.path.join(IMAGE_FOLDER, "Right_Arrow_Click.png")).convert_alpha()
RIGHT_ARROW_CLICK = pygame.transform.scale(RIGHT_ARROW_CLICK, (139, 121))

PLAY_BUTTON = pygame.image.load(os.path.join(IMAGE_FOLDER, "Play_Button.png")).convert_alpha()
PLAY_BUTTON = pygame.transform.scale(PLAY_BUTTON, (251, 107))
PLAY_BUTTON_GET_RECT = PLAY_BUTTON.get_rect(left=179, top=610)

PLAY_BUTTON_CLICK = pygame.image.load(os.path.join(IMAGE_FOLDER, "Play_Button_Click.png")).convert_alpha()
PLAY_BUTTON_CLICK = pygame.transform.scale(PLAY_BUTTON_CLICK, (251, 107))


HELP_BUTTON = pygame.image.load(os.path.join(IMAGE_FOLDER, "Help_Button.png")).convert_alpha()
HELP_BUTTON = pygame.transform.scale(HELP_BUTTON, (251, 107))
HELP_BUTTON_GET_RECT = HELP_BUTTON.get_rect(left=585, top=610)

HELP_BUTTON_CLICK = pygame.image.load(os.path.join(IMAGE_FOLDER, "Help_Button_Click.png")).convert_alpha()
HELP_BUTTON_CLICK = pygame.transform.scale(HELP_BUTTON_CLICK, (251, 107)) 

RACING_GAME = pygame.image.load(os.path.join(IMAGE_FOLDER, "RACING_GAME.png")).convert_alpha()
TETRIS_GAME = pygame.image.load(os.path.join(IMAGE_FOLDER, "TETRIS_GAME.png")).convert_alpha()
RUNNING_GAME = pygame.image.load(os.path.join(IMAGE_FOLDER, "RUNNING_GAME.png")).convert_alpha()

def main():
    # 게임 시작은 이곳에서
    # 파이게임 초기화하기
    pygame.init()
    
    # 프레임 매니저 초기화하기
    clock = pygame.time.Clock()

    # 프레임 레이트 설정하기
    clock.tick(60)

    # index 및 게임 종류 셋팅
    minigames = ['racing', 'tetris', 'running']
    index = 0

    # 제목 표시줄 설정하기
    pygame.display.set_caption("Mini Games")
    screen.blit(LOBBY, (0, 0))
    screen.blit(LOADING, (344,134))
    screen.blit(LEFT_ARROW, (50, 324))
    screen.blit(RIGHT_ARROW, (835, 324))
    screen.blit(PLAY_BUTTON, (179, 610))
    screen.blit(HELP_BUTTON, (585, 610))

    if minigames[index] == "racing":
        screen.blit(RACING_GAME, (344,134))
    elif minigames[index] == "tetris":
        screen.blit(TETRIS_GAME, (344,134))
    elif minigames[index] == "running":
        screen.blit(RUNNING_GAME, (344,134))

    print('LEFT BUTTON POS : ', (LEFT_ARROW.get_width(), LEFT_ARROW.get_height()))
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
            if LEFT_ARROW_GET_RECT.collidepoint(pygame.mouse.get_pos()):
                #print('in mousehover')
                screen.blit(LEFT_ARROW_CLICK, (50, 324))
                if event.type == MOUSEBUTTONDOWN:
                    index -= 1
                    if(index < 0):
                            index = len(minigames)-1
                    print(index)
                    if minigames[index] == "racing":
                        screen.blit(RACING_GAME, (344,134))
                    elif minigames[index] == "tetris":
                        screen.blit(TETRIS_GAME, (344,134))
                    elif minigames[index] == "running":
                        screen.blit(RUNNING_GAME, (344,134))
            else:
                screen.blit(LEFT_ARROW, (50, 324))
                
            if RIGHT_ARROW_GET_RECT.collidepoint(pygame.mouse.get_pos()):
                #print('in mousehover')
                screen.blit(RIGHT_ARROW_CLICK, (835, 324))
                if event.type == MOUSEBUTTONDOWN:
                    index += 1
                    if index > len(minigames)-1:
                        index = 0
                    print(index)
                    if minigames[index] == "racing":
                        screen.blit(RACING_GAME, (344,134))
                    elif minigames[index] == "tetris":
                        screen.blit(TETRIS_GAME, (344,134))
                    elif minigames[index] == "running":
                        screen.blit(RUNNING_GAME, (344,134))
                                        
                    
            else:
                screen.blit(RIGHT_ARROW, (835, 324))
            
            if PLAY_BUTTON_GET_RECT.collidepoint(pygame.mouse.get_pos()):
                screen.blit(PLAY_BUTTON_CLICK, (179, 610))
                if event.type == MOUSEBUTTONDOWN:
                    if minigames[index] == "racing":
                        racingGame.game_start()
                    elif minigames[index] == "tetris":
                        tetris.game_start()
                    elif minigames[index] == "running":
                        runner.game_start()
            else:
                screen.blit(PLAY_BUTTON, (179, 610))
            
            if HELP_BUTTON_GET_RECT.collidepoint(pygame.mouse.get_pos()):
                screen.blit(HELP_BUTTON_CLICK, (585, 610))
                #if event.type == MOUSEBUTTONDOWN:
            else:
                screen.blit(HELP_BUTTON, (585, 610))

        # 화면 업데이트하기
        pygame.display.update()
