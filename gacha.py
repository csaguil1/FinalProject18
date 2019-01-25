#importing modules
import pygame
import random
import time

#initializing pygame
pygame.init()

#i define everything in the beginning

#setting window_width and window_height as variables so that if I need to change them later on it's more convenient
window_width = 800
window_height = 600

#setting up size of window display
window = pygame.display.set_mode((window_width, window_height))

#sets caption as Gacha Game
pygame.display.set_caption("Gacha Game")

#name of colors set to their rbg colors
black = (0,0,0)
red = (200,0,0)
green = (0,200,0)
white = (255, 255, 255)
gray = (224, 224, 224)
royal_blue = (17, 30, 108)
bright_red = (255,0,0)
bright_green = (0,255,0)
gold = (255, 215, 0)
gold_yellow = (255, 223, 0)
blue = (176, 224, 230)

#pygame time
clock = pygame.time.Clock()

# define classes here
class Character:
    """Generic character class"""
    def __init__(self, name, atk, hp, defense):
        self.name = name
        self.atk = atk
        self.defense = defense
        self.hp = hp

    def fight(self, opponent):
        """make player and opponent fight"""    
    
        #displays who attacks who
        text_box(f"{self.name} attacks {opponent.name}")
        pygame.display.update()
        time.sleep(3)

        #how attack works
        dmg = self.atk - (self.atk/opponent.defense)
        opponent.hp -= dmg

        #displays health
        text_box(f"{opponent.name} is at {opponent.hp} health!")
        pygame.display.update()
        time.sleep(3)
        text_box(f"{self.name} is at {self.hp} health!")
        pygame.display.update()
        time.sleep(3)
            
class Player(Character):
  """Class for a player character"""
  def __init__(self, name, atk, hp, defense, rank):
    Character.__init__(self, name, atk, hp, defense)
    self.rank = rank

  def describe(self):
    """describe the specified character"""
    text_box(f"""{self.name}: hp: {self.hp}, atk: {self.atk}, def: {self.defense}, rank: {self.rank}""")

class Opponent(Character):
    """Class for opponents"""
    def __init__(self, name, atk, hp, defense):
        Character.__init__(self, name, atk, hp, defense)

    def describe(self):
        """describe the specified opponent"""
        text_box(f"""{self.name}: hp: {self.hp}, atk: {self.atk}, def: {self.defense}""")

    def fight(self, you):
        """make player and opponent fight"""    

        #displays who attacks who    
        text_box(f"{self.name} attacks {you.name}")
        pygame.display.update()
        time.sleep(3)

        #how attacks works
        dmg = self.atk - (self.atk/you.defense)
        you.hp -= dmg

        #display health
        text_box(f"{you.name} have {you.hp} health!")
        pygame.display.update()
        time.sleep(3)
        text_box(f"{self.name} is at {self.hp} health!")
        pygame.display.update()
        print(self.hp)
        pygame.display.update()


#creating Players that you can summon in the game
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

#creating Opponents that you will fight in the game
f1 = Opponent("Fan 1", 100, 4000, 20)
f2 = Opponent("Fan 2", 100, 4000, 20)
f3 = Opponent("Fan 3", 100, 4000, 20 )
m1 = Opponent("Manager 1", 200, 6000, 30)
m2 = Opponent("Manager 2", 200, 6000, 30)
m3 = Opponent("Manager 3", 200, 6000, 30)
jf = Opponent("JellyFish", 500, 10000, 40)
plt = Opponent("Planetarium", 500, 9000, 40)
wl = Opponent("Woollim", 500, 8000, 40)
ss = Opponent("Starship",300 , 11000, 50)
pd = Opponent("Pledis", 600, 12000, 50)
fnc = Opponent("FNC", 600, 13000, 50)
yg = Opponent("YG",1000 , 10000, 60)
sm = Opponent("SM", 1000, 20000, 60)
jyp = Opponent("JYP", 900, 16000, 60)

#list of players that you can summon
players = [jh, yh, cm, yk, hy, js, hj, sh, dg, sg, dw, ji, wp, sj, tw, hs, yn, ho, yr, ty, tf, sy, so, rv, hb]

#list of players that have been summoned
players_summoned = []

#list of names of players that have been summoned
players_summoned_display = []

#dictionary for inventory of items you can collect in the game
inventory = {
    'summon stone': 0
}

#list for opponents that can be spawned in level 1
op_1 = [f1, f2, f3]

#list for opponents that can be spawned in level 2
op_2 = [m1, m2, m3]

#list for opponents that can be spawned in level 3
op_3 = [jf, plt, wl]

#list for opponents that can be spawned in level 4
op_4 = [ss, pd, fnc]

#list for opponents that can be spawned in level 5
op_5 = [yg, sm, jyp]

#importing images
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

#all the functions come after all the definitons

def text_objects(text, font, color):
    """displays text"""
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def text_box(text):
    """displays text in a text box similar to those of classic games"""

    #drawing rectangles to make actual textbox
    pygame.draw.rect(window, black, (50, 400, 700, 150))
    pygame.draw.rect(window, white, (55, 405, 690, 140))
    pygame.draw.rect(window, black, (60, 410, 680, 130))

    #displays text centered in textbox
    smallText = pygame.font.SysFont("comicsansms",10)
    TextSurf, TextRect = text_objects(text, smallText, white)
    TextRect.center = (400, 475)
    window.blit(TextSurf, TextRect)

def button(msg,x,y,w,h,ic,ac,action=None):
    """creates buttons that that the user can press and interact with to lead into another action"""
    
    #sets up mouse and mouseclicks
    mouse = pygame.mouse.get_pos()
    mouseclick = pygame.mouse.get_pressed()
    print(mouseclick)

    #if mouse is on button draw rect with after color
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(window, ac,(x,y,w,h))

        #if mouse click on button and there is an action (function) go complete that function
        if mouseclick[0] == 1 and action != None:
            action() 
    
    #else draw rect with initial color        
    else:
        pygame.draw.rect(window, ic,(x,y,w,h))
    
    #displays text in the center of button
    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText, white)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    window.blit(textSurf, textRect)

def game_intro():
    """intro to the game, start menu"""

    intro = True

    #loop for intro, while intro is True this will be shown on screen
    while intro:

        # event queue handling
        # this for loop contains anything that should be triggered by an event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #background
        window.blit(back, (0,0))

        #sets Gacha game as centered title on screen
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("Gacha Game", largeText, white)
        TextRect.center = ((window_width/2),(window_height/2))
        window.blit(TextSurf, TextRect)

        #button that will lead to the game_story function
        button("Please Click Here To Start!",150,450,500,50,green,bright_green, game_story)

        #updates screen
        pygame.display.update()

def game_menu():
      """menu for the whole game, where you can choose what to do"""
    
      menu = True

      #loop for menu, while menu is True this will be shown on screen
      while menu:

        # event queue handling
        # this for loop contains anything that should be triggered by an event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        #background
        window.blit(back, (0,0))

        #top, states that this is the menu
        pygame.draw.rect(window, royal_blue, (0,0, 800, 50) )
        mediumText = pygame.font.SysFont("comicsansms",30)
        TextSurf, TextRect = text_objects("menu yall", mediumText, white)
        TextRect.center = ((70, 50/2 ))
        window.blit(TextSurf, TextRect)

        #buttons that lead to different aspects of the game
        button("formation",50,80,700,100,black,gray, formation)
        button("inventory",50,210,700,100,black,gray, inventory_view)
        button("summon",50,340,700,100,black,gray, summon_menu)
        button("fight",50,470,700,100,black,gray, fight_menu)

        #updates screen
        pygame.display.update()

def game_story(): 
    """function that uses textbox and images to tell the plot of the game"""

    #sets up a variable click that is equal to 0
    click = 0

    story = True

    ##loop for story, while story is True this will be shown on screen
    while story:

        #sets frames per second
        clock.tick(5)

        # event queue handling
        # this for loop contains anything that should be triggered by an event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #sets up key clicks, if key is pressed number of clicks goes up by 1
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            click += 1

        #if click equals a number it will display the screen assigned to that number and update screen
        #general format
        #background
        #any possible extra images
        #text box saying story
        #update screen
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

        #instead of a screen when click equals 5 it leads to the game tutorial function
        elif click == 5:
            game_tutorial()

def game_tutorial():
    """function that uses textbox and images that teach the user how to play the game"""

    #sets up a variable click that is equal to 0
    click = 0

    tutorial = True

    #loop for tutorial, while tutorial is True this will be shown on screen
    while tutorial:

        #sets frames per second
        clock.tick(5)

        # event queue handling
        # this for loop contains anything that should be triggered by an event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #sets up key clicks, if key is pressed number of clicks goes up by 1
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            click += 1

        #if click equals a number it will display the screen assigned to that number and update screen
        #general format
        #background
        #any possible extra images
        #text box saying tutorial
        #update screen
        if click == 0:
            window.blit(back, (0,0))
            text_box("First, let's find out how to play the game.")
            pygame.display.update()

        elif click == 1:
            window.blit(back, (0,0))
            text_box("Press the formation button on the menu to choose your fighter.")
            pygame.display.update()

        elif click == 2:
            window.blit(back, (0,0))
            text_box("Press the inventory button on the menu to view your inventory.")
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
            inventory["summon stone"] = 10
            print(inventory)
            pygame.display.update()

        elif click == 6:
            window.blit(back, (0,0))
            text_box("Press the summon button 5 times to get 5 starter idols.")
            pygame.display.update()

        #instead of a screen when click equals 5 it leads to the summon menu function
        elif click == 7:
            summon_menu()

def summon():
    """allows user to summon a character if they have summon stones and displays on screen"""
    
    #did if/else statement out of while loop so that if statement would only go once

    #if user has 2 summon stones or more
    if inventory["summon stone"] >= 2:

        #computers chooses a random player for players list
        pull = random.choice(players)

        #that players is then added to the empty players_summoned list
        players_summoned.append(pull)

        players_summoned_display.append(f"{pull.name}")

        #2 summon stones are removed from your inventory
        inventory["summon stone"] -= 2

        summon = True

        #loop for summon, while summon is True this will be shown on screen
        while summon == True:
            
            # event queue handling
            # this for loop contains anything that should be triggered by an event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            #background
            window.blit(back, (0,0))

            #calls function that describes player pulled
            pull.describe()

            #button to go back to the menu
            button("go back to menu", 50, 50, 200, 50, black, gray, game_menu)

            # button to go back to summon menu
            button("go back to summon", 550, 50, 200, 50, black, gray, summon_menu)

            #update screen
            pygame.display.update()
    
    #else displays this on screen
    else:

        summon = True

        #loop for summon, while summon is True this will be shown on screen
        while summon == True:
            # event queue handling
            # this for loop contains anything that should be triggered by an event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            #background
            window.blit(back, (0,0))

            #displays text explaining they don't have enough summon stones
            text_box("I'm sorry, you don't have enough summon stones to complete this action.")

            #button to go back to the menu
            button("go back to menu", 50, 50, 200, 50, black, gray, game_menu)

            #button to go back to the summon menu
            button("go back to summon", 550, 50, 200, 50, black, gray, summon_menu)

            #updates screen
            pygame.display.update()

def formation():
    """explains how to choose a fighter and displays players summoned"""
    
    #sets up a variable click that is equal to 0
    click = 0

    formation = True

    #loop for formation, while formation is True this will be shown on screen
    while formation:

        #sets up frames per second
        clock.tick(5)

        # event queue handling
        # this for loop contains anything that should be triggered by an event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #sets up key clicks, if key is pressed number of clicks goes up by 1
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            click += 1

        #if click equals a number it will display the screen assigned to that number and update screen
        #general format
        #background
        #any possible extra images
        #text box explaining formation
        #button that leads back to menu
        #update screen
        if click == 0:
            window.blit(back, (0,0))
            text_box("Select your character by pressing the number that corresponds with their place in the list.")
            button("go back to menu", 50, 50, 200, 50, black, gray, game_menu)
            pygame.display.update()
        elif click == 1:
            window.blit(back, (0,0))
            text_box("List of characters will first be displayed, then when it says to choose please press your number.")
            button("go back to menu", 50, 50, 200, 50, black, gray, game_menu)
            pygame.display.update()
        elif click == 2:
            window.blit(back, (0,0))
            text_box(", ".join(players_summoned_display))
            button("go back to menu", 50, 50, 200, 50, black, gray, game_menu)
            pygame.display.update()

        #instead of a screen when click equals 5 it leads to the choose_fighter function 
        elif click == 3:
            choose_fighter()

def choose_fighter():
    """choose fighter to battle opponents"""

    #global fighter variable
    global fighter

    choose_fighter = True

    #loop for choosing fighter, while choosing fighter is True this will be shown on screen
    while choose_fighter:
        
        # event queue handling
        # this for loop contains anything that should be triggered by an event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #background
        window.blit(back, (0,0))
        text_box("Now, please press a number to choose your fighter.")

        #uodates screen
        pygame.display.update()
        
        #sets up key clicks, if user clicks a number 1-9 it displays one of these screens
        #general format
        #loop
        #background
        #defines fighter
        #text box showing what the user chose
        #updates screen
        key = pygame.key.get_pressed()
        if key[pygame.K_1]:

            choose_fighter = True

            #loop for choosing fighter, while choosing fighter is True this will be shown on screen
            while choose_fighter:
                
                # event queue handling
                # this for loop contains anything that should be triggered by an event
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                window.blit(back, (0,0))
                fighter = players_summoned[0]
                text_box(f"you chose {str(players_summoned_display[0])}")
                button("go back to menu", 50, 50, 200, 50, black, gray, game_menu)
                pygame.display.update()

        if key[pygame.K_2]:
            choose_fighter = True

            #loop for choosing fighter, while choosing fighter is True this will be shown on screen
            while choose_fighter:
                
                # event queue handling
                # this for loop contains anything that should be triggered by an event
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                window.blit(back, (0,0))
                fighter = players_summoned[1]
                text_box(f"you chose {str(players_summoned_display[1])}")
                button("go back to menu", 50, 50, 200, 50, black, gray, game_menu)
                pygame.display.update()

        if key[pygame.K_3]:
            choose_fighter = True

            #loop for choosing fighter, while choosing fighter is True this will be shown on screen
            while choose_fighter:
                
                # event queue handling
                # this for loop contains anything that should be triggered by an event
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                window.blit(back, (0,0))
                fighter = players_summoned[2]
                text_box(f"you chose {str(players_summoned_display[2])}")
                button("go back to menu", 50, 50, 200, 50, black, gray, game_menu)
                pygame.display.update()

        if key[pygame.K_4]:
            choose_fighter = True

            #loop for choosing fighter, while choosing fighter is True this will be shown on screen
            while choose_fighter:
                
                # event queue handling
                # this for loop contains anything that should be triggered by an event
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                window.blit(back, (0,0))
                fighter = players_summoned[3]
                text_box(f"you chose {str(players_summoned_display[3])}")
                button("go back to menu", 50, 50, 200, 50, black, gray, game_menu)
                pygame.display.update()

        if key[pygame.K_5]:
            choose_fighter = True

            #loop for choosing fighter, while choosing fighter is True this will be shown on screen
            while choose_fighter:
                
                # event queue handling
                # this for loop contains anything that should be triggered by an event
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                window.blit(back, (0,0))
                fighter = players_summoned[4]
                text_box(f"you chose {str(players_summoned_display[4])}")
                button("go back to menu", 50, 50, 200, 50, black, gray, game_menu)
                pygame.display.update()

        if key[pygame.K_6]:
            choose_fighter = True

            #loop for choosing fighter, while choosing fighter is True this will be shown on screen
            while choose_fighter:
                
                # event queue handling
                # this for loop contains anything that should be triggered by an event
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                window.blit(back, (0,0))
                fighter = players_summoned[5]
                text_box(f"you chose {str(players_summoned_display[5])}")
                button("go back to menu", 50, 50, 200, 50, black, gray, game_menu)
                pygame.display.update()

        if key[pygame.K_7]:
            choose_fighter = True

            #loop for choosing fighter, while choosing fighter is True this will be shown on screen
            while choose_fighter:
                
                # event queue handling
                # this for loop contains anything that should be triggered by an event
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                window.blit(back, (0,0))
                fighter = players_summoned[6]
                text_box(f"you chose {str(players_summoned_display[6])}")
                button("go back to menu", 50, 50, 200, 50, black, gray, game_menu)
                pygame.display.update()

        if key[pygame.K_8]:
            choose_fighter = True

            #loop for choosing fighter, while choosing fighter is True this will be shown on screen
            while choose_fighter:
                
                # event queue handling
                # this for loop contains anything that should be triggered by an event
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                window.blit(back, (0,0))
                fighter = players_summoned[7]
                text_box(f"you chose {str(players_summoned_display[7])}")
                button("go back to menu", 50, 50, 200, 50, black, gray, game_menu)
                pygame.display.update()

        if key[pygame.K_9]:
            choose_fighter = True

            #loop for choosing fighter, while choosing fighter is True this will be shown on screen
            while choose_fighter:
                
                # event queue handling
                # this for loop contains anything that should be triggered by an event
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                window.blit(back, (0,0))
                fighter = players_summoned[9]
                text_box(f"you chose {str(players_summoned_display[9])}")
                button("go back to menu", 50, 50, 200, 50, black, gray, game_menu)
                pygame.display.update()

def inventory_view():
    """allows user to view their inventory or how many summon stones they have"""

    inventory_view = True

    #loop for inventory, while inventory is True this will be shown on screen
    while inventory_view:
        
        # event queue handling
        # this for loop contains anything that should be triggered by an event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #background
        window.blit(back, (0,0))

        #textbox displays inventory dectionary as a string
        text_box(str(inventory))

        #button that goes back to menu
        button("go back to menu", 50, 50, 200, 50, black, gray, game_menu)

        #update screen
        pygame.display.update()

def fight_menu():
    """allows user to choose which level they want to play"""

    fight_menu = True

    #loop for fight menu, while fight menu is True this will be shown on screen
    while fight_menu:

        # event queue handling
        # this for loop contains anything that should be triggered by an event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #background
        window.blit(back, (0,0))

        #buttons that will go to certain levels
        button("level 1", 50, 122.5, 700, 75, black, gray, level_1)
        button("level 2", 50, 217.5, 700, 75, black, gray, level_2)
        button("level 3", 50, 312.5, 700, 75, black, gray, level_3)
        button("level 4", 50, 407.5, 700, 75, black, gray, level_4)
        button("level 5", 50, 502.5, 700, 75, black, gray, level_5)

        #buttons that goes back to menu
        button("go back to menu", 50, 50, 200, 50, black, gray, game_menu)

        #updates screen
        pygame.display.update()

def player_image():
    """display fighter image in fight"""

    #global variable fighter
    global fighter

    #general
    #if fighter is this player, then display that player on screen
    #update screen
    if fighter == jh:
        window.blit(kimjihun, (80, 230))
        pygame.display.update()
    elif fighter == yh:
        window.blit(yunho, (80, 230))
        pygame.display.update()
    elif fighter == cm:
        window.blit(changmin, (80, 230))
        pygame.display.update()
    elif fighter == yk:
        window.blit(brian, (80, 230))
        pygame.display.update()
    elif fighter == hy:
        window.blit(hakyeon, (80, 230))
        pygame.display.update()
    elif fighter == js:
        window.blit(inseong, (80, 230))
        pygame.display.update()
    elif fighter == hj:
        window.blit(heejun, (80, 230))
        pygame.display.update()
    elif fighter == sh:
        window.blit(seoham, (80, 230))
        pygame.display.update()
    elif fighter == dg:
        window.blit(donggu, (80, 230))
        pygame.display.update()
    elif fighter == sg:
        window.blit(sunny, (80, 230))
        pygame.display.update()
    elif fighter == dw:
        window.blit(dongwoon, (80, 230))
        pygame.display.update()
    elif fighter == ji:
        window.blit(jae, (80, 230))
        pygame.display.update()
    elif fighter == wp:
        window.blit(wonpil, (80, 230))
        pygame.display.update()
    elif fighter == sj:
        window.blit(sungjin, (80, 230))
        pygame.display.update()
    elif fighter == tw:
        window.blit(leo, (80, 230))
        pygame.display.update()
    elif fighter == hs:
        window.blit(hyuk, (80, 230))
        pygame.display.update()
    elif fighter == yn:
        window.blit(yoona, (80, 230))
        pygame.display.update()
    elif fighter == ho:
        window.blit(hyoyeon, (80, 230))
        pygame.display.update()
    elif fighter == yr:
        window.blit(yuri, (80, 230))
        pygame.display.update()
    elif fighter == ty:
        window.blit(taeyeon, (80, 230))
        pygame.display.update()
    elif fighter == tf:
        window.blit(tiffany, (80, 230))
        pygame.display.update()
    elif fighter == sy:
        window.blit(soyoung, (80, 230))
        pygame.display.update()
    elif fighter == so:
        window.blit(seohyun, (80, 230))
        pygame.display.update()
    elif fighter == rv:
        window.blit(ravi, (80, 230))
        pygame.display.update()
    elif fighter == hb:
        window.blit(hongbin, (80, 230))
        pygame.display.update()

def opponent_image():
    """display opponent image on screen"""

    #general
    #if opponent is this opponent, then display that opponent on screen
    #update screen
    if opponent == f1:
        window.blit(fan1, (600, 230))
        pygame.display.update()
    elif opponent == f2:
        window.blit(fan2, (600, 230))
        pygame.display.update()
    elif opponent == f3:
        window.blit(fan3, (600, 230))
        pygame.display.update()
    elif opponent == m1:
        window.blit(manager1, (600, 230))
        pygame.display.update()
    elif opponent == m2:
        window.blit(manager2, (600, 230))
        pygame.display.update()
    elif opponent == m3:
        window.blit(manager3, (600, 230))
        pygame.display.update()
    elif opponent == jf:
        window.blit(jellyfish, (600, 230))
        pygame.display.update()
    elif opponent == plt:
        window.blit(planet, (600, 230))
        pygame.display.update()
    elif opponent == wl:
        window.blit(woollim, (600, 230))
        pygame.display.update()
    elif opponent == ss:
        window.blit(starship, (600, 230))
        pygame.display.update()
    elif opponent == pd:
        window.blit(pledis, (600, 230))
        pygame.display.update()
    elif opponent == fnc:
        window.blit(fncent, (600, 230))
        pygame.display.update()
    elif opponent == yg:
        window.blit(ygent, (600, 230))
        pygame.display.update()
    elif opponent == sm:
        window.blit(sment, (600, 230))
        pygame.display.update()
    elif opponent == jyp:
        window.blit(jypent, (600, 230))
        pygame.display.update()

def level_1():
    """user plays level 1 of the game"""

    #there are other functions like this: level_2, level_3, level_4, and level_5, please refer to this function for comments

    #global variable opponents and fighter
    global opponent
    global fighter 

    level_1 = True

    #opponent is randomly chosen from list
    opponent = random.choice(op_1)

    #loop for fight menu, while fight menu is True this will be shown on screen
    while level_1:
        # event queue handling
        # this for loop contains anything that should be triggered by an event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #background
        window.blit(back, (0,0))

        #updates screen
        pygame.display.update()

        #functions display players
        player_image()
        opponent_image()

        #fighting commence
        opponent.fight(fighter)
        fighter.fight(opponent)

        if opponent.hp <= 0:

            #displays they won
            text_box("You Win!")

            #updates screen
            pygame.display.update()
            time.sleep(2)

            #breaks loop
            break

        if fighter.hp <= 0:

            #displays you lost
            text_box("You lose!") #rip

            #updates screen
            pygame.display.update()
            time.sleep(2)

            #break from loop
            break

def level_2():
    """user plays level 2 of the game"""

    #please refer to level_1 for comments

    global opponent
    global fighter 
    level_2 = True
    opponent = random.choice(op_2)

    #loop for fight menu, while fight menu is True this will be shown on screen
    while level_2:
        # event queue handling
        # this for loop contains anything that should be triggered by an event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        window.blit(back, (0,0))
        pygame.display.update()
        player_image()
        opponent_image()
        opponent.fight(fighter)
        fighter.fight(opponent)
        if opponent.hp <= 0:
            text_box("You Win!")
            pygame.display.update()
            time.sleep(2)
            break
        if fighter.hp <= 0:
            text_box("You lose!") #rip
            pygame.display.update()
            time.sleep(2)
            break

def level_3():
    """user plays level 3 of the game"""

    #please refer to level_1 for comments

    global opponent
    global fighter 
    level_3 = True
    opponent = random.choice(op_3)

    #loop for fight menu, while fight menu is True this will be shown on screen
    while level_3:
        # event queue handling
        # this for loop contains anything that should be triggered by an event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        window.blit(back, (0,0))
        pygame.display.update()
        player_image()
        opponent_image()
        opponent.fight(fighter)
        fighter.fight(opponent)
        if opponent.hp <= 0:
            text_box("You Win!")
            pygame.display.update()
            time.sleep(2)
            break
        if fighter.hp <= 0:
            text_box("You lose!") #rip
            pygame.display.update()
            time.sleep(2)
            break

def level_4():
    """user plays level 4 of the game"""

    #please refer to level_1 for comments
    
    global opponent
    global fighter 
    level_4 = True
    opponent = random.choice(op_4)

    #loop for fight menu, while fight menu is True this will be shown on screen
    while level_4:
        # event queue handling
        # this for loop contains anything that should be triggered by an event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        window.blit(back, (0,0))
        pygame.display.update()
        player_image()
        opponent_image()
        opponent.fight(fighter)
        fighter.fight(opponent)
        if opponent.hp <= 0:
            text_box("You Win!")
            pygame.display.update()
            time.sleep(2)
            break
        if fighter.hp <= 0:
            text_box("You lose!") #rip
            pygame.display.update()
            time.sleep(2)
            break

def level_5():
    """user plays level 5 of the game"""

    #please refer to level_1 for comments

    global opponent
    global fighter 
    level_5 = True
    opponent = random.choice(op_5)

    #loop for fight menu, while fight menu is True this will be shown on screen
    while level_5:
        # event queue handling
        # this for loop contains anything that should be triggered by an event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        window.blit(back, (0,0))
        pygame.display.update()
        player_image()
        opponent_image()
        opponent.fight(fighter)
        fighter.fight(opponent)
        if opponent.hp <= 0:
            text_box("You Win!")
            time.sleep(2)
            pygame.display.update()
            break
        if fighter.hp <= 0:
            text_box("You lose!") #rip
            pygame.display.update()
            time.sleep(2)
            break

def summon_menu():
    """menu to summon characters"""

    summon_menu = True

    #loop for summon menu, while summon menu is True this will be shown on screen
    while summon_menu:
        
        # event queue handling
        # this for loop contains anything that should be triggered by an event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #background
        window.blit(back, (0,0))

        #button to go to summon and get characters
        button("summon", 50, 450, 700, 50, black, gray, summon)

        #button to go back to menu
        button("go back to menu", 50, 50, 150, 50, black, gray, game_menu)

        #updates screen
        pygame.display.update()

run = False

# main loop for the whole game
while not run:

    #sets up frames per second
    clock.tick(5)

    # event queue handling
    # this for loop contains anything that should be triggered by an event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True
    
    #function that shows intro of game/start menu
    game_intro()
