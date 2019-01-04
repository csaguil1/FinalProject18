import pygame
import random
import time

pygame.init()

window_width = 800
window_height = 500

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Gacha Game")

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
      print(f"""
  {self.name}:
    hp: {self.hp}
    atk: {self.atk}
    def: {self.defense}
    rank: {self.rank}""")
      return

class Opponent(Character):
  """Class for opponents"""
  def __init__(self, name, atk, hp, defense):
    Character.__init__(self, name, atk, hp, defense)

  def describe(self):
      """describe the specified character"""
      print(f"""
  {self.name}:
    hp: {self.hp}
    atk: {self.atk}
    def: {self.defense}""")
      return

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
wl = Opponent("Woolim", 4000, 8000, 40)
ss = Opponent("Starship",5500 , 11000, 50)
pd = Opponent("Pledis", 6000, 12000, 50)
fnc = Opponent("FNC", 6500, 13000, 50)
yg = Opponent("YG", 9000, 18000, 60)
sm = Opponent("SM", 10000, 20000, 60)
jyp = Opponent("JYP", 8000, 16000, 60)

clock = pygame.time.Clock()

#back = pygame.image.load("background.jpg")

run = False

# main loop
while not run:
    # event queue handling
    # this for loop contains anything that should be triggered by an event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True

    # core logic goes here

    #window.blit(back, (0,0))
    #pygame.display.update()