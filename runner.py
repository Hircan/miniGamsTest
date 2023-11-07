import pygame
import os
from sys import exit
from random import randint, choice

GAME_ROOT_FOLDER = os.path.dirname(__file__)
GRAPHICS_FOLDER = os.path.join(GAME_ROOT_FOLDER, "graphics")
SOUND_FOLDER = os.path.join(GAME_ROOT_FOLDER, "audio")
FONT_FOLDER = os.path.join(GAME_ROOT_FOLDER, "font")

class runner:
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
		self.snail_surf = self.snail_frames[snail_frame_index]

		# Fly
		self.fly_frame1 = pygame.image.load(os.path.join(GRAPHICS_FOLDER, 'Fly/Fly1.png')).convert_alpha()
		self.fly_frame2 = pygame.image.load(os.path.join(GRAPHICS_FOLDER, 'Fly/Fly2.png')).convert_alpha()
		self.fly_frames = [self.fly_frame1, self.fly_frame2]
		self.fly_frame_index = 0
		self.fly_surf = self.fly_frames[fly_frame_index]

		self.obstacle_rect_list = []

		self.player_walk_1 = pygame.image.load(os.path.join(GRAPHICS_FOLDER, 'Player/player_walk_1.png')).convert_alpha()
		self.player_walk_2 = pygame.image.load(os.path.join(GRAPHICS_FOLDER, 'Player/player_walk_2.png')).convert_alpha()
		self.player_walk = [self.player_walk_1,self.player_walk_2]
		self.player_index = 0
		self.player_jump = pygame.image.load(os.path.join(GRAPHICS_FOLDER, 'Player/jump.png')).convert_alpha()

		self.player_surf = self.player_walk[player_index]
		self.player_rect = player_surf.get_rect(midbottom = (80,300))
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

		global fly_frame_index
		global snail_frame_index

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
					if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
						game_active = True
						
						start_time = int(pygame.time.get_ticks() / 1000)

				if game_active:
					if event.type == obstacle_timer:
						self.obstacle_group.add(self.Obstacle(choice(['fly','snail','snail','snail'])))
						# if randint(0,2):
						# 	obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900,1100),300)))
						# else:
						# 	obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900,1100),210)))

					if event.type == snail_animation_timer:
						if snail_frame_index == 0: snail_frame_index = 1
						else: snail_frame_index = 0
						snail_surf = self.snail_frames[snail_frame_index] 

					if event.type == fly_animation_timer:
						if fly_frame_index == 0: fly_frame_index = 1
						else: fly_frame_index = 0
						fly_surf = self.fly_frames[fly_frame_index] 


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

	

