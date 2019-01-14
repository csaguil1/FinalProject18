import pygame
import random
import time

pygame.init()

window_width = 800
window_height = 600

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Gacha Game")

black = (0,0,0)
red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)

clock = pygame.time.Clock()
clock.tick(60)

back = pygame.image.load("background.png")
kimjihun = pygame.image.load("kimjh.png")

def text_objects(text, font):
    """text"""
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def text_box(text, font):
    """text box"""

def button(msg,x,y,w,h,ic,ac,action=None):
    """buttons"""
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(window, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(window, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    window.blit(textSurf, textRect)

def game_intro():
    """intro for the game"""

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        window.blit(back, (0,0))
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("Gacha Game", largeText)
        TextRect.center = ((window_width/2),(window_height/2))
        window.blit(TextSurf, TextRect)

        button("Please Click Here To Start!",150,450,500,50,green,bright_green, game_menu)

        pygame.display.update()
        clock.tick(15)

def game_menu():
      """menu lol"""
    
      menu = True

      while menu:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        window.blit(back, (0,0))
        pygame.draw.rect(window, red, (0,0, 800, 50) )
        mediumText = pygame.font.SysFont("comicsansms",30)
        TextSurf, TextRect = text_objects("menu yall", mediumText)
        TextRect.center = ((70, 50/2 ))
        window.blit(TextSurf, TextRect)

        button("formation",50,80,700,100,green,bright_green, game_intro)
        button("enhance",50,210,700,100,green,bright_green, game_menu)
        button("summon",50,340,700,100,green,bright_green, game_menu)
        button("fight",50,470,700,100,green,bright_green, game_menu)

        pygame.display.update()
        clock.tick(15)


  

# define classes here
class Character:
  """Generic character class"""
  def __init__(self, name, atk, hp, defense):
    self.name = name
    self.atk = atk
    self.defense = defense
    self.hp = hp

class Player(Character):
  """Class for a player character"""
  def __init__(self, name, atk, hp, defense, rank):
    Character.__init__(self, name, atk, hp, defense)
    self.rank = rank

  #def describe(self):
   # """describe the specified character"""
    #print(f"""
  #{self.name}:
   # hp: {self.hp}
    #atk: {self.atk}
    #def: {self.defense}
    #rank: {self.rank}""")
    #return

class Opponent(Character):
  """Class for opponents"""
  def __init__(self, name, atk, hp, defense):
    Character.__init__(self, name, atk, hp, defense)

  #def describe(self):
     # """describe the specified character"""
     # print(f"""
 # {self.name}:
   # hp: {self.hp}
   # atk: {self.atk}
   # def: {self.defense}""")
     # return

jh = Player("Jihun", 10000, 10000, 100, "SSR")
yh = Player("UKnow", 9900, 9900, 100, "SSR")
cm = Player("Max", 9800, 9800, 100, "SSR")
yk = Player("Brian", 9700, 9700, 100, "SSR")
hy = Player("N", 9600, 9600, 100, "SSR")
js = Player("Inseong", 9000, 9000, 70, "SR")
hj = Player("Heejun", 8900, 8900, 70, "SR")
sh = Player("Seoham", 8800, 8800, 70, "SR")
dg = Player("Donggu", 8700, 8700, 70, "SR")
sg = Player("Sunny", 8600, 8600, 70, "SR")
dw = Player("Dongwoon", 8500, 8500, 70, "SR")
ji = Player("Jae", 8400, 8400, 70, "SR")
wp = Player("Wonpil", 8300, 8300, 70, "SR")
sj = Player("Sungjin", 8200, 8200, 70, "SR")
tw = Player("Leo", 8100, 8100, 70, "SR")
hs = Player("Hyuk", 6500, 6500, 50, "R")
yn = Player("Yoona", 6400, 6400, 50, "R")
ho = Player("Hyoyeon", 6300, 6300, 50, "R")
yr = Player("Yuri", 6200, 6200, 50, "R")
ty = Player("Taeyeon", 6100, 6100, 50, "R")
tf = Player("Tiffany", 6000, 6000, 50, "R")
sy = Player("Sooyoung", 5900, 5900, 50, "R")
so = Player("Seohyun", 5800, 5800, 50, "R")
rv = Player("Ravi", 5700, 5700, 50, "R")
hb = Player("Hongbin", 5600, 5600, 50, "R")

players = [jh, yh, cm, yk, hy, js, hj, sh, dg, sg, dw, ji, wp, sj, tw, hs, yn, ho, yr, ty, tf, sy, so, rv, hb]
pull = random.choice(players)

f1 = Opponent("Fan 1", 2000, 4000, 20)
f2 = Opponent("Fan 2", 2000, 4000, 20)
f3 = Opponent("Fan 3", 2000, 4000, 20 )
m1 = Opponent("Manager 1", 3000, 6000, 30)
m2 = Opponent("Manager 2", 3000, 6000, 30)
m3 = Opponent("Manager 3", 3000, 6000, 30)
jf = Opponent("JellyFish", 5000, 10000, 40)
plt = Opponent("Planetarium", 4500, 9000, 40)
wl = Opponent("Woollim", 4000, 8000, 40)
ss = Opponent("Starship",5500 , 11000, 50)
pd = Opponent("Pledis", 6000, 12000, 50)
fnc = Opponent("FNC", 6500, 13000, 50)
yg = Opponent("YG", 9000, 18000, 60)
sm = Opponent("SM", 10000, 20000, 60)
jyp = Opponent("JYP", 8000, 16000, 60)

run = False

# main loop
while not run:
    # event queue handling
    # this for loop contains anything that should be triggered by an event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True

    # core logic goes here
    game_intro()
