import pygame
from color_palette import *
import random
import math

pygame.init()

WIDTH = 600
GAME_HEIGHT = 600
HEIGHT = 630
FPS = 5

my_ft_font = pygame.freetype.SysFont('Verdana', 20, pygame.font.Font.bold)
weight_font = pygame.freetype.SysFont('Verdana', 15, pygame.font.Font.bold)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"



class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0
        self.SCORE = 0
        self.LEVEL = 1
        self.LEVEL_PROGRESS = 1
        self.LEVEL_CHANGE = 3

    def move(self, max_x, max_y):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

        # checks the right border
        if self.body[0].x > max_x:
            self.body[0].x = 0
        # checks the left border
        if self.body[0].x < 0:
            self.body[0].x = max_x
        # checks the bottom border
        if self.body[0].y > max_y:
            self.body[0].y = 0
        # checks the top border
        if self.body[0].y < 0:
            self.body[0].y = max_y

    def change_level(self):
        self.LEVEL_PROGRESS = 0
        self.LEVEL += 1
        self.LEVEL_CHANGE +=1
        global FPS
        FPS += math.log(1+FPS)/2
        print(f"LEVEL CHANGED! Level: {self.LEVEL}. FPS: {FPS}")

    def draw(self, screen, CELL):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food, CELL):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            print(f"Got food! Level_progress: {self.LEVEL_PROGRESS}")
            self.SCORE +=food.weight
            self.LEVEL_PROGRESS +=food.weight
            if self.LEVEL_PROGRESS >= self.LEVEL_CHANGE:
                self.change_level()
            self.body.append(Point(head.x, head.y))
            food.generate_random_pos(CELL)

    def check_self_collision(self):
        head = self.body[0]
        for i in range(1, len(self.body)):
            if head.x == self.body[i].x and head.y == self.body[i].y:
                return True



class Food(pygame.sprite.Sprite):
    def __init__(self, CELL):
        super().__init__() 
        self.pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, GAME_HEIGHT // CELL - 1))
        self.weight = random.randint(1, 3)

    def draw(self, screen, CELL):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))
        weight_font.render_to(screen, (self.pos.x * CELL + CELL/2.6, self.pos.y * CELL + CELL/3.2), f"{self.weight}", colorBLUE)

    def generate_random_pos(self, CELL):
        self.weight = random.randint(1, 3)
        self.pos.x = random.randint(0, WIDTH // CELL - 1)
        self.pos.y = random.randint(0, GAME_HEIGHT // CELL - 1)

class TimedFood(Food):
    def __init__(self, CELL):
        super().__init__(CELL) 

    def draw(self, screen, CELL):
        pygame.draw.rect(screen, colorBLACK, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))
        weight_font.render_to(screen, (self.pos.x * CELL + CELL/2.6, self.pos.y * CELL + CELL/3.2), f"{self.weight}", colorWHITE)

    def generate_random_pos(self, CELL):
        self.kill()



class SceneBase:
    def __init__(self):
        self.next = self
    
    def ProcessInput(self, events, pressed_keys):
        print("uh-oh, you didn't override this in the child class")

    def Update(self):
        print("uh-oh, you didn't override this in the child class")

    def Render(self, screen):
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene):
        self.next = next_scene
    
    def Terminate(self):
        self.SwitchToScene(None)




def run_game(width, height, starting_scene):
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    active_scene = starting_scene

    while active_scene != None:
        pressed_keys = pygame.key.get_pressed()
        
        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                              pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True
            
            if quit_attempt:
                active_scene.Terminate()
            else:
                filtered_events.append(event)
        
        active_scene.ProcessInput(filtered_events, pressed_keys)
        active_scene.Update()
        active_scene.Render(screen)
        
        active_scene = active_scene.next
        
        pygame.display.flip()
        global FPS
        clock.tick(FPS)

# TScene models
class TitleScene(SceneBase):
    font_large = pygame.font.SysFont("Comic Sans MS", 72, True)
    font_small = pygame.font.SysFont("Comic Sans MS", 36, True)
    text_game_name = font_large.render("SNAKE", True,colorBLACK)
    text_intro = font_small.render("Press ENTER", True,colorBLACK)

    def __init__(self):
        super().__init__()
        self.font_large = pygame.font.SysFont("Comic Sans MS", 72, True)
        self.font_small = pygame.font.SysFont("Comic Sans MS", 36, True)
        self.text_game_name = self.font_large.render("SNAKE", True,colorBLACK)
        self.text_intro = self.font_small.render("Press ENTER", True,colorBLACK)
    
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.SwitchToScene(MenuScene())
    
    def Update(self):
        pass
    
    def Render(self, screen):
        screen.fill((255, 0, 0))

        screen_rect = screen.get_rect()
        text_game_name_rect = self.text_game_name.get_rect(center = (screen_rect.width // 2, screen_rect.height // 2 - 50))
        text_intro_rect = self.text_intro.get_rect(center = (screen_rect.width // 2, screen_rect.height // 2))
        screen.blit(self.text_intro, text_intro_rect)
        screen.blit(self.text_game_name, text_game_name_rect)
        # For the sake of brevity, the title scene is a blank red screen
        


class MenuScene(SceneBase):

    def __init__(self):
        super().__init__()
        self.menu_items = ["Play", "Continue", "Options", "Quit"]
        self.active_index = 0
        self.font = pygame.font.SysFont("sfpro", 60, True)
    
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and self.active_index == 0:
                    # Move to the next scene when the user pressed Enter
                    self.SwitchToScene(GameScene())
                elif event.key == pygame.K_RETURN and self.active_index == 1:
                    self.SwitchToScene(EndScene(5, 1))
                elif event.key == pygame.K_RETURN and self.active_index == 3:
                    self.Terminate()
                elif event.key == pygame.K_DOWN:
                    self.active_index += 1
                    if self.active_index >= len(self.menu_items):
                        self.active_index = 0
                elif event.key == pygame.K_UP:
                    self.active_index -= 1
                    if self.active_index < 0:
                        self.active_index = len(self.menu_items) - 1

    def Update(self):
        pass
    
    def Render(self, screen):
        screen.fill(colorGREEN)
        for i, item in enumerate(self.menu_items):
            text = item
            if i == self.active_index:
                text = '+' + text

            rendered_text = self.font.render(text, True, colorBLACK)
            screen.blit(rendered_text, (60, i * 60 + 60))

class EndScene(SceneBase):
    def __init__(self, score, level):
        super().__init__()
        self.score = score
        self.level = level

        # fonts
        self.font_large = pygame.font.SysFont("sfpro", 72, True)
        self.font_small = pygame.font.SysFont("sfpro", 36, True)
        # text
        self.text_end_game = self.font_large.render("ENDGAME", True,colorRED)
        self.text_score = self.font_small.render(f"Score: {self.score}", True,colorRED)
        self.text_level = self.font_small.render(f"Level: {self.level}", True,colorRED)
        self.text_continue = self.font_small.render(f"Press ENTER to continue", True,colorRED)
        
    
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.SwitchToScene(MenuScene())

    def Update(self):
        pass

    def Render(self, screen):
        screen.fill(colorBLACK)

        screen_rect = screen.get_rect()
        text_end_game_rect = self.text_end_game.get_rect(center = (screen_rect.width // 2, screen_rect.height // 2 - 50))
        text_score_rect = self.text_score.get_rect(center = (screen_rect.width // 2, screen_rect.height // 2))
        text_level_rect = self.text_level.get_rect(center = (screen_rect.width // 2, screen_rect.height // 2 + 40))
        text_continue_rect = self.text_continue.get_rect(center = (screen_rect.width // 2, screen_rect.height // 2 + 80))

        screen.blit(self.text_score, text_score_rect)
        screen.blit(self.text_end_game, text_end_game_rect)
        screen.blit(self.text_level, text_level_rect)
        screen.blit(self.text_continue, text_continue_rect)

class GameScene(SceneBase):

    def __init__(self):
        super().__init__()
        self.CELL = 30
        self.food = Food(self.CELL)
        self.snake = Snake()
        self.foods = pygame.sprite.Group()
        self.foods.add(self.food)
        # custom userevents
        self.TIMED_FOOD_KD = pygame.USEREVENT + 1
        self.TIMED_FOOD_TIME = self.TIMED_FOOD_KD + 1
        self.TO_SPAWN_TIMED_FOOD = True

    def draw_grid(self, screen, WIDTH, GAME_HEIGHT):
        for i in range(GAME_HEIGHT // self.CELL):
            for j in range(WIDTH // self.CELL):
                pygame.draw.rect(screen, colorGRAY, (i * self.CELL, j * self.CELL, self.CELL, self.CELL), 1)

    def draw_grid_chess(self, screen, WIDTH, GAME_HEIGHT):
        colors = [colorWHITE, colorGRAY]

        for i in range(GAME_HEIGHT // self.CELL):
            for j in range(WIDTH // self.CELL):
                pygame.draw.rect(screen, colors[(i + j) % 2], (i * self.CELL, j * self.CELL, self.CELL, self.CELL))

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and self.snake.dx != -1:
                    self.snake.dx = 1
                    self.snake.dy = 0
                elif event.key == pygame.K_LEFT and self.snake.dx != 1:
                    self.snake.dx = -1
                    self.snake.dy = 0
                elif event.key == pygame.K_DOWN and self.snake.dy != -1:
                    self.snake.dx = 0
                    self.snake.dy = 1
                elif event.key == pygame.K_UP and self.snake.dy != 1:
                    self.snake.dx = 0
                    self.snake.dy = -1
            if event.type == self.TIMED_FOOD_KD: # TIMED FOOD
                print("TIMED FOOD SPAWNED")
                self.TO_SPAWN_TIMED_FOOD = False
                pygame.time.set_timer(self.TIMED_FOOD_TIME, 6000, 1)
                self.timed_food = TimedFood(self.CELL)
                self.foods.add(self.timed_food)
            if event.type == self.TIMED_FOOD_TIME:
                self.timed_food.kill()
                self.TO_SPAWN_TIMED_FOOD = True
        
    def Update(self):
        if self.snake.check_self_collision():
                self.SwitchToScene(EndScene(self.snake.SCORE, self.snake.LEVEL))
        max_x = WIDTH // self.CELL - 1
        max_y = GAME_HEIGHT // self.CELL - 1
        for entity in self.foods:
                self.snake.check_collision(entity, self.CELL)
        self.snake.move(max_x, max_y)
        if self.TO_SPAWN_TIMED_FOOD: 
            pygame.time.set_timer(self.TIMED_FOOD_KD, 2000, 1)
            self.TO_SPAWN_TIMED_FOOD = False

    
    def Render(self, screen):
        screen.fill(colorBLACK)
        self.draw_grid_chess(screen, WIDTH, GAME_HEIGHT)
        my_ft_font.render_to(screen, (10, HEIGHT-22), f"SCORE: {self.snake.SCORE}", colorGREEN)
        my_ft_font.render_to(screen, (WIDTH - 100, HEIGHT-22), f"LVL: {self.snake.LEVEL}", colorYELLOW)

        self.snake.draw(screen, self.CELL)
        for entity in self.foods:
            entity.draw(screen, self.CELL)

run_game(WIDTH, HEIGHT, TitleScene())