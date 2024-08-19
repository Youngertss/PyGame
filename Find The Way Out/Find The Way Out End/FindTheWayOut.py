import pygame 
from pygame import * 
from random import randint
import time as my_time
import os,sys
from pygame.locals import * 

#----SETTING_GAME----
#player
player_speed = 7
player_hp=100

player_size_width, player_size_height = 50,70
FPS=80
distance=75 

#window
pygame.init()
display.set_caption('Find The Way Out')
win_width, win_height = 1200 , 700
window = display.set_mode((win_width, win_height)) 

#COMMON
os.system('cls')
clock = time.Clock()

dictionary_items={'key_blue':False,'key_dark_blue':False,'key_green':False,'key_purple':False,'key_red':False,'key_yellow':False}


#----IMG----
#player-stop
img_player_stop=transform.scale(image.load("IMG\player\img_player_down_2.png"), (player_size_width, player_size_height))

#player-up
img_player_up_1=transform.scale(image.load("IMG\player\img_player_up_1.png"), (player_size_width, player_size_height))
img_player_up_2=transform.scale(image.load("IMG\player\img_player_up_2.png"), (player_size_width, player_size_height))
img_player_up_3=transform.scale(image.load("IMG\player\img_player_up_3.png"), (player_size_width, player_size_height))
img_list_player_up=[img_player_up_1,img_player_up_2,img_player_up_1,img_player_up_3]

#player-down
img_player_down_1=transform.scale(image.load("IMG\player\img_player_down_1.png"), (player_size_width, player_size_height))
img_player_down_2=transform.scale(image.load("IMG\player\img_player_down_2.png"), (player_size_width, player_size_height))
img_player_down_3=transform.scale(image.load("IMG\player\img_player_down_3.png"), (player_size_width, player_size_height))
img_list_player_down=[img_player_down_1,img_player_down_2,img_player_down_1,img_player_down_3]

#player-left
img_player_left_1=transform.scale(image.load("IMG\player\img_player_left_1.png"), (player_size_width, player_size_height))
img_player_left_2=transform.scale(image.load("IMG\player\img_player_left_2.png"), (player_size_width, player_size_height))
img_list_player_left=[img_player_left_1,img_player_left_2,img_player_left_1,img_player_left_2]

#player-right
img_player_right_1=transform.scale(image.load("IMG\player\img_player_right_1.png"), (player_size_width, player_size_height))
img_player_right_2=transform.scale(image.load("IMG\player\img_player_right_2.png"), (player_size_width, player_size_height))
img_list_player_right=[img_player_right_1,img_player_right_2,img_player_right_1,img_player_right_2]

#common
img_dark_background="IMG\img_dark_background.png" #dark_background/illusion of light
img_backgraund= "IMG\ground_normal.jpg"

img_backgraund3=transform.scale(image.load("IMG/backgraund_dark.png"), (win_width, win_height))
img_backgraund2=transform.scale(image.load("IMG/backgraund_dark_hard.png"), (win_width, win_height))

text_question1 = ("IMG\question.png")


#decor 
bed_img, bed2_img, bed3_img, bed4_img = "IMG/bed.png", "IMG/bed2.png", "IMG/bed3.png", "IMG/bed4.png"
carpet_img = "IMG/carpet.png"
book_img1, book_img2 = "IMG/bookshelf1.png", "IMG/bookshelf2.png"
round_tbl_img = "IMG/round_table.png"
tbl_img = "IMG/table.png"
book_img3, book_img4 = "IMG/bookshelf3.png","IMG/bookshelf4.png"
book_img5, book_img6 = "IMG/bookshelf5.png", "IMG/bookshelf6.png"

text_start = "IMG/text_start.png"

#----SOUND----
mixer.init()


mixer.music.load('SOUNDS/sTest-sound.mp3')
mixer.music.set_volume(0.2)
mixer.music.play()

#----FONT----
font = pygame.font.Font('font.ttf', 50)




#----CLASS----
class Player(sprite.Sprite):#class Player and dark_background/illusion of light
    def __init__(self, player_x, player_y):
        sprite.Sprite.__init__(self)

        #player
        self.img_player_now=img_player_stop

        self.player_speed = player_speed

        self.rect = img_player_stop.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.img_number=0
        #dark_background/illusion of light
        self.img_dark_background=transform.scale(image.load(img_dark_background), (win_width*2, win_height*2))

        self.rect_d_b = self.img_dark_background.get_rect()

    def update(self):    
        global location
        if location != 'menu':
            global values_up, values_down, values_right, values_left
            
            if keys[K_s] and self.rect.y < win_height - player_size_height and values_down == True or keys[K_DOWN] and self.rect.y < win_height -player_size_height:
                self.rect.y += player_speed
                self.img_player_now=img_list_player_down[self.img_number]
                self.img_number+=1

            if self.img_number>3:
                self.img_number=0   

            if keys[K_w] and self.rect.y > 5 and values_up == True or keys[K_UP] and self.rect.y > 5:
                self.rect.y -= player_speed
                self.img_player_now=img_list_player_up[self.img_number]
                self.img_number+=1

            if self.img_number>3:
                self.img_number=0

            if keys[K_a] and self.rect.x > 5 and values_left == True or keys[K_LEFT] and self.rect.x > 5:
                self.rect.x -= player_speed
                self.img_player_now=img_list_player_right[self.img_number]
                self.img_number+=1

            if self.img_number>3:
                self.img_number=0

            if keys[K_d] and self.rect.x < win_width - player_size_width and values_right == True or keys[K_RIGHT] and self.rect.x < win_width - player_size_width:
                self.rect.x += player_speed
                self.img_player_now=img_list_player_left[self.img_number]
                self.img_number+=1

            if self.img_number>3:
                self.img_number=0

            if keys[K_d]==keys[K_a]==keys[K_w]==keys[K_s]:
                self.img_player_now=img_player_stop

        
        window.blit(self.img_player_now, (self.rect.x, self.rect.y))
        window.blit(self.img_dark_background, (self.rect.x-win_width+(player_size_width/2), self.rect.y-win_height+(player_size_height/2)))

class Wall(sprite.Sprite):
    def __init__(self, wall_x,wall_y,size_width,size_height):
        sprite.Sprite.__init__(self)

        self.size_width=size_width
        self.size_height=size_height

        self.image=Surface((self.size_width,self.size_height))
        self.image.fill((0, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

class Door():
    def __init__(self, door_x, door_y, door_size_width, door_size_height,tp_x,tp_y,tp_location,color,item = None):
        sprite.Sprite.__init__(self)
        self.size_width = door_size_width
        self.size_height = door_size_height

        self.item=item

        self.tp_x=tp_x
        self.tp_y=tp_y
        self.tp_location=tp_location

        self.image=Surface((self.size_width,self.size_height))
        self.image.fill((color))

        self.rect = self.image.get_rect()
        self.rect.x = door_x
        self.rect.y = door_y
    def update(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

    def teleportation(self):
        if dictionary_items[self.item] or self.item == None:
            global location
            player_hero.rect.x=self.tp_x
            player_hero.rect.y=self.tp_y
            location=self.tp_location 

class Decor(sprite.Sprite):
    def __init__(self, x, y, size_width, size_height, decor_image):
        sprite.Sprite.__init__(self)
        self.size_width = size_width
        self.size_height = size_height

        self.image = transform.scale(image.load(decor_image), (size_width, size_height))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Note(sprite.Sprite):
    def __init__(self,object_x,object_y,object_size_width,object_size_height,object_img,text):
        self.size_width=object_size_width
        self.size_height=object_size_height
        
        self.image=transform.scale(image.load(object_img), (object_size_width, object_size_height))
        self.rect=self.image.get_rect()
        self.rect.x=object_x
        self.rect.y=object_y

        self.text=text

        self.image2=transform.scale(image.load(object_img), (self.size_width*10, self.size_height*10))
        self.rect=self.image.get_rect()
        self.rect.x=object_x
        self.rect.y=object_y

        
    def update(self):
        global keys
        window.blit(self.image, (self.rect.x, self.rect.y))
    
        if keys[K_e]==True and self.rect.x-distance<player_hero.rect.x+player_size_width/2 <self.rect.x+self.size_width+distance and self.rect.y-distance<player_hero.rect.y+player_size_height/2<self.rect.y+self.size_height+distance:
            while True:
                window.blit(img_backgraund2, (0, 0))
                window.blit(self.image2, (win_width/2-self.size_width*5, win_height/2-self.size_height*5))
                window.blit((font.render(self.text, True, (255, 255, 255))), (100,500))
                for e in event.get():
                    if e.type==QUIT:
                        exit()
                keys = key.get_pressed()
                display.update()
                if keys[K_ESCAPE]:
                    break

class Interactive_object():
    def __init__(self,object_x,object_y,object_size_width,object_size_height,object_img,id,answer,object_img2):
        self.size_width=object_size_width
        self.size_height=object_size_height
        self.id = id 
        self.answer=answer
        self.image=transform.scale(image.load(object_img), (object_size_width, object_size_height))
        self.image1=transform.scale(image.load(object_img), (object_size_width*5, object_size_height*5))
        self.rect=self.image.get_rect()
        self.rect.x=object_x
        self.rect.y=object_y
        self.image2=transform.scale(image.load(object_img2), (self.size_width*5, self.size_height*5))
        self.rect=self.image.get_rect()
        self.rect.x=object_x
        self.rect.y=object_y

    def update(self):
        global keys,note_play
        a=True
        name = ""
        window.blit(self.image, (self.rect.x, self.rect.y))

        if keys[K_e] and self.rect.x-distance<player_hero.rect.x+player_size_width/2 <self.rect.x+self.size_width+distance and self.rect.y-distance<player_hero.rect.y+player_size_height/2<self.rect.y+self.size_height+distance:
            note_play=True
        while note_play:
            for e in event.get():
                if e.type==QUIT:
                    exit()
            window.blit(img_backgraund2,(0,0))
            window.blit(self.image1, (win_width/2-self.size_width*5, win_height/2-self.size_height*5))
            keys = key.get_pressed()
            if keys[K_ESCAPE]:
                note_play=False
            for evt in pygame.event.get():
                window.blit((font.render("Введите текст, а затем нажмите enter: "+name, True, (255, 255, 255))), (100,500))
                if evt.type == QUIT:
                    exit()
                if evt.type == KEYDOWN:
                    if evt.unicode.isdigit():
                        name += evt.unicode 
                    elif evt.unicode.isalpha():
                        name += evt.unicode
                    elif evt.key == K_BACKSPACE:
                        name = name[:-1]
                    elif evt.key == K_RETURN:
                        if name==self.answer:
                            while True:
                                window.blit(img_backgraund2, (0, 0))
                                window.blit(self.image2, (win_width/2-self.size_width*5, win_height/2-self.size_height*5))
                                window.blit((font.render("вы получили это, ESC чтобы продолжить ", True, (255, 255, 255))), (100,500))
                                for e in event.get():
                                    if e.type==QUIT:
                                        exit()
                                keys = key.get_pressed()
                                display.update()
                                if keys[K_ESCAPE]:
                                    break
                            note_play=False
                            dictionary_items[self.id]=True
                            self.rect.x=-100
                        else:
                            name=''
                
                display.update()


name=None

#----FUNCTION----
def object_collide(list):
    global values_up, values_down, values_right, values_left
    for i in range(0,len(list)):
        #UP
        if  abs(player_hero.rect.y+45-(list[i].rect.y+list[i].size_height))<10 and list[i].rect.x-player_size_width< player_hero.rect.x <  (list[i].rect.x+ list[i].size_width):
            values_up=False
        #DOWN
        if  abs((player_hero.rect.y+player_size_height)-list[i].rect.y)<10 and list[i].rect.x-player_size_width< player_hero.rect.x <  (list[i].rect.x+ list[i].size_width):
            values_down=False
        #RIGHT
        if  abs((player_hero.rect.x+player_size_width)-list[i].rect.x)<10 and list[i].rect.y-player_size_height < player_hero.rect.y <  (list[i].rect.y+ list[i].size_height)-45:
            values_right=False
        #LEFT
        if  abs(player_hero.rect.x-(list[i].rect.x+list[i].size_width))<10 and list[i].rect.y-player_size_height < player_hero.rect.y <  (list[i].rect.y+ list[i].size_height)-45:
            values_left=False

def object_draw(list):
    group=sprite.Group()
    for i in range(len(list)):
        group.add(list[i])
    group.draw(window)


#----OGJECT_GAME----
player_hero=Player(600, 385)
backgraund = transform.scale(image.load(img_backgraund), (win_width, win_height))
start = transform.scale(image.load(text_start), (win_width, win_height))

#----ROOMS----
#room-1
#border
room1_wall1= Wall(0, 0, 550, 20)
room1_wall2= Wall(650, 0, 600, 20)
room1_wall3= Wall(0, 0, 20, 300)
room1_wall4= Wall(0, 400, 20, 300)
room1_wall5= Wall(0, 680, 1200, 20)
room1_wall6= Wall(1180, 0, 20, 185)
room1_wall7= Wall(1180, 285, 20, 420)
wall_room1_list = [room1_wall1,room1_wall2,room1_wall3,room1_wall4,room1_wall5,room1_wall6,room1_wall7]
#door
door1_room1=Door(550, 0, 100, 20, 600, 610,'location-6','#EFFF00','key_yellow')
door2_room1=Door(0, 300, 20, 100, 1060, 305,'location-3','#47FF78','key_green')
door3_room1=Door(1180, 185, 20, 100, 50, 140,'location-4','#F447FF','key_purple')
#decor
bed = Decor(1010, 460, 150, 200, bed_img)
bookshelf1 = Decor(20, 30, 130, 160, book_img1)
bookshelf2 = Decor(150, 20, 130, 150, book_img2)
round_tbl = Decor(100, 160, 130, 85, round_tbl_img)
tbl = Decor(480, 570, 260, 100, tbl_img)
#фоновые объекты
carpet = Decor(500, 300, 300, 200, carpet_img)#ковер

#1+1
note1=Note(150,190,30,45,'IMG/note_dark_blue.png','')
object_key_green=Interactive_object(550,600,50,50,'IMG/chest_green.png','key_green','python','IMG/key_green.png')

decor_list1 = [bed, bookshelf1, bookshelf2, tbl,round_tbl]
decor_list11 = [carpet,bed, bookshelf1, bookshelf2, tbl,round_tbl]


#room-2
#border
room2_wall1 = Wall(0, 0, 1210, 20)
room2_wall2 = Wall(0, 0, 20, 700)
room2_wall3 = Wall(0, 680, 850, 20)
room2_wall4 = Wall(950, 680, 550, 20)
room2_wall5 = Wall(1180, 0, 20, 695)
list_wall_room2 = [room2_wall1,room2_wall2,room2_wall3,room2_wall4,room2_wall5]
#Двери
door1_room2=Door(850, 680, 100, 20, 920, 70,'location-4','#00FFFF','key_blue')
#Декор
round_tbl2 = Decor(985, 525, 145, 125, round_tbl_img)
bookshelf3 = Decor(870, 10, 175, 130, book_img1)
bookshelf4 = Decor(1045, 15, 115, 135, book_img2)
bookshelf5 = Decor(20, 10, 130, 140, book_img3)
bookshelf6 = Decor(145, 20, 130, 140, book_img4)
bed2 = Decor(20, 475, 165, 200, bed2_img)
tbl2 = Decor(480, 300, 255, 100, tbl_img)
#
object_key_dark_blue=Interactive_object(550,600,50,50,'IMG/chest_dark_blue.png','key_dark_blue','Тисовой','IMG/key_dark_blue.png')
note_dark_yellow=Note(150,190,30,45,'IMG/note_yellow.png','')

#room-3
#border
room3_wall1 = Wall(0, 0, 550, 20)
room3_wall2 = Wall(0, 0, 20, 680)
room3_wall3 = Wall(0, 680, 1200, 20)
room3_wall4 = Wall(1180, 0, 20, 260)
room3_wall5 = Wall(1180, 350, 20, 335)
room3_wall6 = Wall(650, 0, 650, 20)
list_wall_room3 = [room3_wall1,room3_wall2,room3_wall3,room3_wall4,room3_wall5,room3_wall6]
#Двери
door1_room3=Door(1180, 250, 20, 100, 115, 345,'location-1','#47FF78','key_green')
door2_room3=Door(550, 0, 100, 20, 600, 610,'location-5','#1A00FF','key_dark_blue')
#Декор
bookshelf7 = Decor(20, 10, 150, 190, book_img3)
round_tbl3 = Decor(200, 70, 120, 120, round_tbl_img)
tbl3 = Decor(560, 220, 125, 230, tbl_img)
#
object_key_purpule=Interactive_object(550,400,50,50,'IMG/chest_purple.png','key_purple','1991','IMG/key_purple.png')

#room-4
#border
room4_wall1= Wall(0, 0, 20, 125)
room4_wall2= Wall(0, 225, 20, 510)
room4_wall3= Wall(0, 680, 1210, 20)
room4_wall4= Wall(1000, 0, 310, 20)
room4_wall5= Wall(0, 0, 900, 20)
room4_wall6= Wall(1180, 0, 20, 690)
list_wall_room4 = [room4_wall1,room4_wall2,room4_wall3,room4_wall4,room4_wall5,room4_wall6]
#Двери
door1_room4=Door(900, 0, 100, 20, 920, 600,'location-2','#00FFFF','key_blue')
door2_room4=Door(0, 125, 20, 100, 1100, 200,'location-1','#F447FF','key_purple')
#Декор
tbl4 = Decor(435, 30, 330, 200, tbl_img)
round_tbl4 = Decor(1000, 275, 140, 125, round_tbl_img)
bed3 = Decor(20, 520, 115, 165, bed3_img)
#
object_key_blue=Interactive_object(1000,600,50,50,'IMG/chest_blue.png','key_blue','4587','IMG/key_blue.png')

#room-5
#border
room5_wall1 = Wall(0, 0, 700, 20)
room5_wall2 = Wall(0, 0, 20, 700)
room5_wall3 = Wall(700, 0, 495, 20)
room5_wall4 = Wall(0, 680, 550, 20)
room5_wall5 = Wall(645, 680, 550, 20)
room5_wall6 = Wall(1180, 0, 20, 695)
list_wall_room5 = [room5_wall1,room5_wall2,room5_wall3,room5_wall4,room5_wall5,room5_wall6]
#Двери
door1_room5=Door(550, 680, 100, 20, 600, 70,'location-3','#1A00FF','key_dark_blue')
#Декор
bed4 = Decor(20, 500, 175, 180, bed4_img)
bookshelf8, bookshelf9 = Decor(440, 20, 140, 140, book_img5), Decor(580, 20, 180, 140, book_img6) 
tbl5 = Decor(480, 145, 190, 70, tbl_img)
#
object_key_yellow=Interactive_object(550,150,50,50,'IMG/chest_yellow.png','key_yellow','Лангольеры','IMG/key_yellow.png')
object_key_red=Interactive_object(100,100,50,50,'IMG/chest_red.png','key_red','Чужак','IMG/key_red.png')

#room-6
#border
room6_wall1 = Wall(0, 0, 550, 20)
room6_wall2 = Wall(650,0 , 550, 20)
room6_wall3 = Wall(0, 680, 550, 20)
room6_wall4 = Wall(650, 680, 700, 20)

room6_wall5 = Wall(1180, 0, 20, 695)
room6_wall6 = Wall(0, 0, 20, 695)
list_wall_room6 = [room6_wall1,room6_wall2,room6_wall3,room6_wall4,room6_wall5,room6_wall6]
#Двери
door1_room6=Door(550, 680, 100, 20, 600, 70,'location-1','#EFFF00','key_yellow')
door2_room6=Door(550, 0, 100, 20, player_hero.rect.x, player_hero.rect.y,'final','#FF0000','key_red')
#Декор
bookshelf10, bookshelf11 = Decor(455, 130, 110, 180, book_img5), Decor(560, 130, 150, 180, book_img6)
tbl6 = Decor(460, 310, 245, 80, tbl_img)
##
note_red=Note(500,300,30,50,'IMG/note_cover.jpg','Похоже кто-то закрасил название книги')

#список декора по комнатам: 1 - первая комната и т.д.
decor_list2 = [round_tbl2, bookshelf3, bookshelf4, bookshelf5, bookshelf6, bed2, tbl2]
decor_list3 = [bookshelf7, tbl3, round_tbl3]
decor_list4 = [bed3, tbl4, round_tbl4]
decor_list5 = [bed4, bookshelf8, bookshelf9, tbl5]
decor_list6 = [tbl6, bookshelf10, bookshelf11]
decor_list = [decor_list1, decor_list2, decor_list3, decor_list4, decor_list5, decor_list6]

#----VARIABLE----
location='menu'

note_play=False
carpet_checker=a=b1=question_start=gold_key=False

while True:
    keys = key.get_pressed()
    values_up = values_down = values_right = values_left = True
    for e in event.get():
        if e.type==QUIT:
            exit()

    if location == 'menu':
        window.blit(backgraund,(0, 0))
        object_draw(wall_room1_list),object_draw(decor_list11)
        door1_room1.update(), door2_room1.update(),door3_room1.update()
        player_hero.update()
        
        window.blit(start, (0, 0))
        if keys[K_SPACE]:
            location = "location-1"

    elif location == 'location-1':
        window.blit(backgraund,(0, 0))
        
        object_collide(wall_room1_list),object_collide(decor_list1)

        if sprite.collide_rect(door1_room1, player_hero):
            door1_room1.teleportation()
        elif sprite.collide_rect(door2_room1, player_hero):
            door2_room1.teleportation()
        elif sprite.collide_rect(door3_room1, player_hero):
            door3_room1.teleportation()

        door1_room1.update(), door2_room1.update(), door3_room1.update()
        object_draw(wall_room1_list),object_draw(decor_list11)

        object_key_green.update()
        note1.update()
        player_hero.update()
 
    elif location == 'location-2':
        window.blit(backgraund,(0, 0))

        object_collide(list_wall_room2)
        object_collide(decor_list2)

        door1_room2.update()

        
        object_draw(decor_list2)
        object_draw(list_wall_room2)
        object_key_dark_blue.update()
        note_dark_yellow.update()
        player_hero.update()


        if sprite.collide_rect(door1_room2, player_hero):
            door1_room2.teleportation()

    elif location == 'location-3':
        window.blit(backgraund,(0, 0))

        object_collide(list_wall_room3)
        object_collide(decor_list3)
        door1_room3.update(), door2_room3.update()

        
        object_draw(decor_list3)
        object_draw(list_wall_room3)
        object_key_purpule.update()
        player_hero.update()


        if sprite.collide_rect(door1_room3, player_hero):
            door1_room3.teleportation()
        elif sprite.collide_rect(door2_room3, player_hero):
            door2_room3.teleportation()

    elif location == 'location-4':
        window.blit(backgraund,(0, 0))

        object_collide(list_wall_room4)
        object_collide(decor_list4)

        door1_room4.update(), door2_room4.update()

        
        object_draw(decor_list4)
        object_draw(list_wall_room4)
        object_key_blue.update()
        player_hero.update()


        if sprite.collide_rect(door1_room4, player_hero):
            door1_room4.teleportation()
        elif sprite.collide_rect(door2_room4, player_hero):
            door2_room4.teleportation()

    elif location == 'location-5':
        window.blit(backgraund,(0, 0))

        object_collide(list_wall_room5)
        object_collide(decor_list5)

        door1_room5.update()
        
        object_draw(decor_list5)
        object_draw(list_wall_room5)
        object_key_yellow.update()
        object_key_red.update()
        player_hero.update()


        if sprite.collide_rect(door1_room5, player_hero):
            door1_room5.teleportation()

    elif location == 'location-6':
        window.blit(backgraund,(0, 0))

        object_collide(list_wall_room6)
        object_collide(decor_list6)
        
        door1_room6.update(),door2_room6.update()
        
        object_draw(decor_list6)
        object_draw(list_wall_room6)
        note_red.update()
        player_hero.update()


        if sprite.collide_rect(door1_room6, player_hero):
            door1_room6.teleportation()
        if sprite.collide_rect(door2_room6, player_hero):
            door2_room6.teleportation()
    elif location == 'final':
        window.fill('#000000')
        window.blit(transform.scale(image.load('IMG/text_final.png'), (800, 600)), (240, 10))

    display.update()
    clock.tick(FPS)
