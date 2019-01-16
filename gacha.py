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
white = (255, 255, 255)
bright_red = (255,0,0)
bright_green = (0,255,0)

clock = pygame.time.Clock()

back = pygame.image.load("background.png")
back2 = pygame.image.load("background 2.png")
kimjihun = pygame.image.load("kimjh.png")
brian = pygame.image.load("briankang.png")
hakyeon = pygame.image.load("choihakyeon.png")
donggu = pygame.image.load("donggu.png")
dongwoon = pygame.image.load("dongwoon.png")
fan1 = pygame.image.load("fan1.png")
fan2 = pygame.image.load("fan2.png")
fan3 = pygame.image.load("fan3.png")
fncent = pygame.image.load("fnc.png")
hongbin = pygame.image.load("hongbin.png")
hyoyeon = pygame.image.load("hyoyeon.png")
hyuk = pygame.image.load("hyuk.png")
jae = pygame.image.load("jae.png")
jellyfish = pygame.image.load("jelly.png")
inseong = pygame.image.load("jeonginseong.png")
yunho = pygame.image.load("jeongyunho.png")
jypent = pygame.image.load("jyp.png")
leo = pygame.image.load("leo.png")
manager1 = pygame.image.load("manager1.png")
manager2 = pygame.image.load("manager2.png")
manager3 = pygame.image.load("manager3.png")
heejun = pygame.image.load("ohheejun.png")
pledis = pygame.image.load("pld.png")
planet = pygame.image.load("plt.png")
ravi = pygame.image.load("ravi.png")
seoham = pygame.image.load("seoham.png")
seohyun = pygame.image.load("seohyun.png")
changmin = pygame.image.load("shimchangmin.png")
sment = pygame.image.load("sm.png")
sooyoung = pygame.image.load("sooyoung.png")
starship = pygame.image.load("star.png")
sungjin = pygame.image.load("sungjin.png")
sunny = pygame.image.load("sunny.png")
taeyeon = pygame.image.load("taeyeon.png")
tiffany = pygame.image.load("tiffany.png")
wonpil = pygame.image.load("wonpil.png")
woollim = pygame.image.load("woollim.png")
ygent = pygame.image.load("yg.png")
yoona = pygame.image.load("yoona.png")
yuri = pygame.image.load("yuri.png")

def text_objects(text, font, color):
    """text"""
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def text_box(text):
    """text box"""
    pygame.draw.rect(window, black, (50, 400, 700, 150))
    pygame.draw.rect(window, white, (55, 405, 690, 140))
    pygame.draw.rect(window, black, (60, 410, 680, 130))
    smallText = pygame.font.SysFont("comicsansms",10)
    TextSurf, TextRect = text_objects(text, smallText, white)
    TextRect.center = (400, 475)
    window.blit(TextSurf, TextRect)

def button(msg,x,y,w,h,ic,ac,action=None):
    """buttons"""
    mouse = pygame.mouse.get_pos()
    mouseclick = pygame.mouse.get_pressed()
    print(mouseclick)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(window, ac,(x,y,w,h))

        if mouseclick[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(window, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText, white)
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
        TextSurf, TextRect = text_objects("Gacha Game", largeText, white)
        TextRect.center = ((window_width/2),(window_height/2))
        window.blit(TextSurf, TextRect)

        button("Please Click Here To Start!",150,450,500,50,green,bright_green, game_story)

        pygame.display.update()

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
        TextSurf, TextRect = text_objects("menu yall", mediumText, white)
        TextRect.center = ((70, 50/2 ))
        window.blit(TextSurf, TextRect)

        button("formation",50,80,700,100,green,bright_green, formation)
        button("enhance",50,210,700,100,green,bright_green, enhance)
        button("summon",50,340,700,100,green,bright_green, summon)
        button("fight",50,470,700,100,green,bright_green, fight_menu)

        pygame.display.update()

def game_story(): 
    """i hate this"""

    click = 0

    story = True

    while story:
        clock.tick(5)
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            click += 1

        if click == 0:
            window.blit(back, (0,0))
            text_box("PRESS SPACE TO GO TO THE NEXT SCREEN")
            pygame.display.update()
        elif click == 1:
            window.blit(back, (0,0))
            text_box("It is a nice day in Seoul, Korea... ")
            pygame.display.update()
        elif click == 2:
            window.blit(back, (0,0))
            text_box("The idols are tired from working and finally have a rest day! They are relaxing peacefully...")
            pygame.display.update()
        elif click == 3:
            window.blit(back, (0,0))
            text_box("That is until their fans, managers, and companies demand that they work!")
            pygame.display.update()
        elif click == 4:
            window.blit(back, (0,0))
            text_box("THE IDOLS GET MAD! NOW THEY MUST FIGHT EVERYONE IN ORDER TO GET THEIR REST")
            pygame.display.update()
        elif click == 5:
            game_tutorial()

def game_tutorial():
    """how to play the game kiddo"""
    
    click = 0

    tutorial = True

    while tutorial:
        clock.tick(5)
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            click += 1

        if click == 0:
            window.blit(back, (0,0))
            text_box("First, let's find out how to play the game.")
            pygame.display.update()
        elif click == 1:
            window.blit(back, (0,0))
            text_box("Press the formation button on the menu to set up your team.")
            pygame.display.update()
        elif click == 2:
            window.blit(back, (0,0))
            text_box("Press the enhance button on the menu to upgrade your idols.")
            pygame.display.update()
        elif click == 3:
            window.blit(back, (0,0))
            text_box("Press the summon button to get idols.")
            pygame.display.update()
        elif click == 4:
            window.blit(back, (0,0))
            text_box("Press the fight button to battle enemies and win your rest.")
            pygame.display.update()
        elif click == 5:
            window.blit(back, (0,0))
            text_box("First of all, you will get 10 summon stones to summon idols.")
            pygame.display.update()
        elif click == 6:
            window.blit(back, (0,0))
            text_box("Press the multi summon button to get 5 starter idols.")
            pygame.display.update()
        elif click == 7:
            summon()

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

  def describe(self):
    """describe the specified character"""
    text_box(f"""
{self.name}:
    hp: {self.hp}
    atk: {self.atk}
    def: {self.defense}
    rank: {self.rank}""")
    

class Opponent(Character):
  """Class for opponents"""
  def __init__(self, name, atk, hp, defense):
    Character.__init__(self, name, atk, hp, defense)

  def describe(self):
    """describe the specified character"""
    text_box(f"""
{self.name}:
    hp: {self.hp}
    atk: {self.atk}
    def: {self.defense}""")

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

inventory = {
    'summon stone': 0,
    'silver': 0,
    'copper': 0,
    'armor': 0,
    'bow': 0,
    'arrow': 0,
    'backpack': 0,
    'apple': 0
}

players_summoned = {
    jh: 0, 
    yh: 0, 
    cm: 0, 
    yk: 0, 
    hy: 0, 
    js: 0, 
    hj: 0, 
    sh: 0, 
    dg: 0, 
    sg: 0, 
    dw: 0, 
    ji: 0, 
    wp: 0, 
    sj: 0, 
    tw: 0, 
    hs: 0, 
    yn: 0, 
    ho: 0, 
    yr: 0, 
    ty: 0, 
    tf: 0, 
    sy: 0, 
    so: 0, 
    rv: 0, 
    hb: 0
}

def pull():
    players = [jh, yh, cm, yk, hy, js, hj, sh, dg, sg, dw, ji, wp, sj, tw, hs, yn, ho, yr, ty, tf, sy, so, rv, hb]
    pull = random.choice(players)
    window.blit(back, (0,0))
    pull.describe()
    pygame.display.update()

def formation():
    """im not sure yet how to do this"""

def enhance():
    """oof am i even going to do this"""

def fight_menu():
    """yah yeet"""

def fight():
    """eyeyeyeyeyeyeyeyeeyye"""

def summon():
    """summon the demon"""

    pull()

run = False

# main loop
while not run:
    clock.tick(5)
    # event queue handling
    # this for loop contains anything that should be triggered by an event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True
   

    # core logic goes here
    game_intro()
