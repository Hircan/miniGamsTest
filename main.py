import asyncio
import pygame
import pygame_gui
import sys, os, random, time
from pygame.locals import *
from random import randint, choice

# 게임 경로 설정하기
GAME_ROOT_FOLDER = os.path.dirname(__file__)
IMAGE_FOLDER = os.path.join(GAME_ROOT_FOLDER, "Images")
GRAPHICS_FOLDER = os.path.join(GAME_ROOT_FOLDER, "graphics")
SOUND_FOLDER = os.path.join(GAME_ROOT_FOLDER, "audio")
FONT_FOLDER = os.path.join(GAME_ROOT_FOLDER, "font")
# 이미지 가져오기
START_PAGE = pygame.image.load(os.path.join(IMAGE_FOLDER, "startPage.png"))
START_PAGE = pygame.transform.scale(START_PAGE, (1024, 768))

# 게임 화면 초기화하기
screen = pygame.display.set_mode(START_PAGE.get_size())

class Robby:
    # 게임 화면 초기화하기
    global robby_screen
    robby_screen = pygame.display.set_mode((1024, 768))

    # 이미지 가져오기
    global LOBBY
    global LOADING
    global LEFT_ARROW
    global LEFT_ARROW_GET_RECT
    global LEFT_ARROW_CLICK
    global RIGHT_ARROW
    global RIGHT_ARROW_GET_RECT
    global RIGHT_ARROW_CLICK
    global PLAY_BUTTON
    global PLAY_BUTTON_GET_RECT
    global PLAY_BUTTON_CLICK
    global HELP_BUTTON
    global HELP_BUTTON_GET_RECT
    global HELP_BUTTON_CLICK
    global RACING_GAME
    global TETRIS_GAME
    global RUNNING_GAME

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

    def setblit(self, minigames, index):
        robby_screen = pygame.display.set_mode((1024, 768))
        # 제목 표시줄 설정하기
        pygame.display.set_caption("Mini Games")
        robby_screen.blit(LOBBY, (0, 0))
        robby_screen.blit(LOADING, (344,134))
        robby_screen.blit(LEFT_ARROW, (50, 324))
        robby_screen.blit(RIGHT_ARROW, (835, 324))
        robby_screen.blit(PLAY_BUTTON, (179, 610))
        robby_screen.blit(HELP_BUTTON, (585, 610))

        if minigames[index] == "racing":
            robby_screen.blit(RACING_GAME, (344,134))
        elif minigames[index] == "tetris":
            robby_screen.blit(TETRIS_GAME, (344,134))
        elif minigames[index] == "running":
            robby_screen.blit(RUNNING_GAME, (344,134))

    def main(self):
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

        self.setblit(minigames, index)

        #변수 선언
        global racingGame
        global tetris
        global runner
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
                # if event.type == KEYDOWN:
                #     if event.key == K_1:
                #         #tetris.game_start()
                #         print("테스리스")
                #     if event.key == K_2:
                #         racingGame = RacingGame()
                #         racingGame.game_start()
                #         print("테스트")
                #     if event.key == K_3:
                #         print("런너")
                #         #runner.game_start()
                #     else:
                #         print("test2")
                if LEFT_ARROW_GET_RECT.collidepoint(pygame.mouse.get_pos()):
                    #print('in mousehover')
                    robby_screen.blit(LEFT_ARROW_CLICK, (50, 324))
                    if event.type == MOUSEBUTTONDOWN:
                        index -= 1
                        if(index < 0):
                                index = len(minigames)-1
                        print(index)
                        if minigames[index] == "racing":
                            robby_screen.blit(RACING_GAME, (344,134))
                        elif minigames[index] == "tetris":
                            robby_screen.blit(TETRIS_GAME, (344,134))
                        elif minigames[index] == "running":
                            robby_screen.blit(RUNNING_GAME, (344,134))
                else:
                    robby_screen.blit(LEFT_ARROW, (50, 324))
                    
                if RIGHT_ARROW_GET_RECT.collidepoint(pygame.mouse.get_pos()):
                    #print('in mousehover')
                    robby_screen.blit(RIGHT_ARROW_CLICK, (835, 324))
                    if event.type == MOUSEBUTTONDOWN:
                        index += 1
                        if index > len(minigames)-1:
                            index = 0
                        print(index)
                        if minigames[index] == "racing":
                            robby_screen.blit(RACING_GAME, (344,134))
                        elif minigames[index] == "tetris":
                            robby_screen.blit(TETRIS_GAME, (344,134))
                        elif minigames[index] == "running":
                            robby_screen.blit(RUNNING_GAME, (344,134))
                                            
                        
                else:
                    robby_screen.blit(RIGHT_ARROW, (835, 324))
                
                if PLAY_BUTTON_GET_RECT.collidepoint(pygame.mouse.get_pos()):
                    robby_screen.blit(PLAY_BUTTON_CLICK, (179, 610))
                    if event.type == MOUSEBUTTONDOWN:
                        if minigames[index] == "racing":
                            racingGame = RacingGame()
                            racingGame.main()
                            self.setblit(minigames, index)
                        elif minigames[index] == "tetris":
                            tetris = Tetris()
                            tetris.game_start()
                            self.setblit(minigames, index)
                        elif minigames[index] == "running":
                            print("테스트")
                            runner = Runner()
                            runner.game_start()
                            self.setblit(minigames, index)
                else:
                    robby_screen.blit(PLAY_BUTTON, (179, 610))
                
                if HELP_BUTTON_GET_RECT.collidepoint(pygame.mouse.get_pos()):
                    robby_screen.blit(HELP_BUTTON_CLICK, (585, 610))
                    #if event.type == MOUSEBUTTONDOWN:
                else:
                    robby_screen.blit(HELP_BUTTON, (585, 610))

            # 화면 업데이트하기
            
            pygame.display.update()

class RacingGame:

    # 전역 변수 선언
    global IMG_ROAD
    global racing_screen
    global IMG_PLAYER
    global IMG_ENEMIES
    global startSpeed
    global moveSpeed
    global maxSpeed
    global score
    global eNum
    global paused
    global textFonts
    global textSize
    global BLACK
    global WHITE
    global RED

    def __init__(self): 
        # 게임 색상 정의하기
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED   = (255, 0, 0)

        # 게임 변수 초기화하기
        self.startSpeed = 5                          # 시작 스피드
        self.moveSpeed = self.startSpeed
        self.maxSpeed = 10                           # 최고 스피드
        self.score = 0                               # 점수
        self.eNum = -1                               # 적의 개수 -1 : 적이 없음
        self.paused = False
        self.textFonts = ['comicsansms','arial']
        self.textSize = 48
        self.endGame = False

    # 게임 경로 설정하기
    #GAME_ROOT_FOLDER = os.path.dirname(__file__)
    #IMAGE_FOLDER = os.path.join(GAME_ROOT_FOLDER, "Images")


    # 배경 가져오기
    IMG_ROAD = pygame.image.load(os.path.join(IMAGE_FOLDER, "Road.png"))
    # 게임 화면 초기화하기
    #racing_screen = pygame.display.set_mode(IMG_ROAD.get_size())

    # 이미지 가져오기
    IMG_ROAD = pygame.image.load(os.path.join(IMAGE_FOLDER, "Road.png")).convert_alpha()
    IMG_PLAYER = pygame.image.load(os.path.join(IMAGE_FOLDER, "Player.png")).convert_alpha()
    IMG_ENEMIES = []
    IMG_ENEMIES.append(pygame.image.load(os.path.join(IMAGE_FOLDER, "Enemy.png")).convert_alpha())
    IMG_ENEMIES.append(pygame.image.load(os.path.join(IMAGE_FOLDER, "Enemy2.png")).convert_alpha())
    IMG_ENEMIES.append(pygame.image.load(os.path.join(IMAGE_FOLDER, "Enemy3.png")).convert_alpha())
    IMG_ENEMIES.append(pygame.image.load(os.path.join(IMAGE_FOLDER, "IceCube.png")).convert_alpha())

    

    # 게임 끝내기 함수
    def GameOver(self):
        # 게임 끝내기 문자열 만들기
        fontGameOver = pygame.font.SysFont(self.textFonts, self.textSize)
        textGameOver = fontGameOver.render("Game Over!", True, self.RED)
        rectGameOver = textGameOver.get_rect()
        rectGameOver.center = (IMG_ROAD.get_width()//2,
                            IMG_ROAD.get_height()//2)
        
        fontGameOver2 = pygame.font.SysFont(self.textFonts, self.textSize//2)
        textGameOver2 = fontGameOver2.render("Score " + str(self.score), True, self.RED)
        rectGameOver2 = textGameOver2.get_rect()
        rectGameOver2.center = (IMG_ROAD.get_width()//2,
                            IMG_ROAD.get_height()//2 + 80)
        
        # 검은색 배경에 게임 오버 메시지 출력하기
        racing_screen = pygame.display.set_mode(IMG_ROAD.get_size())
        racing_screen.fill(self.BLACK)
        racing_screen.blit(textGameOver, rectGameOver)       
        racing_screen.blit(textGameOver2, rectGameOver2)                                                                                                                                            

        pygame.display.update()

        # 이벤트 확인하기
        while True:
            # 키보드를 눌렀을 때
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                # 플레이어가 게임을 그만두는지?
                if event.type == QUIT:
                    # 게임 끝내기
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        self.endGame = False
                        return
                    if event.key == K_e:
                        self.endGame = True
                        return


        
    def main(self):
        # 이미지 가져오기
        #global IMG_ROAD
        #global IMG_PLAYER
        #global IMG_ENEMIES

        # 게임 화면 초기화하기

        # 게임 시작은 이곳에서
        # 파이게임 초기화하기
        pygame.init()

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
        ONCE = True
        # 메인 게임 루프
        while True:
            time_delta = clock.tick(60)/1000.0

            # 배경 두기
            if(ONCE == True):
                racing_screen = pygame.display.set_mode(IMG_ROAD.get_size())
                ONCE = False
            racing_screen.blit(IMG_ROAD, (0,0))
            #screen.blit(MAIN_HOME, (0, 0))

            # 플레이어 화면에 두기
            racing_screen.blit(player.image, player.rect)

            # 적이 있는지 확인하기
            if self.eNum == -1:
                # 무작위로 적 발생시키기
                self.eNum = random.randrange(0, len(IMG_ENEMIES))
                # 적 초기 위치 계산하기
                hl = IMG_ENEMIES[self.eNum].get_width()//2
                hr = IMG_ROAD.get_width() - (IMG_ENEMIES[self.eNum].get_width()//2)
                h = random.randrange(hl, hr)
                v = 0
                # enemy 스프라이트 만들기
                enemy = pygame.sprite.Sprite()
                enemy.image = IMG_ENEMIES[self.eNum]
                enemy.surf = pygame.Surface(IMG_ENEMIES[self.eNum].get_size())
                enemy.rect = enemy.surf.get_rect(center = (h, v))


            # 키보드를 눌렀을 때
            keys = pygame.key.get_pressed()

            # 일시 정지인지?
            if self.paused:
                # 스페이스 키 확인하기
                if not keys[K_SPACE]:
                    # 일시 정지 끄기
                    # 이전 속도로 되돌리기
                    self.moveSpeed = tempSpeed
                    # 일시 정지 아니라고 표시하기
                    self.paused = False
            else:
                # 왼쪽 화살표 키인지 확인하기
                if keys[K_LEFT] and player.rect.left > 0:
                    # 왼쪽으로 움직이기
                    player.rect.move_ip(-self.moveSpeed, 0)
                    # 너무 왼쪽으로 가지 않도록 하기
                    if player.rect.left < 0:
                        # 너무 갔다면 되돌리기
                        player.rect.left = 0
                # 오른쪽 화살표 키인지 확인하기
                if keys[K_RIGHT] and player.rect.right < IMG_ROAD.get_width():
                    # 오른쪽으로 움직이기
                    player.rect.move_ip(self.moveSpeed, 0)
                    # 너무 오른쪽으로 가지 않도록 하기
                    if player.rect.right > IMG_ROAD.get_width():
                        # 너무 갔다면 되돌리기
                        player.rect.right = IMG_ROAD.get_width()
                # 스페이스 키 확인하기 key
                if keys[K_SPACE]:
                    # 일시 정지 켜기
                    # 게임 속도 저장하기
                    tempSpeed = self.moveSpeed
                    # 속도를 0으로 설정하기
                    self.moveSpeed = 0
                    # 일시 정지 중이라 표시하기
                    self.paused = True

            # 적 화면에 두기
            racing_screen.blit(enemy.image, enemy.rect)

            # 적을 아래쪽으로 움직이기       
            enemy.rect.move_ip(0, self.moveSpeed)

            # 화면 밖으로 나갔는지 확인하기
            if (enemy.rect.bottom > IMG_ROAD.get_height()):
                # enemy 객체 없애기
                enemy.kill()
                # 적 없음
                self.eNum = -1
                # 점수 올리기
                self.score += 1
                # 속도 올리기
                self.moveSpeed += 1
                # 속도 올리기
                if self.moveSpeed < self.maxSpeed:
                    self.moveSpeed += 1

            # 충돌 확인하기
            if self.eNum >= 0 and pygame.sprite.collide_rect(player, enemy):
                # 적 번호가 3인지?
                if self.eNum == 3:
                    # 얼음덩어리라면 속도 되돌리기
                    self.moveSpeed = self.startSpeed
                else:
                    # 충돌! 게임 오버
                    self.GameOver()
                    if(self.endGame):
                        return
                    #ONCE = True
                    enemy.kill()
                    self.eNum = -1
                    self.score = 0
                    self.moveSpeed = 5

            # 이벤트 확인하기
            for event in pygame.event.get():
                # 플레이어가 게임을 그만두는지?
                if event.type == QUIT:
                    # 게임 끝내기
                    pygame.quit()
                    sys.exit()

            # 화면 업데이트하기
            pygame.display.update()

class Tetris:
    pygame.font.init()
    pygame.mixer.init()

    global SOUND_FOLDER
    global move_sound
    global clear_sound
    SOUND_FOLDER = os.path.join(GAME_ROOT_FOLDER, "audio")
    move_sound = pygame.mixer.Sound(os.path.join(SOUND_FOLDER, 'Tetris-block-move-sound-effect.wav'))
    clear_sound = pygame.mixer.Sound(os.path.join(SOUND_FOLDER, 'clear.wav'))

    # GLOBALS VARS
    def __init__(self):
        self.s_width = 1024
        self.s_height = 768
        self.play_width = 300  # meaning 300 // 10 = 30 width per block
        self.play_height = 600  # meaning 600 // 20 = 30 height per block
        self.block_size = 30

        self.top_left_x = (self.s_width - self.play_width) // 2
        self.top_left_y = self.s_height - self.play_height
        self.run = True
          

        # SHAPE FORMATS

        S = [['.....',
            '.....',
            '..00.',
            '.00..',
            '.....'],
            ['.....',
            '..0..',
            '..00.',
            '...0.',
            '.....']]

        Z = [['.....',
            '.....',
            '.00..',
            '..00.',
            '.....'],
            ['.....',
            '..0..',
            '.00..',
            '.0...',
            '.....']]

        I = [['..0..',
            '..0..',
            '..0..',
            '..0..',
            '.....'],
            ['.....',
            '0000.',
            '.....',
            '.....',
            '.....']]

        O = [['.....',
            '.....',
            '.00..',
            '.00..',
            '.....']]

        J = [['.....',
            '.0...',
            '.000.',
            '.....',
            '.....'],
            ['.....',
            '..00.',
            '..0..',
            '..0..',
            '.....'],
            ['.....',
            '.....',
            '.000.',
            '...0.',
            '.....'],
            ['.....',
            '..0..',
            '..0..',
            '.00..',
            '.....']]

        L = [['.....',
            '...0.',
            '.000.',
            '.....',
            '.....'],
            ['.....',
            '..0..',
            '..0..',
            '..00.',
            '.....'],
            ['.....',
            '.....',
            '.000.',
            '.0...',
            '.....'],
            ['.....',
            '.00..',
            '..0..',
            '..0..',
            '.....']]

        T = [['.....',
            '..0..',
            '.000.',
            '.....',
            '.....'],
            ['.....',
            '..0..',
            '..00.',
            '..0..',
            '.....'],
            ['.....',
            '.....',
            '.000.',
            '..0..',
            '.....'],
            ['.....',
            '..0..',
            '.00..',
            '..0..',
            '.....']]
        self.shapes = [S, Z, I, O, J, L, T]
        
        self.shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
    # index 0 - 6 represent shape


    class Piece(object):  # *
        def __init__(self, my, x, y, shape):
            self.x = x
            self.y = y
            self.shape = shape
            self.color = my.shape_colors[my.shapes.index(shape)]
            self.rotation = 0


    def create_grid(self, locked_pos={}):  # *
        grid = [[(0,0,0) for _ in range(10)] for _ in range(20)]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (j, i) in locked_pos:
                    c = locked_pos[(j,i)]
                    grid[i][j] = c
        return grid


    def convert_shape_format(self, shape):
        positions = []
        format = shape.shape[shape.rotation % len(shape.shape)]

        for i, line in enumerate(format):
            row = list(line)
            for j, column in enumerate(row):
                if column == '0':
                    positions.append((shape.x + j, shape.y + i))

        for i, pos in enumerate(positions):
            positions[i] = (pos[0] - 2, pos[1] - 4)

        return positions


    def valid_space(self, shape, grid):
        accepted_pos = [[(j, i) for j in range(10) if grid[i][j] == (0,0,0)] for i in range(20)]
        accepted_pos = [j for sub in accepted_pos for j in sub]

        formatted = self.convert_shape_format(shape)

        for pos in formatted:
            if pos not in accepted_pos:
                if pos[1] > -1:
                    return False
        return True


    def check_lost(self, positions):
        for pos in positions:
            x, y = pos
            if y < 1:
                return True

        return False


    def get_shape(self):
        return self.Piece(self, 5, 0, random.choice(self.shapes))


    def draw_text_middle(self, surface, text, size, color):
        font = pygame.font.SysFont("comicsans", size, bold=True)
        label = font.render(text, 1, color)

        surface.blit(label, (self.top_left_x + self.play_width /2 - (label.get_width()/2), self.top_left_y + self.play_height/2 - label.get_height()/2))


    def draw_grid(self, surface, grid):
        sx = self.top_left_x
        sy = self.top_left_y

        for i in range(len(grid)):
            pygame.draw.line(surface, (128,128,128), (sx, sy + i*self.block_size), (sx+self.play_width, sy+ i*self.block_size))
            for j in range(len(grid[i])):
                pygame.draw.line(surface, (128, 128, 128), (sx + j*self.block_size, sy),(sx + j*self.block_size, sy + self.play_height))


    def clear_rows(self, grid, locked):

        inc = 0
        for i in range(len(grid)-1, -1, -1):
            row = grid[i]
            if (0,0,0) not in row:
                inc += 1
                ind = i
                for j in range(len(row)):
                    try:
                        del locked[(j,i)]
                    except:
                        continue

        if inc > 0:
            for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
                x, y = key
                if y < ind:
                    newKey = (x, y + inc)
                    locked[newKey] = locked.pop(key)
                    clear_sound.play()

        return inc


    def draw_next_shape(self, shape, surface):
        font = pygame.font.SysFont('comicsans', 30)
        label = font.render('Next Shape', 1, (255,255,255))

        sx = self.top_left_x + self.play_width + 90
        sy = self.top_left_y + self.play_height/2 - 80
        format = shape.shape[shape.rotation % len(shape.shape)]

        for i, line in enumerate(format):
            row = list(line)
            for j, column in enumerate(row):
                if column == '0':
                    pygame.draw.rect(surface, shape.color, (sx + j*self.block_size, sy + i*self.block_size, self.block_size, self.block_size), 0)

        surface.blit(label, (sx, sy - 50))


    def update_score(self, nscore):
        score = self.max_score()
        file_path = GAME_ROOT_FOLDER + '/scores.txt'
        with open(file_path, 'w') as f:
            print(file_path)
            if int(score) > nscore:
                print("1")
                f.write(str(score))
                f.close()
            else:
                print("2")
                f.write(str(nscore))
                f.close()


    def max_score(self):
        file_path = GAME_ROOT_FOLDER + '/scores.txt'
        with open(file_path, 'r') as r:
            print(r)
            lines = r.readlines()
            print(lines)
            if lines:
                score = lines[0].strip()
                r.close()
                return score
            else:
                score = "0"
                r.close()
                return score


    def draw_window(self, surface, grid, score=0, last_score = 0):
        surface.fill((0, 0, 0))

        pygame.font.init()
        font = pygame.font.SysFont('comicsans', 60)
        label = font.render('Tetris', 1, (255, 255, 255))

        surface.blit(label, (self.top_left_x + self.play_width / 2 - (label.get_width() / 2), 30))

        # current score
        font = pygame.font.SysFont('comicsans', 30)
        label = font.render('Score: ' + str(score), 1, (255,255,255))

        sx = self.top_left_x + self.play_width + 50
        sy = self.top_left_y + self.play_height/2 - 100

        surface.blit(label, (sx + 60, sy + 160))
        # last score
        label = font.render('High Score: ' + last_score, 1, (255,255,255))

        sx = self.top_left_x - 250
        sy = self.top_left_y + 200

        surface.blit(label, (sx, sy + 160))

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                pygame.draw.rect(surface, grid[i][j], (self.top_left_x + j*self.block_size, self.top_left_y + i*self.block_size, self.block_size, self.block_size), 0)

        pygame.draw.rect(surface, (255, 0, 0), (self.top_left_x, self.top_left_y, self.play_width, self.play_height), 5)

        self.draw_grid(surface, grid)
        #pygame.display.update()


    def main(self, win):  # *
        last_score = self.max_score()
        locked_positions = {}
        grid = self.create_grid(locked_positions)

        change_piece = False
        self.run = True
        current_piece = self.get_shape()
        next_piece = self.get_shape()
        clock = pygame.time.Clock()
        fall_time = 0
        fall_speed = 0.27
        level_time = 0
        score = 0

        while self.run:
            grid = self.create_grid(locked_positions)
            fall_time += clock.get_rawtime()
            level_time += clock.get_rawtime()
            clock.tick()

            if level_time/1000 > 5:
                level_time = 0
                if level_time > 0.12:
                    level_time -= 0.005

            if fall_time/1000 > fall_speed:
                fall_time = 0
                current_piece.y += 1
                if not(self.valid_space(current_piece, grid)) and current_piece.y > 0:
                    current_piece.y -= 1
                    change_piece = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.display.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        move_sound.play()
                        current_piece.x -= 1
                        if not(self.valid_space(current_piece, grid)):
                            current_piece.x += 1
                    if event.key == pygame.K_RIGHT:
                        move_sound.play()
                        current_piece.x += 1
                        if not(self.valid_space(current_piece, grid)):
                            current_piece.x -= 1
                    if event.key == pygame.K_DOWN:
                        move_sound.play()
                        current_piece.y += 1
                        if not(self.valid_space(current_piece, grid)):
                            current_piece.y -= 1
                    if event.key == pygame.K_UP:
                        move_sound.play()
                        current_piece.rotation += 1
                        if not(self.valid_space(current_piece, grid)):
                            current_piece.rotation -= 1

            shape_pos = self.convert_shape_format(current_piece)

            for i in range(len(shape_pos)):
                x, y = shape_pos[i]
                if y > -1:
                    grid[y][x] = current_piece.color

            if change_piece:
                for pos in shape_pos:
                    p = (pos[0], pos[1])
                    locked_positions[p] = current_piece.color
                current_piece = next_piece
                next_piece = self.get_shape()
                change_piece = False
                score += self.clear_rows(grid, locked_positions) * 10

            self.draw_window(win, grid, score, last_score)
            self.draw_next_shape(next_piece, win)
            pygame.display.update()

            if self.check_lost(locked_positions):
                self.draw_text_middle(win, "YOU LOST!", 80, (255,255,255))
                pygame.display.update()
                pygame.time.delay(1500)
                
                while self.run:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == K_e:
                                self.run = False
                            if event.key == K_r:
                                self.update_score(score)
                                return

                self.update_score(score)


    def main_menu(self, win):  # *
        self.run = True
        while self.run:
            win.fill((0,0,0))
            self.draw_text_middle(win, 'Press Any Key To Play', 60, (255,255,255))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.KEYDOWN:
                    self.main(win)
            if self.run == False:
                return
        


    def game_start(self):
        win = pygame.display.set_mode((self.s_width, self.s_height))
        pygame.display.set_caption('Tetris')
        self.main_menu(win)

class Runner:
	def __init__(self):
		self.screen = pygame.display.set_mode((800,400))
		self.test_font = pygame.font.Font(os.path.join(FONT_FOLDER,'Pixeltype.ttf'), 50)
		self.start_time = 0

		self.player = pygame.sprite.GroupSingle()
		self.player.add(self.Player())

		self.obstacle_group = pygame.sprite.Group()

		# Snail 
		self.snail_frame_1 = pygame.image.load(os.path.join(GRAPHICS_FOLDER, 'snail/snail1.png')).convert_alpha()
		self.snail_frame_2 = pygame.image.load(os.path.join(GRAPHICS_FOLDER, 'snail/snail2.png')).convert_alpha()
		self.snail_frames = [self.snail_frame_1, self.snail_frame_2]
		self.snail_frame_index = 0
		self.snail_surf = self.snail_frames[self.snail_frame_index]

		# Fly
		self.fly_frame1 = pygame.image.load(os.path.join(GRAPHICS_FOLDER, 'Fly/Fly1.png')).convert_alpha()
		self.fly_frame2 = pygame.image.load(os.path.join(GRAPHICS_FOLDER, 'Fly/Fly2.png')).convert_alpha()
		self.fly_frames = [self.fly_frame1, self.fly_frame2]
		self.fly_frame_index = 0
		self.fly_surf = self.fly_frames[self.fly_frame_index]

		self.obstacle_rect_list = []

		self.player_walk_1 = pygame.image.load(os.path.join(GRAPHICS_FOLDER, 'Player/player_walk_1.png')).convert_alpha()
		self.player_walk_2 = pygame.image.load(os.path.join(GRAPHICS_FOLDER, 'Player/player_walk_2.png')).convert_alpha()
		self.player_walk = [self.player_walk_1,self.player_walk_2]
		self.player_index = 0
		self.player_jump = pygame.image.load(os.path.join(GRAPHICS_FOLDER, 'Player/jump.png')).convert_alpha()

		self.player_surf = self.player_walk[self.player_index]
		self.player_rect = self.player_surf.get_rect(midbottom = (80,300))
		self.player_gravity = 0

		# Intro screen
		self.player_stand = pygame.image.load(os.path.join(GRAPHICS_FOLDER, 'Player/player_stand.png')).convert_alpha()
		self.player_stand = pygame.transform.rotozoom(self.player_stand,0,2)
		self.player_stand_rect = self.player_stand.get_rect(center = (400,200))

		self.game_name = self.test_font.render('Pixel Runner',False,(111,196,169))
		self.game_name_rect = self.game_name.get_rect(center = (400,80))

		self.game_message = self.test_font.render('Press space to run',False,(111,196,169))
		self.game_message_rect = self.game_message.get_rect(center = (400,330))

	class Player(pygame.sprite.Sprite):
		def __init__(self):
			super().__init__()
			player_walk_1 = pygame.image.load(os.path.join(GRAPHICS_FOLDER, 'Player/player_walk_1.png')).convert_alpha()
			player_walk_2 = pygame.image.load(os.path.join(GRAPHICS_FOLDER, 'Player/player_walk_2.png')).convert_alpha()
			self.player_walk = [player_walk_1,player_walk_2]
			self.player_index = 0
			self.player_jump = pygame.image.load(os.path.join(GRAPHICS_FOLDER, 'Player/jump.png')).convert_alpha()

			self.image = self.player_walk[self.player_index]
			self.rect = self.image.get_rect(midbottom = (80,300))
			self.gravity = 0

			#self.jump_sound = pygame.mixer.Sound(os.path.join(SOUND_FOLDER,'jump.mp3'))
			#self.jump_sound.set_volume(0.5)

		def player_input(self):
			keys = pygame.key.get_pressed()
			if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
				self.gravity = -20
				#self.jump_sound.play()

		def apply_gravity(self):
			self.gravity += 1
			self.rect.y += self.gravity
			if self.rect.bottom >= 300:
				self.rect.bottom = 300

		def animation_state(self):
			if self.rect.bottom < 300: 
				self.image = self.player_jump
			else:
				self.player_index += 0.1
				if self.player_index >= len(self.player_walk):self.player_index = 0
				self.image = self.player_walk[int(self.player_index)]

		def update(self):
			self.player_input()
			self.apply_gravity()
			self.animation_state()

	class Obstacle(pygame.sprite.Sprite):
		def __init__(self,type):
			super().__init__()
			
			if type == 'fly':
				fly_1 = pygame.image.load(os.path.join(GRAPHICS_FOLDER, 'Fly/Fly1.png')).convert_alpha()
				fly_2 = pygame.image.load(os.path.join(GRAPHICS_FOLDER, 'Fly/Fly2.png')).convert_alpha()
				self.frames = [fly_1,fly_2]
				y_pos = 210
			else:
				snail_1 = pygame.image.load(os.path.join(GRAPHICS_FOLDER, 'snail/snail1.png')).convert_alpha()
				snail_2 = pygame.image.load(os.path.join(GRAPHICS_FOLDER, 'snail/snail2.png')).convert_alpha()
				self.frames = [snail_1,snail_2]
				y_pos  = 300

			self.animation_index = 0
			self.image = self.frames[self.animation_index]
			self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos))

		def animation_state(self):
			self.animation_index += 0.1 
			if self.animation_index >= len(self.frames): self.animation_index = 0
			self.image = self.frames[int(self.animation_index)]

		def update(self):
			self.animation_state()
			self.rect.x -= 6
			self.destroy()

		def destroy(self):
			if self.rect.x <= -100: 
				self.kill()


	def display_score(self):
		current_time = int(pygame.time.get_ticks() / 1000) - self.start_time
		score_surf = self.test_font.render(f'Score: {current_time}',False,(64,64,64))
		score_rect = score_surf.get_rect(center = (400,50))
		self.screen.blit(score_surf,score_rect)
		return current_time

	def obstacle_movement(self, obstacle_list):
		if obstacle_list:
			for obstacle_rect in obstacle_list:
				obstacle_rect.x -= 5

				if obstacle_rect.bottom == 300: self.screen.blit(self.snail_surf,obstacle_rect)
				else: self.screen.blit(self.fly_surf,obstacle_rect)

			obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

			return obstacle_list
		else: return []

	def collisions(self, player,obstacles):
		if obstacles:
			for obstacle_rect in obstacles:
				if player.colliderect(obstacle_rect): return False
		return True

	def collision_sprite(self):
		if pygame.sprite.spritecollide(self.player.sprite,self.obstacle_group,False):
			self.obstacle_group.empty()
			score = 0
			return False
		else: return True

	def player_animation(self):
		global player_surf, player_index

		if self.player_rect.bottom < 300:
			player_surf = self.player_jump
		else:
			player_index += 0.1
			if player_index >= len(self.player_walk):player_index = 0
			player_surf = self.player_walk[int(player_index)]



	def game_start(self):
		pygame.init()
		screen = pygame.display.set_mode((800,400))
		pygame.display.set_caption('Runner')
		clock = pygame.time.Clock()
		
		game_active = False
		
		score = 0
		bg_music = pygame.mixer.Sound(os.path.join(SOUND_FOLDER,'music.wav'))
		bg_music.play(loops = -1)

		#Groups
		

		sky_surface = pygame.image.load(os.path.join(GRAPHICS_FOLDER, 'Sky.png')).convert()
		ground_surface = pygame.image.load(os.path.join(GRAPHICS_FOLDER, 'ground.png')).convert()

		# score_surf = test_font.render('My game', False, (64,64,64))
		# score_rect = score_surf.get_rect(center = (400,50))

		

		# Timer 
		obstacle_timer = pygame.USEREVENT + 1
		pygame.time.set_timer(obstacle_timer,1500)

		snail_animation_timer = pygame.USEREVENT + 2
		pygame.time.set_timer(snail_animation_timer,500)

		fly_animation_timer = pygame.USEREVENT + 3
		pygame.time.set_timer(fly_animation_timer,200)

		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()
				
				if game_active:
					if event.type == pygame.MOUSEBUTTONDOWN:
						if self.player_rect.collidepoint(event.pos) and self.player_rect.bottom >= 300: 
							player_gravity = -20
					
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_SPACE and self.player_rect.bottom >= 300:
							player_gravity = -20
				else:
					if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
						game_active = True
						self.start_time = int(pygame.time.get_ticks() / 1000)
                        
					if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
						bg_music.stop()
						return

				if game_active:
					if event.type == obstacle_timer:
						self.obstacle_group.add(self.Obstacle(choice(['fly','snail','snail','snail'])))
						# if randint(0,2):
						# 	obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900,1100),300)))
						# else:
						# 	obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900,1100),210)))

					if event.type == snail_animation_timer:
						if self.snail_frame_index == 0: self.snail_frame_index = 1
						else: self.snail_frame_index = 0
						snail_surf = self.snail_frames[self.snail_frame_index] 

					if event.type == fly_animation_timer:
						if self.fly_frame_index == 0: self.fly_frame_index = 1
						else: self.fly_frame_index = 0
						fly_surf = self.fly_frames[self.fly_frame_index] 


			if game_active:
				screen.blit(sky_surface,(0,0))
				screen.blit(ground_surface,(0,300))
				# pygame.draw.rect(screen,'#c0e8ec',score_rect)
				# pygame.draw.rect(screen,'#c0e8ec',score_rect,10)
				# screen.blit(score_surf,score_rect)
				score = self.display_score()
				
				# snail_rect.x -= 4
				# if snail_rect.right <= 0: snail_rect.left = 800
				# screen.blit(snail_surf,snail_rect)

				# Player 
				# player_gravity += 1
				# player_rect.y += player_gravity
				# if player_rect.bottom >= 300: player_rect.bottom = 300
				# player_animation()
				# screen.blit(player_surf,player_rect)
				self.player.draw(screen)
				self.player.update()

				self.obstacle_group.draw(screen)
				self.obstacle_group.update()

				# Obstacle movement 
				# obstacle_rect_list = obstacle_movement(obstacle_rect_list)

				# collision 
				game_active = self.collision_sprite()
				# game_active = collisions(player_rect,obstacle_rect_list)
				
			else:
				screen.fill((94,129,162))
				screen.blit(self.player_stand,self.player_stand_rect)
				self.obstacle_rect_list.clear()
				self.player_rect.midbottom = (80,300)
				player_gravity = 0

				score_message = self.test_font.render(f'Your score: {score}',False,(111,196,169))
				score_message_rect = score_message.get_rect(center = (400,330))
				screen.blit(self.game_name,self.game_name_rect)

				if score == 0: screen.blit(self.game_message,self.game_message_rect)
				else: screen.blit(score_message,score_message_rect)

			pygame.display.update()
			clock.tick(60)
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
                    #tetris.game_start()
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
                print("test1")
                #MiniGames(screen)
                #screen.blit(START_PAGE,(0,0))
                #miniGameList.main()
                robby = Robby()
                robby.main()


        # 화면 업데이트하기
        pygame.display.update()
        await asyncio.sleep(0)  # very important, and keep it 0

asyncio.run( main(screen) )
