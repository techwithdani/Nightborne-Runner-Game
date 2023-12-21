import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        nightborne_run_1 = pygame.transform.rotozoom(
            pygame.image.load("graphics/nightbornerun/NightBorne_run1.png"),0,3).convert_alpha()
        nightborne_run_2 = pygame.transform.rotozoom(
            pygame.image.load("graphics/nightbornerun/NightBorne_run2.png"),0,3).convert_alpha()
        nightborne_run_3 = pygame.transform.rotozoom(
            pygame.image.load("graphics/nightbornerun/NightBorne_run3.png"),0,3).convert_alpha()
        nightborne_run_4 = pygame.transform.rotozoom(
            pygame.image.load("graphics/nightbornerun/NightBorne_run4.png"),0,3).convert_alpha()
        nightborne_run_5 = pygame.transform.rotozoom(
            pygame.image.load("graphics/nightbornerun/NightBorne_run5.png"),0,3).convert_alpha()
        nightborne_run_6 = pygame.transform.rotozoom(
            pygame.image.load("graphics/nightbornerun/NightBorne_run6.png"),0,3).convert_alpha()
        
        self.player_jump = nightborne_run_4
        self.player_run = [nightborne_run_1, nightborne_run_2, nightborne_run_3,
                           nightborne_run_4, nightborne_run_5, nightborne_run_6]
        self.player_index = 0

        self.gravity = 0
        self.image = self.player_run[self.player_index]
        self.rect = self.image.get_rect(center = (80, 330))

        self.jump_sound = pygame.mixer.Sound("audio/jump.mp3")
        self.jump_sound.set_volume(0.2)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 330:
            self.gravity = -20
            self.jump_sound.play()

    def gravity_apply(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 330:
            self.rect.bottom = 330

    def player_animation(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.15
            if self.player_index > len(self.player_run):
                self.player_index = 0
            self.image = self.player_run[int(self.player_index)]

    def update(self):
        self.player_input()
        self.gravity_apply()
        self.player_animation()

class IntroPlayer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.is_animating = True
        nightborneidle_1 = pygame.transform.rotozoom(
            pygame.image.load("graphics/nightborneidle/NightBorne_idle1.png"),0,5).convert_alpha()
        nightborneidle_2 = pygame.transform.rotozoom(
            pygame.image.load("graphics/nightborneidle/NightBorne_idle2.png"),0,5).convert_alpha()
        nightborneidle_3 = pygame.transform.rotozoom(
            pygame.image.load("graphics/nightborneidle/NightBorne_idle3.png"),0,5).convert_alpha()
        nightborneidle_4 = pygame.transform.rotozoom(
            pygame.image.load("graphics/nightborneidle/NightBorne_idle4.png"),0,5).convert_alpha()
        nightborneidle_5 = pygame.transform.rotozoom(
            pygame.image.load("graphics/nightborneidle/NightBorne_idle5.png"),0,5).convert_alpha()
        nightborneidle_6 = pygame.transform.rotozoom(
            pygame.image.load("graphics/nightborneidle/NightBorne_idle6.png"),0,5).convert_alpha()
        nightborneidle_7 = pygame.transform.rotozoom(
            pygame.image.load("graphics/nightborneidle/NightBorne_idle7.png"),0,5).convert_alpha()
        nightborneidle_8 = pygame.transform.rotozoom(
            pygame.image.load("graphics/nightborneidle/NightBorne_idle8.png"),0,5).convert_alpha()
        nightborneidle_9 = pygame.transform.rotozoom(
            pygame.image.load("graphics/nightborneidle/NightBorne_idle9.png"),0,5).convert_alpha()
        
        self.player_idle = [nightborneidle_1, nightborneidle_2, nightborneidle_3, nightborneidle_4, nightborneidle_5,
                            nightborneidle_6, nightborneidle_7, nightborneidle_8, nightborneidle_9]
        self.player_idle_index = 0
        self.image = self.player_idle[self.player_idle_index]
        self.rect = self.image.get_rect(center = (500, 200))

    def animate(self):
        self.is_animating = True

    def update(self, speed):
        if self.is_animating == True:
            self.player_idle_index += speed

            if self.player_idle_index >= len(self.player_idle):
                self.player_idle_index = 0
            self.image = self.player_idle[int(self.player_idle_index)]

class Enemy(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()

        if type == 'bat':
            bat_1 = pygame.transform.rotozoom(
            pygame.image.load("graphics/batflying/bat1.png"),0,3).convert_alpha()
            bat_2 = pygame.transform.rotozoom(
            pygame.image.load("graphics/batflying/bat2.png"),0,3).convert_alpha()
            bat_3 = pygame.transform.rotozoom(
            pygame.image.load("graphics/batflying/bat3.png"),0,3).convert_alpha()
            bat_4 = pygame.transform.rotozoom(
            pygame.image.load("graphics/batflying/bat4.png"),0,3).convert_alpha()
            bat_5 = pygame.transform.rotozoom(
            pygame.image.load("graphics/batflying/bat5.png"),0,3).convert_alpha()
            bat_6 = pygame.transform.rotozoom(
            pygame.image.load("graphics/batflying/bat6.png"),0,3).convert_alpha()
            self.frames = [bat_1,bat_2,bat_3,bat_4,bat_5,bat_6]
            y_pos = 200
        else:
            hellhound_1 = pygame.transform.rotozoom(
            pygame.image.load("graphics/hellhoundrun/hellhoundrun_1.png"),0,3).convert_alpha()
            hellhound_2 = pygame.transform.rotozoom(
            pygame.image.load("graphics/hellhoundrun/hellhoundrun_2.png"),0,3).convert_alpha()
            hellhound_3 = pygame.transform.rotozoom(
            pygame.image.load("graphics/hellhoundrun/hellhoundrun_3.png"),0,3).convert_alpha()
            hellhound_4 = pygame.transform.rotozoom(
            pygame.image.load("graphics/hellhoundrun/hellhoundrun_4.png"),0,3).convert_alpha()
            hellhound_5 = pygame.transform.rotozoom(
            pygame.image.load("graphics/hellhoundrun/hellhoundrun_5.png"),0,3).convert_alpha()
            self.frames = [hellhound_1, hellhound_2, hellhound_3, hellhound_4, hellhound_5]
            y_pos = 299

        self.animate_index = 0
        self.image = self.frames[self.animate_index]
        self.rect = self.image.get_rect(center = (randint(1200, 1300), y_pos))

    def enemy_animation(self):
        self.animate_index += 0.16
        if self.animate_index >= len(self.frames):
            self.animate_index = 0
        self.image = self.frames[int(self.animate_index)]

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

    def update(self):
        self.enemy_animation()
        self.rect.x -= 15
        self.destroy()

def display_score():
    global current_time
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = game_font.render(f"Score: {current_time}", False, (139, 0, 0))
    score_rect = score_surf.get_rect(center = (500, 40))
    WINDOW.blit(score_surf, score_rect)
    return current_time

def sprite_collisions():
    if pygame.sprite.spritecollide(player_group.sprite, enemy_group, False):
        enemy_group.empty()
        return False
    else:
        return True
    
def draw_bg():
    for i in range(5):
        for j in bg_images:
            WINDOW.blit(j, ((i * bg_width) + scroll, 0))

def draw_ground():
    for i in range(15):
        WINDOW.blit(ground_image, ((i * ground_width + 1) + scroll, HEIGHT - ground_height))

pygame.init()
WIDTH, HEIGHT = 1000, 400
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
GAME_NAME = pygame.display.set_caption("Nightborne Runner")
FPS = 60
clock = pygame.time.Clock()
game_font = pygame.font.Font("font/GlitchGoblin.ttf", 40)
is_game_active = False
start_time = 0
game_score = 0
scroll = 0
game_music = pygame.mixer.Sound("audio/battle.mp3")
game_music.play(loops = -1)

#class groups
player_group = pygame.sprite.GroupSingle()
player_group.add(Player())
playeridle_group = pygame.sprite.GroupSingle()
playeridle_group.add(IntroPlayer())
enemy_group = pygame.sprite.Group()

# Layered background (parallax scrolling)
ground_image = pygame.image.load("graphics/background/Layer1.png")
ground_width = ground_image.get_width()
ground_height = ground_image.get_height()
bg_images = []
for i in range(1, 6):
    bg_image = pygame.image.load(f"graphics/background/plx-{i}.png").convert_alpha()
    bg_images.append(bg_image)
bg_width = bg_images[0].get_width()

# Intro text
game_name = game_font.render("NightBorne Runner", False, (139, 0, 0))
game_name_rect = game_name.get_rect(center = (500, 50))
game_message = game_font.render("Press SPACE to run", False, (139, 0, 0))
game_message_rect = game_message.get_rect(center = (500, 350))

# Timer
enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, 800)

# Main game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()
        
        if is_game_active:
            if event.type == enemy_timer:
                enemy_group.add(Enemy(choice(['hellhound', 'bat', 'hellhound', 'bat'])))
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                is_game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)

    if is_game_active:
        draw_bg()
        draw_ground()
        game_score = display_score()

        player_group.draw(WINDOW)
        player_group.update()

        enemy_group.draw(WINDOW)
        enemy_group.update()

        is_game_active = sprite_collisions()
    
    else:
        WINDOW.fill((48, 25, 52))
        playeridle_group.draw(WINDOW)
        playeridle_group.update(0.18)

        final_score = game_font.render(f"Your score: {game_score}", False, (139, 0, 0))
        final_score_rect = final_score.get_rect(center = (500, 350))
        WINDOW.blit(game_name, game_name_rect)

        if game_score == 0:
            WINDOW.blit(game_message, game_message_rect)
        else:
            WINDOW.blit(final_score, final_score_rect)

    scroll -= 11
    if abs(scroll) > bg_width:
        scroll = 0

    pygame.display.update()
    clock.tick(FPS)