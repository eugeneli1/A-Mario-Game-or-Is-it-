import pygame
################
def crop(img,rows,cols):
    image = pygame.image.load(img)
    width, height = image.get_size()
    cellWidth, cellHeight = width / cols, height / rows
    print(cellWidth,cellHeight,img)
    images = []
    for i in range(rows):
        for j in range(cols):
            subImage = image.subsurface(
                (j * cellWidth, i * cellHeight, cellWidth, cellHeight))
            images.append(subImage)
    return images
def startbuttonboundary(mx,my,width,height):
    if (mx >= width*0.3 and mx <= (width*0.3 + 80)
        and my >= height*0.6 and my <= height*0.6 + 41):
            return True
    return False
######write message function###########
def message(msg,color,fontsize,fonttype,surface,location):
    font = pygame.font.SysFont(fonttype, fontsize) 
    text = font.render(msg,True,color)
    surface.blit(text, [location[0],location[1]])
######basic implement img and draw square##################
class basicimg(pygame.sprite.Sprite):
    def __init__(self, width = 64,height = 64,color = (255,255,255)):
        super(basicimg, self).__init__()
        self.image = pygame.Surface((width,height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
    def getimg(self,img = None):
        if img != None:
            self.image = pygame.image.load(img)
            self.rect = self.image.get_rect()
    def setposition(self,x,y):
        self.rect.x = x
        self.rect.y = y
    def info(self):
        return (self.rect.x,self.rect.y) 
        
class basiccroppedimg(pygame.sprite.Sprite):
    def __init__(self, width = 64,height = 64,color = (255,255,255)):
        super(basiccroppedimg, self).__init__()
        self.image = pygame.Surface((width,height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
    def getimg(self,img = None):
        if img != None:
            self.image = img
            self.rect = self.image.get_rect()
    def setposition(self,x,y):
        self.rect.x = x
        self.rect.y = y
    def info(self):
        return (self.rect.x,self.rect.y) 
        
class questionmark(pygame.sprite.Sprite):
    def __init__(self,img,x,y):
        super(questionmark,self).__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 
    def setpos(self,questionchange,questiony):
        self.rect.x += questionchange
        self.rect.y += questiony
    def info(self):
        return [self.rect.x,self.rect.y]
        
class emptybox(pygame.sprite.Sprite):
    def __init__(self,img,x,y):
        super(emptybox,self).__init__()
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 
    def setpos(self,questionchange,questiony):
        self.rect.x += questionchange
        self.rect.y += questiony
    def info(self):
        return [self.rect.x,self.rect.y]
class brick(pygame.sprite.Sprite):
    def __init__(self,img,x,y,questionchange):
        super(brick,self).__init__()
        self.image = pygame.image.load(img) 
        self.rect = self.image.get_rect()
        self.rect.x = x + questionchange
        self.rect.y = y
    def info(self):
        return (self.rect.x,self.rect.y) 
class tube(pygame.sprite.Sprite):
    def __init__(self, width,height,color,x,y,questionchange):
        super(tube, self).__init__()
        self.image = pygame.Surface((width,height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x + questionchange
        self.rect.y = y
    def info(self):
        return (self.rect.x,self.rect.y) 
class stair(pygame.sprite.Sprite):
    def __init__(self,img,x,y,questionchange):
        super(stair,self).__init__()
        self.image = pygame.image.load(img) 
        self.rect = self.image.get_rect()
        self.rect.x = x + questionchange
        self.rect.y = y
    def info(self):
        return (self.rect.x,self.rect.y)
        
class stepon(pygame.sprite.Sprite):
    def __init__(self,img,x,y,questionchange):
        super(stepon,self).__init__()
        self.image = pygame.image.load(img) 
        self.rect = self.image.get_rect()
        self.rect.x = x + questionchange
        self.rect.y = y
    def info(self):
        return (self.rect.x,self.rect.y) 
class animal(pygame.sprite.Sprite):
    def __init__(self,img,x,y,questionchange,animalmove):
        super(animal,self).__init__()
        self.image = img 
        self.rect = self.image.get_rect()
        self.rect.x = x + questionchange + animalmove
        self.rect.y = y
    def info(self):
        return (self.rect.x,self.rect.y) 
        
class animalpt2(pygame.sprite.Sprite):
    def __init__(self,img,x,y,questionchange,animalmove,questionchangey):
        super(animalpt2,self).__init__()
        self.image = img 
        self.rect = self.image.get_rect()
        self.rect.x = x + questionchange + animalmove
        self.rect.y = y + questionchangey
    def info(self):
        return (self.rect.x,self.rect.y) 
class coin(pygame.sprite.Sprite):
    def __init__(self,img,x,y,questionchange):
        super(coin,self).__init__()
        self.image = img 
        self.rect = self.image.get_rect()
        self.rect.x = x + questionchange
        self.rect.y = y
    def info(self):
        return (self.rect.x,self.rect.y) 

class mushroomanim(pygame.sprite.Sprite):
    def __init__(self,img,x,y,questionchange,mushroommove,questionchangey):
        super(mushroomanim,self).__init__()
        self.image = img 
        self.rect = self.image.get_rect()
        self.rect.x = x + questionchange + mushroommove
        self.rect.y = y + questionchangey
    def info(self):
        return (self.rect.x,self.rect.y) 
    
class flag(pygame.sprite.Sprite):
    def __init__(self,img,x,y,questionchange,flagy):
        super(flag,self).__init__()
        self.image = pygame.image.load(img) 
        self.rect = self.image.get_rect()
        self.rect.x = x + questionchange
        self.rect.y = y + flagy
    def info(self):
        return (self.rect.x,self.rect.y)
class pole(pygame.sprite.Sprite):
    def __init__(self, width,height,color,x,y,questionchange):
        super(pole, self).__init__()
        self.image = pygame.Surface((width,height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x + questionchange
        self.rect.y = y
    def info(self):
        return (self.rect.x,self.rect.y)

class death(pygame.sprite.Sprite):
    def __init__(self,img,x,y,questionchange):
        super(death,self).__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y + questionchange
    def info(self):
        return (self.rect.x,self.rect.y)
class flagmario(pygame.sprite.Sprite):
    def __init__(self,img,x,y,xchange,ychange,pos):
        super(flagmario,self).__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x + xchange + pos
        self.rect.y = y + ychange
    def info(self):
        return (self.rect.x,self.rect.y)
######introgroup###
widths = 400
heights = 300
red = (255,0,0) 
white = (255,255,255) 
tinyright = crop("/Users/EugeneLi/Desktop/tp/mariobrostinyright.png",1,14)
intro_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
questionmark_group = pygame.sprite.Group()
brick_group = pygame.sprite.Group()
tube_group = pygame.sprite.Group()
stair_group = pygame.sprite.Group()
stepon_group = pygame.sprite.Group()
draw_mushroomgroup1 = pygame.sprite.Group()
draw_mushroomgroup2 = pygame.sprite.Group()
draw_mushroomgroup3 = pygame.sprite.Group()
flag_group = pygame.sprite.Group()
pole_group = pygame.sprite.Group()
animal_group1 = pygame.sprite.Group()
animal_group2 = pygame.sprite.Group()
animal_group3 = pygame.sprite.Group()
animal_group4 = pygame.sprite.Group()
animal_group5 = pygame.sprite.Group()
animal_group6 = pygame.sprite.Group()
animal_group7 = pygame.sprite.Group()
animal_group8 = pygame.sprite.Group()
animal_group9 = pygame.sprite.Group()
animal_group10 = pygame.sprite.Group()
animal_group11 = pygame.sprite.Group()
animal_group12 = pygame.sprite.Group()
death_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
########
questionmarkimg = crop("/Users/EugeneLi/Desktop/tp/questionimage.png", 3,4)
q1 = questionmark(questionmarkimg[0],345,188) 
q2 = questionmark(questionmarkimg[0],463,188) 
q3 = questionmark(questionmarkimg[0],495,188) 
q4 = questionmark(questionmarkimg[0],1377,188)
q5 = questionmark(questionmarkimg[0],1670,188)
q6 = questionmark(questionmarkimg[0],2000,120)
q7 = questionmark(questionmarkimg[0],2160,188)
q8 = questionmark(questionmarkimg[0],477,120)
q9 = questionmark(questionmarkimg[0],2283,188)
q10 = questionmark(questionmarkimg[0],2343,188) 
q11 = questionmark(questionmarkimg[0],2392,188)
q12 = questionmark(questionmarkimg[0],2342,120)
q13 = questionmark(questionmarkimg[0],2780,120)
q14 = questionmark(questionmarkimg[0],2796,120)
q15 = questionmark(questionmarkimg[0],3650,188)
            ##
q16 = questionmark(questionmarkimg[1],345,188) 
q17 = questionmark(questionmarkimg[1],463,188)  
q18 = questionmark(questionmarkimg[1],495,188) 
q19 = questionmark(questionmarkimg[1],1377,188)
q20= questionmark(questionmarkimg[1],1670,188)
q21 = questionmark(questionmarkimg[1],2000,120)
q22 = questionmark(questionmarkimg[1],2160,188)
q23= questionmark(questionmarkimg[1],477,120)
q24 = questionmark(questionmarkimg[1],2283,188)
q25 = questionmark(questionmarkimg[1],2343,188)
q26 = questionmark(questionmarkimg[1],2392,188)
q27 = questionmark(questionmarkimg[1],2342,120)
q28 = questionmark(questionmarkimg[1],2780,120)
q29 = questionmark(questionmarkimg[1],2796,120)
q30 = questionmark(questionmarkimg[1],3650,188)
            ####
q31 = questionmark(questionmarkimg[2],345,188) 
q32 = questionmark(questionmarkimg[2],463,188) 
q33 = questionmark(questionmarkimg[2],495,188) 
q34 = questionmark(questionmarkimg[2],1377,188)
q35 = questionmark(questionmarkimg[2],1670,188)
q36 = questionmark(questionmarkimg[2],2000,120)
q37 = questionmark(questionmarkimg[2],2160,188)
q38 = questionmark(questionmarkimg[2],477,120)
q39 = questionmark(questionmarkimg[2],2283,188)
q40 = questionmark(questionmarkimg[2],2343,188)
q41 = questionmark(questionmarkimg[2],2392,188)
q42 = questionmark(questionmarkimg[2],2342,120)
q43 = questionmark(questionmarkimg[2],2780,120)
q44 = questionmark(questionmarkimg[2],2796,120)
q45 = questionmark(questionmarkimg[2],3650,188)
            #####
q46 = questionmark(questionmarkimg[2],345,188) 
q47 = questionmark(questionmarkimg[2],463,188) 
q48 = questionmark(questionmarkimg[2],495,188) 
q49 = questionmark(questionmarkimg[2],1377,188) 
q50 = questionmark(questionmarkimg[2],1670,188)
q51 = questionmark(questionmarkimg[2],2000,120)
q52 = questionmark(questionmarkimg[2],2160,188)
q53 = questionmark(questionmarkimg[2],477,120)
q54= questionmark(questionmarkimg[2],2283,188)
q55 = questionmark(questionmarkimg[2],2343,188)
q56 = questionmark(questionmarkimg[2],2392,188)
q57 = questionmark(questionmarkimg[2],2342,120)
q58 = questionmark(questionmarkimg[2],2780,120)
q59 = questionmark(questionmarkimg[2],2796,120)
q60 = questionmark(questionmarkimg[2],3650,188)

mushroom_group = pygame.sprite.Group()
mushroom_group.add(q2,q17,q32,q47,q4,q19,q34,q49,q57,q42,q27,q12)
mushroom_group1 = pygame.sprite.Group()
mushroom_group2 = pygame.sprite.Group()
mushroom_group3 = pygame.sprite.Group()
mushroom_group1.add(q2,q17,q32,q47)
mushroom_group2.add(q4,q19,q34,q49)
mushroom_group3.add(q57,q42,q27,q12)
#####################################
def introgroup():
    introstartbutton2 =basicimg()
    introstartbutton2.getimg("/Users/EugeneLi/Desktop/tp/button.png")
    introstartbutton2.setposition(0.55*widths,0.64*heights)
    introstartbutton = basicimg()
    introstartbutton.getimg("/Users/EugeneLi/Desktop/tp/button2.png") 
    introstartbutton.setposition(0.3*widths,0.6*heights)
    intro_group.add(introstartbutton2,introstartbutton) 
introgroup()
def playergroup(img,x,y):
    player1 = basiccroppedimg()
    player1.getimg(img)
    player1.setposition(x,y)
    player_group.empty()
    player_group.add(player1) 
playergroup(tinyright[6], 100,200)
#####################animation############
def mariojumpanimation(screen,imgbigleft,imgbigright,imgsmallleft,imgsmallright,
                mushroom, left,right,mariomovex,mariomovey,width,height,olddir):
    if mushroom == False:
        if right == True:
            playergroup(imgsmallright[4],mariomovex*width,mariomovey *height)
        if left == True:
            playergroup(imgsmallleft[4],mariomovex*width,mariomovey *height)
        if left == False and right == False:
            if olddir == "right":
                 playergroup(imgsmallright[4],
                    mariomovex*width,mariomovey *height)
            if olddir == "left":
                 playergroup(imgsmallleft[4],
                    mariomovex*width,mariomovey *height)
    if mushroom == True:
        if right == True:
            playergroup(imgbigright[4],
                mariomovex*width,mariomovey *height)
        if left == True:
            playergroup(imgbigleft[4],
                mariomovex*width,mariomovey *height)
        if left == False and right == False:
            if olddir == "right":
                 playergroup(imgbigright[4],
                    mariomovex*width,mariomovey *height)
            if olddir == "left":
                 playergroup(imgbigleft[4],
                    mariomovex*width,mariomovey *height)
    player_group.draw(screen) 
    
def mariomoveanimation(screen,imgbigleft,imgbigright,imgsmallleft,imgsmallright
                    ,marioanimationmove,width,height,mariomove,mushroom,
                    moveleft,moveright,olddir,mariomovey):
    if mushroom == False:
        if moveleft == True:
            if marioanimationmove == 2:
                playergroup(imgsmallleft[0],mariomove*width,height*mariomovey)
            if marioanimationmove == 3:
                playergroup(imgsmallleft[1],mariomove*width,height*mariomovey)
            if marioanimationmove == 4:
                playergroup(imgsmallleft[2],mariomove*width,height*mariomovey)
        if moveright == True:
            if marioanimationmove == 2:
                playergroup(imgsmallright[0],mariomove*width,height*mariomovey)
            if marioanimationmove == 3:
                playergroup(imgsmallright[1],mariomove*width,height*mariomovey)
            if marioanimationmove == 4:
                playergroup(imgsmallright[2],mariomove*width,height*mariomovey)
        if moveright == False and moveleft == False:
            if olddir == "left":
                if marioanimationmove <= 0 and marioanimationmove >= -6:
                    playergroup(imgsmallleft[3],
                        mariomove*width,height*mariomovey)
                if marioanimationmove < -6:
                    playergroup(imgsmallleft[6],
                        mariomove*width,height*mariomovey)
            else:
                if marioanimationmove <= 0 and marioanimationmove >= -6:
                    playergroup(imgsmallright[3],
                        mariomove*width,height*mariomovey)
                if marioanimationmove < -6:
                    playergroup(imgsmallright[6],
                        mariomove*width,height*mariomovey)
    if mushroom == True:
        if moveleft == True:
            if marioanimationmove == 2:
                playergroup(imgbigleft[0],mariomove*width,height*mariomovey)
            if marioanimationmove == 3:
                playergroup(imgbigleft[1],mariomove*width,height*mariomovey)
            if marioanimationmove == 4:
                playergroup(imgbigleft[2],mariomove*width,height*mariomovey)
        if moveright == True:
            if marioanimationmove == 2:
                playergroup(imgbigright[0],mariomove*width,height*mariomovey)
            if marioanimationmove == 3:
                playergroup(imgbigright[1],mariomove*width,height*mariomovey)
            if marioanimationmove == 4:
                playergroup(imgbigright[2],mariomove*width,height*mariomovey)
        if moveright == False and moveleft == False:
            if olddir == "left":
                if marioanimationmove <= 0 and marioanimationmove >= -6:
                    playergroup(imgbigleft[3],
                        mariomove*width,height*mariomovey)
                if marioanimationmove < -6:
                    playergroup(imgbigleft[6],
                        mariomove*width,height*mariomovey)
            else:
                if marioanimationmove <= 0 and marioanimationmove >= -6:
                    playergroup(imgbigright[3],
                        mariomove*width,height*mariomovey)
                if marioanimationmove < -6:
                    playergroup(imgbigright[6],
                        mariomove*width,height*mariomovey)
    player_group.draw(screen)
#########################all the items on the map#######
def drawbrick(screen,brickimg,questionpos):
    ##short ones###
    b1 = brick(brickimg,447,188, questionpos)
    b2 = brick(brickimg, 479,188,questionpos) 
    b3 = brick(brickimg, 511,188,questionpos) 
    b4 = brick(brickimg, 1654, 188, questionpos) 
    b5 = brick(brickimg, 1686, 188, questionpos)
    b6 = brick(brickimg, 2000, 188, questionpos) 
    b7 = brick(brickimg, 2144, 188, questionpos) 
    b8 = brick(brickimg, 2540, 188, questionpos)
    b9 = brick(brickimg, 2764, 120, questionpos) 
    b10 = brick(brickimg, 2812, 120, questionpos) 
    b11 = brick(brickimg, 3666, 188, questionpos) 
    ##long ones### 
    b12 = brick(brickimg, 1702, 120, questionpos) 
    b13 = brick(brickimg, 1718, 120, questionpos) 
    b14 = brick(brickimg, 1734, 120, questionpos) 
    b15 = brick(brickimg, 1750, 120, questionpos) 
    b16 = brick(brickimg, 1766, 120, questionpos) 
    b17 = brick(brickimg, 1782, 120, questionpos) 
    b18 = brick(brickimg, 1798, 120, questionpos) 
    b19 = brick(brickimg, 1814, 120, questionpos) 
    b20 = brick(brickimg, 1830, 120, questionpos) 
    b21 = brick(brickimg, 1846, 120, questionpos) 
    b22 = brick(brickimg, 1862, 120, questionpos) 
    b23 = brick(brickimg, 1984, 120, questionpos) 
    b24 = brick(brickimg, 1968, 120, questionpos) 
    b25 = brick(brickimg, 1952, 120, questionpos) 
    b26 = brick(brickimg, 2600, 120, questionpos) 
    b27 = brick(brickimg, 2616, 120, questionpos) 
    b28 = brick(brickimg, 2632, 120, questionpos) 
    b29 = brick(brickimg, 2648, 120, questionpos) 
    b30 = brick(brickimg, 2780, 188, questionpos) 
    b31 = brick(brickimg, 2796, 188, questionpos) 
    b32 = brick(brickimg, 3634, 188, questionpos) 
    b33 = brick(brickimg, 3618, 188, questionpos) 
    brick_group.empty()
    brick_group.add(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,
                b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,
                b24,b25,b26,b27,b28,b29,b30,b31,b32,b33)
    brick_group.draw(screen)  
    
def drawtube(screen,tubeimg,questionpos,tubebottom):
    t1 = tube(39,50,(255,255,255), 603,223,questionpos)
    t2 = tube(39,90,(255,255,255), 818, 204, questionpos) 
    t3 = tube(39,120,(255,255,255), 987, 180, questionpos) 
    t4 = tube(39,120,(255,255,255), 1223, 180, questionpos) 
    t5 = tube(39,50,(255,255,255), 3494, 223,questionpos)
    t6 = tube(39,50,(255,255,255), 3837, 223,questionpos)
    tube_group.empty()
    tube_group.add(t1,t2,t3,t4,t5,t6) 

def drawstairs(screen,stairimg, questionpos): 
    stair_group.empty()
    x = 3000
    y = 188
    s1 = stair(stairimg, x,y,questionpos) 
    x2 = 2939
    y2 = 188
    s2 = stair(stairimg, x2,y2, questionpos) 
    x3 = 3238
    y3 = 188
    s3 = stair(stairimg, x3,y3, questionpos)
    s7 = stair(stairimg, 3254, 188, questionpos) 
    x4 = 3321
    y4 = 188
    s4 = stair(stairimg, x4,y4,questionpos) 
    x5 = 3950
    y5 = 188
    s5 = stair(stairimg, x5,y5, questionpos) 
    s6 = stair(stairimg, 4012, 120, questionpos) 
    s8 = stair(stairimg, 4070, 188, questionpos) 
    s9 = stair(stairimg, 4085,188,questionpos) 
    s10 = stair(stairimg, 4100, 188, questionpos)
    s11 = stair(stairimg, 4115, 188, questionpos) 
    s12 = stair(stairimg, 4130, 188, questionpos) 
    s13 = stair(stairimg, 4145, 188, questionpos)  
    s14 = stair(stairimg, 4160, 188, questionpos)  
    s15 = stair(stairimg, 4175, 188, questionpos)  
    s16 = stair(stairimg, 4190, 188, questionpos)   
    stair_group.empty()
    stair_group.add(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16) 
    stair_group.draw(screen) 

def addstepon(screen,steponimg, questionpos):
    stepon_group.empty()
    x = 0
    y = 268
    for j in range(71):
        st1 = stepon(steponimg, x,y, questionpos) 
        stepon_group.add(st1)
        x += 21
    x = 0
    y2 = 290
    for j in range(71):
        st2 = stepon(steponimg, x,y2, questionpos) 
        stepon_group.add(st2)
        x += 21
    x += 21+10
    y = 268
    for j in range(16):
        st2 = stepon(steponimg, x,y, questionpos) 
        stepon_group.add(st2)
        x += 21   
    x -= 21*16
    y = 290
    for j in range(16):
        st2 = stepon(steponimg, x,y, questionpos) 
        stepon_group.add(st2)
        x += 21   
    x += 21*2
    y = 268
    for j in range(200):
        st2 = stepon(steponimg, x,y, questionpos) 
        stepon_group.add(st2)
        x += 21
    y = 290
    x -= 200*21
    for j in range(200):
        st2 = stepon(steponimg, x,y, questionpos) 
        stepon_group.add(st2)
        x += 21
    stepon_group.draw(screen)
def drawanimal1(screen,animalimg, 
    questionpos,animalchange,x,y,group):
    a1 = animal(animalimg, x, y, questionpos, animalchange)
    group.empty()
    group.add(a1)
    group.draw(screen)
    
def drawanimal2(screen,animalimg, questionpos,
    animalchange,x,y,group,questionchangey):
    a1 = animalpt2(animalimg, x, y, questionpos, animalchange,questionchangey)
    group.empty()
    group.add(a1)
    group.draw(screen)
def coinanimation(screen, animationcount, img, questionpos,x,y):
    if animationcount ==0:
        c1 = coin(img[8], x,y,questionpos)
    if animationcount== 1:
        c1 = coin(img[9], x,y,questionpos)
    if animationcount ==2:
        c1 = coin(img[10], x,y,questionpos)
    if animationcount ==3:
        c1 = coin(img[11], x,y,questionpos)
    coin_group.empty()
    coin_group.add(c1)
    coin_group.draw(screen)
##################################
###################
class PygameGame(object):
    def __init__(self, width=widths, height=heights, fps=60, title="Mario Game"):
        #####picture######
        self.startingscreen = pygame.image.load("/Users/EugeneLi/Desktop/tp/mariomenu.jpg") 
        self.background = pygame.image.load("/Users/EugeneLi/Desktop/tp/level_1.png")
        self.mariobigleft = crop("/Users/EugeneLi/Desktop/tp/mariobroleft.png",1,19)[::-1]
        self.mariobigright = crop("/Users/EugeneLi/Desktop/tp/mariobroright.png",1,19) 
        self.mariotinyleft = crop("/Users/EugeneLi/Desktop/tp/mariobrostinyleft.png",1,14)[::-1]
        self.mariotinyright = crop("/Users/EugeneLi/Desktop/tp/mariobrostinyright.png",1,14)
        self.brickimg = "/Users/EugeneLi/Desktop/tp/singlebrick.png"
        self.tubeimg = "/Users/EugeneLi/Desktop/tp/tube.png"
        self.tubebottom = "/Users/EugeneLi/Desktop/tp/bottomtube.png"
        self.stairimg = "/Users/EugeneLi/Desktop/tp/stair.png"
        self.steponimg = "/Users/EugeneLi/Desktop/tp/stepon.png"
        self.enemy = crop("/Users/EugeneLi/Desktop/tp/enemies.png",1,3)
        self.empty_box = "/Users/EugeneLi/Desktop/tp/empty_box.png"
        self.mushroomimg = crop("/Users/EugeneLi/Desktop/tp/mushroom.png",1,3)
        self.flagimg = "/Users/EugeneLi/Desktop/tp/flag.png"
        self.helpback = "/Users/EugeneLi/Desktop/tp/help_background.jpg"
        self.arrowimg ="/Users/EugeneLi/Desktop/tp/arrows.png"
        #####basic##########
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        #####gamemode##############
        self.Trueback = False
        self.playing = False 
        self.intro = True
        self.endgame = False
        self.restartgame = False
        self.deathmode = False
        self.collectscorescreen = False
        self.greatscore = 9999
        ######screen movement####
        self.screenmove = 0
        self.screenchange = 0 
        ##animation move####
        self.marioanimationmove = 0 
        self.questionmarkanimation = 0 
        self.boxanimation = 0 
        self.boxanimationswitch1 = False
        self.boxanimationswitch2 = False
        self.boxanimationswitch3 = False
        self.boxanimationswitch4 = False
        ####items true and false####
        self.mushroom = False
        self.mushroomtransfanim = False 
        self.mushroomtranscount = 0 
        self.storemushroomy = 0 
        self.mushroomanimation1 = False
        self.mushroomanimation2 = False
        self.mushroomanimation3 = False
        self.mushroomx1 = None
        self.mushroomx2 = None
        self.mushroomx3 = None
        self.mushroomy1 = None
        self.mushroomy2 = None
        self.mushroomy3 = None
        self.mushroommovex1 = 0
        self.mushroommovex2 = 0
        self.mushroommovex3 = 0
        self.mushroommovey1 = 0 
        self.mushroommovey2 = 0
        self.mushroommovey3 = 0
        self.mushroomchangex1 = None 
        self.mushroomchangex2 = None
        self.mushroomchangex3 = None
        self.mushroomchangey1 = None 
        self.mushroomchangey2 = None
        self.mushroomchangey3 = None
        self.letmushgo1 = False
        self.letmushgo2 = False
        self.letmushgo3 = False
        self.questionChange = 0
        self.questionPos = 0
        self.questiony1 = -1
        self.questiony2 = -1
        self.questiony3 = -1
        self.questiony4 = -1
        self.storemariomonstery = None
        self.mushroomawayanim = False
        ###mario movement####
        self.mariomovex = 0.2
        self.mariochangex = 0.004
        self.mariomovey = 0.850
        self.standingy = ((0.844*300)+ 15)/300
        self.moveleft = self.moveright = False
        self.olddir = "right" 
        self.justmark = False
        ###jump###
        self.mariojump = 0 
        self.jumpchange = 0 
        self.jumpacceleration = 0
        self.jumponoff = False 
        self.jumppeak = 0.5 
        self.jumpkeyreleasebelow = False 
        self.jumpkeyreleaseabove = False 
        self.forcedown = False
        self.differentplatform = False 
        self.sidewaypump = False 
        self.storeoldy = None 
        self.tubemark = False 
        ###animal 1##
        self.animalmove1 = 0 
        self.animalchange1 = 2
        self.animal1switch = False
        self.animal1pause = False
        self.animal1pausecount = 0 
        self.animal1animation = 0 
        self.screenswitch1 = False 
        ######animal 2##
        self.animalmove2 = 0 
        self.animalanimation2 = 0 
        self.animalchange2 = 2
        self.animalswitch2 = False
        self.animalpause2 = False
        self.animalpausecount2 = 0
        self.screenswitch2 = False  
        ##animal 3##
        self.animalmove3 = 0 
        self.animalanimation3 = 0 
        self.animalchange3 = 2
        self.animalswitch3 = False
        self.animalpause3 = False
        self.animalpausecount3 = 0
        self.screenswitch3 = False  
        ###animal 4###
        self.animalmove4 = 0 
        self.animalanimation4 = 0 
        self.animalchange4 = 2
        self.animalswitch4 = False 
        self.animalpause4 = False
        self.animalpausecount4 = 0
        self.screenswitch4 = False 
        ##animal 5####
        self.animalmove5 = 0 
        self.animalanimation5 = 0 
        self.animalchange5 = 2
        self.animalswitch5 = False 
        self.animalpause5 = False
        self.animalpausecount5 = 0
        self.animaly5 = 0 
        self.screenswitch5 = False 
        ##animal 6####
        self.animalmove6= 0 
        self.animalanimation6 = 0 
        self.animalchange6 = 2
        self.animalswitch6 = False 
        self.animalpause6 = False
        self.animalpausecount6 = 0
        self.animaly6 = 0 
        self.screenswitch6 = False 
        ##animal 7####
        self.animalmove7 = 0 
        self.animalanimation7 = 0 
        self.animalchange7 = 2
        self.animalswitch7 = False
        self.animalpause7 = False
        self.animalpausecount7 = 0
        self.animaly7 = 0 
        self.screenswitch7 = False 
        ##animal 8####
        self.animalmove8 = 0 
        self.animalanimation8 = 0 
        self.animalchange8 = 2
        self.animalswitch8 = False 
        self.animalpause8 = False
        self.animalpausecount8 = 0
        self.animaly8 = 0 
        self.screenswitch8 = False 
        ##animal 9####
        self.animalmove9 = 0 
        self.animalanimation9 = 0 
        self.animalchange9 = 2
        self.animalswitch9 = False 
        self.animalpause9 = False
        self.animalpausecount9 = 0
        self.animaly9 = 0 
        self.screenswitch9 = False 
        ##animal 10####
        self.animalmove10 = 0 
        self.animalanimation10 = 0 
        self.animalchange10 = 2
        self.animalswitch10 = False
        self.animalpause10 = False
        self.animalpausecount10 = 0
        self.animaly10 = 0
        self.screenswitch10 = False  
        ##animal 11####
        self.animalmove11 = 0 
        self.animalanimation11 = 0 
        self.animalchange11 = 2
        self.animalswitch11 = False
        self.animalpause11 = False
        self.animalpausecount11 = 0
        self.animaly11 = 0
        self.screenswitch11 = False
        ##animal 12####
        self.animalmove12 = 0 
        self.animalanimation12 = 0 
        self.animalchange12 = 2
        self.animalswitch12 = False
        self.animalpause12 = False
        self.animalpausecount12 = 0
        self.animaly12 = 0
        self.screenswitch12 = False
#########################
        self.gamecount2 = 0 
        self.gamecount = 0
        self.time = 2000
        self.score = 0  
############################
        self.lives = 3
        self.deathanimation = False
        self.deathy = self.height*0.7
        self.deathychange = -5
        self.deathmove = 0
        self.deathx = None 
        self.deathacceleration = 1
####        
########questionark####
        self.question1 = pygame.sprite.Group()
        self.question1.add(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,
                    q12,q13,q14,q15)
        self.question2 = pygame.sprite.Group()
        self.question2.add(q16,q17,q18,q19,q20,q21,q22,q23,q24,
                    q25,q26,q27,q28,q29,q30)
        self.question3 = pygame.sprite.Group()
        self.question3.add(q31,q32,q33,q34,q35,q36,q37,q38,q39,
                    q40,q41,q42,q43,q44,q45)
        self.question4 = pygame.sprite.Group()
        self.question4.add(q46,q47,q48,q49,q50,q51,q52,q53,q54,
                    q55,q56,q57,q58,q59,q60)
        self.storegarbage = pygame.sprite.Group()
        self.storequestionx1 = None 
        self.storequestiony1 = None
        self.storequestionx2 = None 
        self.storequestiony2 = None
        self.storequestionx3 = None 
        self.storequestiony3 = None
        self.storequestionx4 = None 
        self.storequestiony4 = None
        self.coinanimation = False 
        self.coinanimationcount = 0
        self.coinx = None
        self.coiny = None 
####
        self.endingscreenchange = None
        self.flagy = 0
        self.flagychange = 5
        self.flagmarioychange = 5
        self.flagmarioxchange = 0
        self.flagmariomovey = 0
        self.flagmariomovex = 0
        self.yoloswitch = False
        self.flagwait = 0
        self.flagwalkanimation = 0
        #####
        self.collectscorescreen = False
        self.heartanimationtime = 0
        self.heartx = 150
        self.endgame2 = False
        self.endgame3 = False
        self.bbbcount = 0 
        self.help = False 
    #####
    ######
        self.ultimateplaying = True
    #####
    ####
        pygame.init()
    def run(self):
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        while self.ultimateplaying == True:
            while self.intro == True and self.playing == False:
                clock.tick(self.fps)
                pygame.mixer.music.load("lv1.wav")
                pygame.mixer.music.play(-1)
                screen.blit(self.startingscreen,(0,0))
                pygame.draw.rect(screen, white, 
                            ((self.width*0.29,self.height*0.57), 
                            (self.width*0.45, self.height*0.25)), 0) 
                message("PUSH FOR GLORY", red, 10,"arialnarrow",screen, 
                        (self.width*0.55,self.height*0.6)) 
                intro_group.draw(screen)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if (startbuttonboundary(event.pos[0],event.pos[1],
                                            self.width,self.height)):
                            self.intro = False 
                            self.playing = True 
                        if event.type == pygame.QUIT:
                            self.ultimateplaying = False
                        if (event.pos[0] >= self.width*0.55 
                            and event.pos[0] <= self.width*0.55 + 50 
                            and event.pos[1] >= self.height*0.6 
                            and event.pos[1] <= self.height*0.6 + 50):
                            self.help = True 
                            self.intro = False
                pygame.display.flip()
            while self.playing == True and self.intro == False:
                clock.tick(self.fps)
                screen.fill((white))
                if self.jumponoff == False:
                    if self.screenchange != 0:
                        if self.moveleft == True:
                            self.screenchange = 4
                            self.questionChange = 4
                        if self.moveright == True:
                            self.screenchange = -4
                            self.questionChange = -4
                self.screenmove += self.screenchange
                self.questionPos += self.questionChange 
                self.questionmarkanimation += 1
                if self.questionmarkanimation == 28:
                    self.questionmarkanimation = 0 
                ######draw the items on the map######
                screen.blit(self.background,(self.screenmove,0))
                ################
                drawbrick(screen,self.brickimg,self.questionPos)
                drawtube(screen,self.tubeimg,self.questionPos,self.tubebottom)
                drawstairs(screen,self.stairimg, self.questionPos) 
                addstepon(screen,self.steponimg,self.questionPos)
                steponcollide = pygame.sprite.spritecollide(
                                player_group.sprites()[0], stepon_group,False)
                t = pygame.sprite.spritecollide(
                                player_group.sprites()[0], tube_group,False)
                b = pygame.sprite.spritecollide(
                                player_group.sprites()[0], brick_group,False)
                stairs = pygame.sprite.spritecollide(
                                player_group.sprites()[0],stair_group, False)
                animal1 = pygame.sprite.spritecollide(
                                player_group.sprites()[0], animal_group1,False)
                for thing in self.question1:
                    if self.boxanimationswitch1 == False:
                        thing.setpos(self.questionChange, 0) 
                    else:
                        if self.storequestionx1 != None and self.storequestiony1 != None:
                            if thing.info()[0] == self.storequestionx1:
                                thing.setpos(self.questionChange, self.questiony1) 
                                if (abs(thing.info()[1] - self.storequestiony1) > 1
                                    and thing.info()[1] < self.storequestiony1):
                                    self.questiony1 = 1
                                    if thing not in mushroom_group:
                                        self.coinanimation = True 
                                        self.coinx = self.storequestionx1
                                        self.coiny = self.storequestiony1
                                    if thing in mushroom_group1:
                                        self.mushroomanimation1 = True 
                                        self.mushroomx1 = self.storequestionx1 
                                        self.mushroomy1 = self.storequestiony1
                                        self.mushroomchangey1 = -1
                                    if thing in mushroom_group2:
                                        self.mushroomanimation2 = True 
                                        self.mushroomx2 = self.storequestionx1 
                                        self.mushroomy2 = self.storequestiony1
                                        self.mushroomchangey2 = -1
                                    if thing in mushroom_group3:
                                        self.mushroomanimation3 = True 
                                        self.mushroomx3 = self.storequestionx1 
                                        self.mushroomy3 = self.storequestiony1
                                        self.mushroomchangey3 = -1
                                if thing.info()[1] == self.storequestiony1:
                                    self.question1.remove(thing) 
                                    self.storegarbage.add(emptybox(self.empty_box,
                                        self.storequestionx1,self.storequestiony1))
                                    self.storequestionx1 = None
                                    self.storequestiony1 = None 
                                    self.questiony1 = -1
                                    self.boxanimationswitch1 = False
                            else:
                                thing.setpos(self.questionChange, 0)
                for thing in self.question2:
                    if self.boxanimationswitch2 == False:
                        thing.setpos(self.questionChange, 0) 
                    else:
                        if self.storequestionx2 != None and self.storequestiony2 != None:
                            if thing.info()[0] == self.storequestionx2:
                                thing.setpos(self.questionChange, self.questiony2) 
                                if (abs(thing.info()[1] - self.storequestiony2) > 1 
                                    and thing.info()[1] < self.storequestiony2):
                                    self.questiony2 = 1
                                    if thing not in mushroom_group:
                                        self.coinanimation = True 
                                        self.coinx = self.storequestionx2
                                        self.coiny = self.storequestiony2
                                    if thing in mushroom_group1:
                                        self.mushroomanimation1 = True 
                                        self.mushroomx1 = self.storequestionx2          
                                        self.mushroomy1 = self.storequestiony2
                                        self.mushroomchangey1 = -1
                                    if thing in mushroom_group2:
                                        self.mushroomanimation2 = True 
                                        self.mushroomx2 = self.storequestionx2 
                                        self.mushroomy2 = self.storequestiony2
                                        self.mushroomchangey2 = -1
                                    if thing in mushroom_group3:
                                        self.mushroomanimation3 = True 
                                        self.mushroomx3 = self.storequestionx2 
                                        self.mushroomy3 = self.storequestiony2
                                        self.mushroomchangey3 = -1
                                if thing.info()[1] == self.storequestiony2:
                                    self.question2.remove(thing) 
                                    self.storegarbage.add(emptybox(self.empty_box,
                                                    self.storequestionx2,self.storequestiony2))
                                    self.storequestionx2 = None
                                    self.storequestiony2 = None 
                                    self.questiony2 = -1
                                    self.boxanimationswitch2 = False 
                            else:
                                thing.setpos(self.questionChange, 0)
                for thing in self.question3:
                    if self.boxanimationswitch3 == False:
                        thing.setpos(self.questionChange, 0) 
                    else:
                        if self.storequestionx3 != None and self.storequestiony3 != None:
                            if thing.info()[0] == self.storequestionx3:
                                thing.setpos(self.questionChange, self.questiony3) 
                                if (abs(thing.info()[1] - self.storequestiony3) > 1 
                                    and thing.info()[1] < self.storequestiony3):
                                    self.questiony3 = 1
                                    if thing not in mushroom_group:
                                        self.coinanimation = True 
                                        self.coinx = self.storequestionx3
                                        self.coiny = self.storequestiony3
                                    if thing in mushroom_group1:
                                        self.mushroomanimation1 = True 
                                        self.mushroomx1 = self.storequestionx3              
                                        self.mushroomy1 = self.storequestiony3      
                                        self.mushroomchangey1 = -1
                                    if thing in mushroom_group2:
                                        self.mushroomanimation2 = True 
                                        self.mushroomx2 = self.storequestionx3
                                        self.mushroomy2 = self.storequestiony3
                                        self.mushroomchangey2 = -1
                                    if thing in mushroom_group3:
                                        self.mushroomanimation3 = True 
                                        self.mushroomx3 = self.storequestionx3 
                                        self.mushroomy3 = self.storequestiony3
                                        self.mushroomchangey3 = -1
                                if thing.info()[1] == self.storequestiony3:
                                    self.question3.remove(thing) 
                                    self.storegarbage.add(emptybox(self.empty_box,self.storequestionx3,self.storequestiony3))
                                    self.storequestionx3 = None
                                    self.storequestiony3 = None 
                                    self.questiony3 = -1 
                                    self.boxanimationswitch3 = False 
                            else:
                                thing.setpos(self.questionChange, 0)
                for thing in self.question4:
                    if self.boxanimationswitch4 == False:
                        thing.setpos(self.questionChange, 0) 
                    else:
                        if self.storequestionx4 != None and self.storequestiony4 != None:
                            if thing.info()[0] == self.storequestionx4:
                                thing.setpos(self.questionChange, self.questiony4) 
                                if (abs(thing.info()[1] - self.storequestiony4) > 1 
                                    and thing.info()[1] < self.storequestiony4):
                                    self.questiony4 = 1
                                    if thing not in mushroom_group:
                                        self.coinanimation = True 
                                        self.coinx = self.storequestionx4
                                        self.coiny = self.storequestiony4
                                    if thing in mushroom_group1:
                                        self.mushroomanimation1 = True 
                                        self.mushroomx1 = self.storequestionx4
                                        self.mushroomy1 = self.storequestiony4
                                        self.mushroomchangey1 = -1
                                    if thing in mushroom_group2:
                                        self.mushroomanimation2 = True 
                                        self.mushroomx2 = self.storequestionx4 
                                        self.mushroomy2 = self.storequestiony4
                                        self.mushroomchangey2 = -1
                                    if thing in mushroom_group3:
                                        self.mushroomanimation3 = True 
                                        self.mushroomx3 = self.storequestionx4 
                                        self.mushroomy3 = self.storequestiony4
                                        self.mushroomchangey3 = -1
                                if thing.info()[1] == self.storequestiony4:
                                    self.question4.remove(thing) 
                                    self.storegarbage.add(emptybox(self.empty_box,
                                                self.storequestionx4,self.storequestiony4))
                                    self.storequestionx4 = None
                                    self.storequestiony4 = None 
                                    self.questiony4 = -1 
                                    self.boxanimationswitch4 = False 
                            else:
                                thing.setpos(self.questionChange, 0) 
                if self.coinanimation == True:
                    coinanimation(screen, self.coinanimationcount, 
                                questionmarkimg, 0,self.coinx,self.coiny - 17)
                    self.coinanimationcount += 1
                    if self.coinanimationcount == 4:
                        self.coinanimation = False 
                        self.coinanimationcount = 0 
                if self.mushroomanimation1 == True:
                    mushroom1 = mushroomanim(self.mushroomimg[0], 
                                self.mushroomx1+255, self.mushroomy1,
                                self.questionPos, self.mushroommovex1, 
                                self.mushroommovey1) 
                    self.mushroommovey1 += self.mushroomchangey1
                    if mushroom1.info()[1] < self.mushroomy1 - 14:
                        self.mushroomchangey1 = 0
                        self.mushroomanimation1 = False
                        self.letmushgo1 = True 
                        self.mushroomchangex1 = 5
                    draw_mushroomgroup1.empty()
                    draw_mushroomgroup1.add(mushroom1)
                    draw_mushroomgroup1.draw(screen)
                if self.mushroomanimation1 == False and self.letmushgo1 == True:
                    mushroom1 = mushroomanim(self.mushroomimg[0], 
                                self.mushroomx1+255, self.mushroomy1-3,
                                self.questionPos, self.mushroommovex1, 
                                self.mushroommovey1)
                    mushques =  pygame.sprite.spritecollide(mushroom1, 
                                            questionmark_group, False) 
                    mushbrick =  pygame.sprite.spritecollide(mushroom1, 
                                            brick_group, False) 
                    mushflr = pygame.sprite.spritecollide(mushroom1, 
                                            stepon_group, False)
                    mushtub = pygame.sprite.spritecollide(mushroom1,
                                            tube_group, False)
                    if mushtub != []:
                        self.mushroomchangex1 = -5
                    if mushflr == [] and mushbrick == [] and mushques == []: 
                        self.mushroomchangey1 = 5  
                    else: self.mushroomchangey1 = 0  
                    if pygame.sprite.collide_rect(player_group.sprites()[0], mushroom1) == True:
                        if self.mushroom == False:
                            self.letmushgo1 = False
                            self.mushroomtransfanim = True
                            self.storemushroomy = self.mariomovey - 0.05
                        else:
                            self.score += 100 
                            self.letmushgo1 = False
                    self.mushroommovex1 += self.mushroomchangex1
                    self.mushroommovey1 += self.mushroomchangey1 
                    draw_mushroomgroup1.empty()
                    draw_mushroomgroup1.add(mushroom1)
                    draw_mushroomgroup1.draw(screen)
                    #####
                if self.mushroomanimation2 == True:
                    mushroom2 = mushroomanim(self.mushroomimg[0], 
                                    self.mushroomx2+1049, self.mushroomy2,
                                    self.questionPos, self.mushroommovex2, 
                                    self.mushroommovey2) 
                    self.mushroommovey2 += self.mushroomchangey2
                    if mushroom2.info()[1] < self.mushroomy2 - 14:
                        self.mushroomchangey2 = 0
                        self.mushroomanimation2 = False
                        self.letmushgo2 = True 
                        self.mushroomchangex2 = 5
                    draw_mushroomgroup2.empty()
                    draw_mushroomgroup2.add(mushroom2)
                    draw_mushroomgroup2.draw(screen)
                if self.mushroomanimation2 == False and self.letmushgo2 == True:
                    mushroom2 = mushroomanim(self.mushroomimg[0], 
                                self.mushroomx2+1049, self.mushroomy2-3,
                                self.questionPos, self.mushroommovex2, 
                                self.mushroommovey2)
                    mushques =  pygame.sprite.spritecollide(mushroom2, 
                                    questionmark_group, False) 
                    mushbrick =  pygame.sprite.spritecollide(mushroom2, 
                                    brick_group, False) 
                    mushflr = pygame.sprite.spritecollide(mushroom2, 
                                    stepon_group, False)
                    mushtub = pygame.sprite.spritecollide(mushroom2,
                                    tube_group, False)
                    if mushtub != []:
                        self.mushroomchangex2 = -5
                    if mushflr == [] and mushbrick == [] and mushques == []: 
                        self.mushroomchangey2 = 5  
                    else: self.mushroomchangey2 = 0  
                    if (mushflr == [] and mushbrick == [] and mushques == [] 
                        and mushroom2.info()[1] > 0.840*self.height):
                        self.mushroomchangex2 = 0 
                    if pygame.sprite.collide_rect(player_group.sprites()[0], mushroom2) == True:
                        if self.mushroom == False:
                            self.letmushgo2 = False
                            self.mushroomtransfanim = True
                            self.storemushroomy = self.mariomovey - 0.05
                        else:
                            self.score += 100 
                            self.letmushgo2 = False
                    self.mushroommovex2 += self.mushroomchangex2
                    self.mushroommovey2 += self.mushroomchangey2 
                    draw_mushroomgroup2.empty()
                    draw_mushroomgroup2.add(mushroom2)
                    draw_mushroomgroup2.draw(screen)
                #####
                if self.mushroomanimation3 == True:
                    mushroom3 = mushroomanim(self.mushroomimg[0], 
                                        self.mushroomx3+2020, self.mushroomy3,
                                        self.questionPos, self.mushroommovex3, 
                                        self.mushroommovey3) 
                    self.mushroommovey3 += self.mushroomchangey3
                    if mushroom3.info()[1] < self.mushroomy3 - 14:
                        self.mushroomchangey3 = 0
                        self.mushroomanimation3 = False
                        self.letmushgo3 = True 
                        self.mushroomchangex3 = 5
                    draw_mushroomgroup3.empty()
                    draw_mushroomgroup3.add(mushroom3)
                    draw_mushroomgroup3.draw(screen)
                if self.mushroomanimation3 == False and self.letmushgo3 == True:
                    mushroom3 = mushroomanim(self.mushroomimg[0], 
                                            self.mushroomx3+2020, 
                                            self.mushroomy3-3,self.questionPos, 
                                            self.mushroommovex3, self.mushroommovey3)
                    mushques =  pygame.sprite.spritecollide(mushroom3, 
                                        questionmark_group, False) 
                    mushbrick =  pygame.sprite.spritecollide(mushroom3, 
                                        brick_group, False) 
                    mushflr = pygame.sprite.spritecollide(mushroom3, 
                                        stepon_group, False)
                    mushtub = pygame.sprite.spritecollide(mushroom3, 
                                        tube_group, False)
                    if mushtub != []:
                        self.mushroomchangex3 = -5
                    if mushflr == [] and mushbrick == [] and mushques == []: 
                        self.mushroomchangey3 = 5  
                    else: self.mushroomchangey3 = 0  
                    if (mushflr == [] and mushbrick == [] and mushques == [] 
                        and mushroom3.info()[1] > 0.840*self.height):
                        self.mushroomchangex3 = 0 
                    if pygame.sprite.collide_rect(player_group.sprites()[0], mushroom3) == True:
                        if self.mushroom == False:
                            self.letmushgo3 = False
                            self.mushroomtransfanim = True
                            self.storemushroomy = self.mariomovey - 0.05
                        else:
                            self.score += 100 
                            self.letmushgo3 = False
                    self.mushroommovex3 += self.mushroomchangex3
                    self.mushroommovey3 += self.mushroomchangey3 
                    draw_mushroomgroup3.empty()
                    draw_mushroomgroup3.add(mushroom3)
                    draw_mushroomgroup3.draw(screen)
            ######
                if self.mushroomtransfanim == True:
                    self.moveleft = False
                    self.moveright = False
                    self.jumpchange = 0 
                    self.mariochangex = 0 
                    self.mariomovey = self.storemushroomy
                    if self.mushroomtranscount >= 0 and self.mushroomtranscount <= 2:
                        screen.blit(self.mariobigright[15], 
                            (self.mariomovex*self.width, 
                            self.mariomovey*self.height)) 
                    if self.mushroomtranscount >= 3 and self.mushroomtranscount <= 5:
                        screen.blit(self.mariobigright[6], 
                            (self.mariomovex*self.width, 
                            self.mariomovey*self.height)) 
                    if self.mushroomtranscount >= 6 and self.mushroomtranscount <= 8:
                        screen.blit(self.mariotinyright[6], 
                            (self.mariomovex*self.width,
                             self.mariomovey*self.height)) 
                    if self.mushroomtranscount >= 9 and self.mushroomtranscount <= 11:
                        screen.blit(self.mariobigright[6], 
                            (self.mariomovex*self.width, 
                            self.mariomovey*self.height)) 
                    if self.mushroomtranscount >= 12 and self.mushroomtranscount <= 14:
                        screen.blit(self.mariobigright[15], 
                            (self.mariomovex*self.width, 
                            self.mariomovey*self.height)) 
                    if self.mushroomtranscount >= 15 and self.mushroomtranscount <= 17:
                        screen.blit(self.mariobigright[6], 
                            (self.mariomovex*self.width, 
                            self.mariomovey*self.height)) 
                    if self.mushroomtranscount >= 18 and self.mushroomtranscount <= 20:
                        screen.blit(self.mariobigright[15], 
                            (self.mariomovex*self.width, 
                            self.mariomovey*self.height)) 
                    self.mushroomtranscount += 1 
                    if self.mushroomtranscount == 21:
                        if self.jumponoff == True:
                            self.jumpchange = 0.03
                            self.jumpacceleration =0.00003
                        self.mushroomtranscount = 0 
                        self.mushroomtransfanim = False
                        self.mushroom = True
                    
                ######
                if len(self.storegarbage) != 0:
                    for gp in self.storegarbage:
                        gp.setpos(self.questionChange, 0)
                if len(self.storegarbage) != 0:
                    self.storegarbage.draw(screen)
                    gb = (pygame.sprite.spritecollide(player_group.sprites()[0], 
                            self.storegarbage, False))
                if self.questionmarkanimation >= 0 and self.questionmarkanimation <= 6:
                    self.question1.draw(screen)
                    q = (pygame.sprite.spritecollide(player_group.sprites()[0],
                            self.question1,False))
                if self.questionmarkanimation >= 7 and self.questionmarkanimation <= 13:
                    self.question2.draw(screen)
                    q = (pygame.sprite.spritecollide(player_group.sprites()[0], 
                            self.question2,False))
                if self.questionmarkanimation >= 14 and self.questionmarkanimation <= 20:
                    self.question3.draw(screen)
                    q = (pygame.sprite.spritecollide(player_group.sprites()[0], 
                            self.question3,False))
                if self.questionmarkanimation >= 21 and self.questionmarkanimation <= 27:
                    self.question4.draw(screen)
                    q = (pygame.sprite.spritecollide(player_group.sprites()[0],
                            self.question4,False))
                if len(self.storegarbage) == 0:
                    collidequestion = q + b + t + stairs
                else:
                    collidequestion = q + b + t + gb + stairs
                ####
                tog= pygame.image.load("/Users/EugeneLi/Desktop/tp/together.png")
                torect= tog.get_rect()
                xheart = 0
                for i in range(self.lives):
                    torect.x = xheart
                    torect.y = 5
                    screen.blit(tog,torect)
                    xheart += 30 
                message("Time: " + str(self.time), white, 20, 
                        "arialnarrow", screen, (100,0))
                message("TO BEAT: " + str(self.greatscore), 
                        white,20, "arialnarrow", screen, (290,0))
                message("SCORE: " + str(self.score), white, 
                        20,"arialnarrow", screen, (195,0))
                self.time -= 1
                if self.time == 0:
                    self.deathx= self.mariomovex
                    self.deathanimation = True
                    self.lives -= 1
                ####jumping#####
                self.jumpchange += self.jumpacceleration 
                self.mariomovey += self.jumpchange
                if (self.jumpkeyreleasebelow == True and 
                    self.mariomovey <= self.jumppeak + 0.15 
                    and self.mushroomtransfanim == False 
                    and self.mushroomawayanim == False): 
                    self.jumpacceleration = -(self.jumpacceleration) 
                    self.jumpchange = -(self.jumpchange)
                    self.jumpkeyreleasebelow = False 
                if (self.jumpkeyreleaseabove == True and 
                    self.mushroomtransfanim == False and 
                    self.mushroomawayanim == False):
                    self.jumpacceleration = -(self.jumpacceleration) 
                    self.jumpchange = -(self.jumpchange)
                    self.jumpkeyreleaseabove = False
                if (self.mariomovey < self.jumppeak and 
                    self.mushroomtransfanim == False and 
                    self.mushroomawayanim == False):
                    self.mariomovey = self.jumppeak
                    self.forcedown = True 
                    self.jumpacceleration = (0.00003) 
                    self.jumpchange = (0.03)
                    self.jumpkeyreleaseabove, self.jumpkeyreleasebelow = False, False
                for thing in collidequestion:
                    if (thing not in t and self.mushroomtransfanim == False 
                        and self.mushroomawayanim == False):
                        if ((thing.info()[1] + 7<=player_group.sprites()[0].info()[1] 
                            <= thing.info()[1] + 19) and 
                            (thing.info()[0]-13<= 
                            player_group.sprites()[0].info()[0] <=
                            thing.info()[0]+13 and self.justmark == False) 
                            and self.storeoldy > ((thing.info()[1]+14)/self.height) 
                            and animal1 == []):
                            #just for jumping from bottom to top
                            if (thing in self.question1 or 
                                thing in self.question2 or thing in 
                                self.question3 or thing in self.question4):
                                self.score += 100 
                                self.boxanimationswitch1 = True
                                self.storequestionx1 = thing.info()[0] 
                                self.storequestiony1 = thing.info()[1] 
                                self.boxanimationswitch2 = True
                                self.storequestionx2 = thing.info()[0]
                                self.storequestiony2 = thing.info()[1]
                                self.boxanimationswitch3 = True
                                self.storequestionx3 = thing.info()[0] 
                                self.storequestiony3 = thing.info()[1]
                                self.boxanimationswitch4 = True
                                self.storequestionx4 = thing.info()[0]
                                self.storequestiony4 = thing.info()[1]
                            self.mariomovey = ((thing.info()[1] + 17)/self.height)
                            self.forcedown = True 
                            self.jumpacceleration = (0.00003) 
                            self.jumpchange = (0.03)
                            self.jumpkeyreleaseabove, self.jumpkeyreleasebelow = False, False
                            self.sidewaypump = True
                for thing in collidequestion:
                    if (player_group.sprites()[0].info()[1] + 0.1 <= thing.info()[1] 
                        and self.differentplatform == False and animal1 == [] 
                        and self.mushroomtransfanim == False 
                        and self.mushroomawayanim == False):
                        self.differentplatform = True 
                        self.jumponoff = False
                        self.standingy = thing.info()[1]/self.height
                        self.jumppeak = (thing.info()[1]/self.height) - 0.34
                        self.ultimatestorey = thing.info()[1] 
                        self.forcedown = False
                        self.jumpkeyreleaseabove, self.jumpkeyreleasebelow = False, False
                        self.sidewaypump = True    
                        self.tubemark = False 
                if collidequestion == []:
                    self.sidewaypump = False 
                for thing in collidequestion:
                    if (thing.info()[1] == 120 and self.mushroomtransfanim == False 
                        and self.mushroomawayanim == False):
                        if (player_group.sprites()[0].info()[1] + 0.5 <= 
                            thing.info()[1] and animal1 == []):
                            self.jumponoff = False
                            self.standingy = thing.info()[1]/self.height
                            self.jumppeak = (thing.info()[1]/self.height) - 0.34
                            self.ultimatestorey = thing.info()[1] 
                            self.forcedown = False
                            self.jumpkeyreleaseabove, self.jumpkeyreleasebelow = False, False
                if self.mushroom == False:
                    if ((((self.mariomovey * self.height)+17)/self.height>= self.standingy) 
                        and (collidequestion != [] or steponcollide != [])):
                        self.mariomovey = ((self.standingy*self.height)-13)/self.height
                        self.jumponoff = False 
                        self.justmark = False 
                        self.forcedown = False
                        self.jumpacceleration = 0 
                        self.jumpchange = 0 
                        self.jumpkeyreleaseabove, self.jumpkeyreleasebelow = False, False
                if self.mushroom == True:
                    if ((((self.mariomovey * self.height)+30)/self.height>= self.standingy) 
                        and (collidequestion != [] or steponcollide != [])):
                        self.mariomovey = ((self.standingy*self.height)-28)/self.height
                        self.jumponoff = False 
                        self.justmark = False 
                        self.forcedown = False
                        self.jumpacceleration = 0 
                        self.jumpchange = 0 
                        self.jumpkeyreleaseabove, self.jumpkeyreleasebelow = False, False
                for thing in q:
                    if (thing.info()[1] < player_group.sprites()[0].info()[1] 
                        and abs(thing.info()[1] - 
                        player_group.sprites()[0].info()[1]) <= 2):
                        self.lives -= 1
                        self.deathanimation = True
                        self.deathx = self.mariomovex
    ################animal#########
                if self.screenmove <= -500:
                    self.screenswitch1 = True 
                if self.animal1switch == False and self.screenswitch1 == True:
                    collideanimal1 = pygame.sprite.spritecollide(player_group.sprites()[0], 
                                animal_group1, False)
                    if self.jumpchange <= -0.0305:
                        self.jumpacceleration = 0.0003
                        self.jumpchange = 0.03
                    if self.mushroom == False:
                        for thing in collideanimal1:
                            if self.animal1pause == False:
                                if (player_group.sprites()[0].info()[1] <= thing.info()[1]
                                and player_group.sprites()[0].info()[1] + 16 >= thing.info()[1] 
                                and self.jumponoff == True):
                                    self.mariomovey = (thing.info()[1] - 16)/self.height
                                    self.jumpacceleration = -0.0003
                                    self.score += 100
                                    self.jumpchange = -0.03
                                    self.animal1animation = -1 
                                    self.animal1pause = True
                                else:
                                    if self.mushroomawayanim != True and self.deathanimation == False:
                                        self.lives -= 1
                                        self.deathx = self.mariomovex
                                        self.deathanimation = True
                    if self.mushroom == True:
                        for thing in collideanimal1:
                            if self.animal1pause == False:
                                if (player_group.sprites()[0].info()[1] <= thing.info()[1]
                                    and (player_group.sprites()[0].info()[1] + 32 >= thing.info()[1])
                                    and self.jumponoff == True):
                                    self.mariomovey = (thing.info()[1] - 32)/self.height
                                    self.jumpacceleration = -0.0003
                                    self.jumpchange = -0.03
                                    self.animal1animation = -1 
                                    self.animal1pause = True
                                else:
                                    if self.mushroomawayanim == False:
                                        self.mushroomawayanim = True
                                        self.storemariomonstery = self.mariomovey
                    if self.animal1pause == True:
                        self.animal1pausecount += 1 
                    if self.animal1pausecount >= 10:
                        self.animal1switch = True
                    if self.animal1animation != -1:
                        self.animalmove1 += self.animalchange1
                    for thing in animal_group1: 
                        if pygame.sprite.spritecollide(thing,tube_group, False):
                            if self.animalchange1 > 0:
                                self.animalmove1 -= 7
                            if self.animalchange1 < 0:
                                self.animalmove1 += 7
                            self.animalchange1 = -self.animalchange1
                    if self.animal1animation >= 4: 
                        self.animal1animation = 0 
                    if self.animal1animation%2 == 0 and self.animal1animation >= 0:
                        drawanimal1(screen,self.enemy[0],
                                    self.questionPos,self.animalmove1,
                                    890,255,animal_group1)
                    if self.animal1animation%2 != 0 and self.animal1animation >= 0:
                        drawanimal1(screen,self.enemy[1],
                                    self.questionPos,self.animalmove1,
                                    890,255,animal_group1)
                    if self.animal1animation == -1:
                        drawanimal1(screen,self.enemy[2],
                                    self.questionPos,self.animalmove1,
                                    890,255,animal_group1)
                    if self.animal1animation != -1:
                        self.animal1animation += 1 
                #####
                if self.screenmove <= -100:
                    self.screenswitch2 = True 
                if self.animalswitch2 == False and self.screenswitch2 == True :
                    collideanimal2 = pygame.sprite.spritecollide(player_group.sprites()[0], 
                                animal_group2, False)
                    if self.jumpchange <= -0.0305:
                        self.jumpacceleration = 0.0003
                        self.jumpchange = 0.03
                    if self.mushroom == False:
                        for thing in collideanimal2:
                            if self.animalpause2 == False:
                                if (player_group.sprites()[0].info()[1] <= thing.info()[1]
                                    and player_group.sprites()[0].info()[1] + 16 >= thing.info()[1] 
                                    and self.jumponoff == True):
                                    self.mariomovey = (thing.info()[1] - 16)/self.height
                                    self.score += 100
                                    self.jumpacceleration = -0.0003
                                    self.jumpchange = -0.03
                                    self.animalanimation2 = -1 
                                    self.animalpause2 = True
                                else:
                                    if self.mushroomawayanim != True and self.deathanimation == False:
                                        self.lives -= 1
                                        self.deathx = self.mariomovex
                                        self.deathanimation = True
                    if self.mushroom == True:
                        for thing in collideanimal2:
                            if self.animalpause2 == False:
                                if (player_group.sprites()[0].info()[1] <= thing.info()[1]
                                    and player_group.sprites()[0].info()[1] + 32 >= thing.info()[1] 
                                    and self.jumponoff == True):
                                    self.mariomovey = (thing.info()[1] - 32)/self.height
                                    self.score += 100
                                    self.jumpacceleration = -0.0003
                                    self.jumpchange = -0.03
                                    self.animalanimation2 = -1 
                                    self.animalpause2 = True
                                else:
                                    if self.mushroomawayanim == False:
                                        self.mushroomawayanim = True
                                        self.storemariomonstery = self.mariomovey
                    if self.animalpause2 == True:
                        self.animalpausecount2 += 1 
                    if self.animalpausecount2 >= 10:
                        self.animalswitch2 = True
                    if self.animalanimation2 != -1:
                        self.animalmove2 -= self.animalchange2
                    if self.animalanimation2 >= 4: 
                        self.animalanimation2 = 0 
                    if self.animalanimation2%2 == 0 and self.animalanimation2>= 0:
                        drawanimal1(screen,self.enemy[0],
                                self.questionPos,self.animalmove2,
                                603,255,animal_group2)
                    if self.animalanimation2%2 != 0 and self.animalanimation2 >= 0:
                        drawanimal1(screen,self.enemy[1],self.questionPos,
                                    self.animalmove2,603,255,animal_group2)
                    if self.animalanimation2 == -1:
                        drawanimal1(screen,self.enemy[2],self.questionPos,
                                self.animalmove2,603,255,animal_group2)
                    if self.animalanimation2 != -1:
                        self.animalanimation2 += 1 
                ###
                if self.screenmove <= -700:
                    self.screenswitch3 = True 
                if self.animalswitch3 == False and self.screenswitch3 == True :
                    collideanimal3 = pygame.sprite.spritecollide(player_group.sprites()[0], 
                                animal_group3, False)
                    if self.jumpchange <= -0.0305:
                        self.jumpacceleration = 0.0003
                        self.jumpchange = 0.03
                    if self.mushroom == False:
                        for thing in collideanimal3:
                            if self.animalpause3 == False:
                                if (player_group.sprites()[0].info()[1] <= thing.info()[1]
                                    and player_group.sprites()[0].info()[1] + 16 >= thing.info()[1] 
                                    and self.jumponoff == True):
                                    self.mariomovey = (thing.info()[1] - 16)/self.height
                                    self.jumpacceleration = -0.0003
                                    self.score += 100
                                    self.jumpchange = -0.03
                                    self.animalanimation3 = -1 
                                    self.animalpause3 = True
                                else:
                                    if (self.mushroomawayanim != True and 
                                        self.deathanimation == False):
                                        self.lives -= 1
                                        self.deathx = self.mariomovex
                                        self.deathanimation = True
                    if self.mushroom == True:
                        for thing in collideanimal3:
                            if self.animalpause3 == False:
                                if (player_group.sprites()[0].info()[1] <= thing.info()[1]
                                    and player_group.sprites()[0].info()[1] + 32 >= thing.info()[1] 
                                    and self.jumponoff == True):
                                    self.mariomovey = (thing.info()[1] - 32)/self.height
                                    self.jumpacceleration = -0.0003
                                    self.score += 100
                                    self.jumpchange = -0.03
                                    self.animalanimation3 = -1 
                                    self.animalpause3 = True
                                else:
                                    if self.mushroomawayanim == False:
                                        self.mushroomawayanim = True
                                        self.storemariomonstery = self.mariomovey
                    if self.animalpause3 == True:
                        self.animalpausecount3 += 1 
                    if self.animalpausecount3 >= 10:
                        animal_group3.empty()
                        self.animalswitch3 = True
                    if self.animalanimation3 != -1:
                        self.animalmove3 -= self.animalchange3
                    for thing in animal_group3: 
                        if pygame.sprite.spritecollide(thing,tube_group, False):
                            if self.animalchange3 > 0:
                                self.animalmove3 += 7
                                self.animalmove4 += 7
                            if self.animalchange3 < 0:
                                self.animalmove3 -= 7
                                self.animalmove4 -= 7
                            self.animalchange3 = -self.animalchange3
                            self.animalchange4 = -self.animalchange4
                    if self.animalanimation3 >= 4: 
                        self.animalanimation3 = 0 
                    if self.animalanimation3%2 == 0 and self.animalanimation3>= 0:
                        drawanimal1(screen,self.enemy[0],self.questionPos,
                                    self.animalmove3,1150,255,animal_group3)
                    if self.animalanimation3%2 != 0 and self.animalanimation3 >= 0:
                        drawanimal1(screen,self.enemy[1],self.questionPos,
                                    self.animalmove3,1150,255,animal_group3)
                    if self.animalanimation3 == -1:
                        drawanimal1(screen,self.enemy[2],self.questionPos,
                                    self.animalmove3,1150,255,animal_group3)
                    if self.animalanimation3 != -1:
                        self.animalanimation3 += 1 
            #####
                if self.screenmove <= -700: 
                    self.screenswitch4 = True 
                if self.animalswitch4 == False and self.screenswitch4 == True :
                    collideanimal4 = pygame.sprite.spritecollide(player_group.sprites()[0], 
                                animal_group4, False)
                    if self.jumpchange <= -0.0305:
                        self.jumpacceleration = 0.0003
                        self.jumpchange = 0.03
                    if self.mushroom == False:
                        for thing in collideanimal4:
                            if self.animalpause4 == False:
                                if (player_group.sprites()[0].info()[1] <= thing.info()[1]
                                    and player_group.sprites()[0].info()[1] + 16 >= thing.info()[1] 
                                    and self.jumponoff == True):
                                    self.mariomovey = (thing.info()[1] - 16)/self.height
                                    self.jumpacceleration = -0.0003
                                    self.score += 100
                                    self.jumpchange = -0.03
                                    self.animalanimation4 = -1 
                                    self.animalpause4 = True
                                else:
                                    if self.mushroomawayanim != True and self.deathanimation == False:
                                        self.lives -= 1
                                        self.deathx = self.mariomovex
                                        self.deathanimation = True
                    if self.mushroom == True:
                        for thing in collideanimal4:
                            if self.animalpause4 == False:
                                if (player_group.sprites()[0].info()[1] <= thing.info()[1]
                                    and player_group.sprites()[0].info()[1] + 32 >= thing.info()[1] 
                                    and self.jumponoff == True):
                                    self.mariomovey = (thing.info()[1] - 32)/self.height
                                    self.jumpacceleration = -0.0003
                                    self.score += 100
                                    self.jumpchange = -0.03
                                    self.animalanimation4 = -1 
                                    self.animalpause4 = True
                                else:
                                    if self.mushroomawayanim == False:
                                        self.mushroomawayanim = True
                                        self.storemariomonstery = self.mariomovey
                    if self.animalpause4 == True:
                        self.animalpausecount4 += 1 
                    if self.animalpausecount4 >= 10:
                        animal_group4.empty()
                        self.animalswitch4 = True
                    if self.animalanimation4 != -1:
                        self.animalmove4 -= self.animalchange4
                    for thing in animal_group4: 
                        if pygame.sprite.spritecollide(thing,tube_group, False):
                            if self.animalchange4 < 0:
                                self.animalmove4 -= 7
                                self.animalmove3 -= 7
                            if self.animalchange4 > 0:
                                self.animalmove4 += 7
                                self.animalmove3 += 7
                            self.animalchange3 = -self.animalchange3
                            self.animalchange4 = -self.animalchange4
                    if self.animalanimation4 >= 4: 
                        self.animalanimation4 = 0 
                    if self.animalanimation4%2 == 0 and self.animalanimation4>= 0:
                        drawanimal1(screen,self.enemy[0],
                            self.questionPos,self.animalmove4,
                            1120,255,animal_group4)
                    if self.animalanimation4%2 != 0 and self.animalanimation4 >= 0:
                        drawanimal1(screen,self.enemy[1],
                            self.questionPos,self.animalmove4,
                            1120,255,animal_group4)
                    if self.animalanimation4 == -1:
                        drawanimal1(screen,self.enemy[2],
                            self.questionPos,self.animalmove4,
                            1120,255,animal_group4)
                    if self.animalanimation4 != -1:
                        self.animalanimation4 += 1 
                ####
                if self.screenmove <= -1690:               
                    self.screenswitch5 = True 
                if self.animalswitch5 == False and self.screenswitch5 == True :
                    collideanimal5 = pygame.sprite.spritecollide(player_group.sprites()[0], 
                                animal_group5, False)
                    if self.jumpchange <= -0.0305:
                        self.jumpacceleration = 0.0003
                        self.jumpchange = 0.03
                    if self.mushroom == False:
                        for thing in collideanimal5:
                            if self.animalpause5 == False:
                                if (player_group.sprites()[0].info()[1] <= thing.info()[1]
                                    and player_group.sprites()[0].info()[1] + 16 >= thing.info()[1] 
                                    and self.jumponoff == True):
                                    self.mariomovey = (thing.info()[1] - 16)/self.height
                                    self.jumpacceleration = -0.0003
                                    self.score += 100
                                    self.jumpchange = -0.03
                                    self.animalanimation5 = -1 
                                    self.animalpause5 = True
                                else:
                                    if self.mushroomawayanim != True and self.deathanimation == False:
                                        self.lives -= 1
                                        self.deathx = self.mariomovex
                                        self.deathanimation = True
                    if self.mushroom == True:
                        for thing in collideanimal5:
                            if self.animalpause5 == False:
                                if (player_group.sprites()[0].info()[1] <= thing.info()[1]
                                    and player_group.sprites()[0].info()[1] + 32 >= thing.info()[1] 
                                    and self.jumponoff == True):
                                    self.mariomovey = (thing.info()[1] - 32)/self.height
                                    self.jumpacceleration = -0.0003
                                    self.score += 100
                                    self.jumpchange = -0.03
                                    self.animalanimation5 = -1 
                                    self.animalpause5 = True
                                else:
                                    if self.mushroomawayanim == False:
                                        self.mushroomawayanim = True
                                        self.storemariomonstery = self.mariomovey
                    if self.animalpause5 == True:
                        self.animalpausecount5 += 1 
                    if self.animalpausecount5 >= 10:
                        self.animalswitch5 = True
                    if self.animalanimation5 != -1:
                        self.animalmove5 -= self.animalchange5
                    if self.animalanimation5 >= 4: 
                        self.animalanimation5 = 0 
                    if self.animalanimation5%2 == 0 and self.animalanimation5 >= 0:
                        drawanimal2(screen,self.enemy[0],
                            self.questionPos,self.animalmove5,
                            2300,255,animal_group5,self.animaly5)
                    if self.animalanimation5%2 != 0 and self.animalanimation5 >= 0:
                        drawanimal2(screen,self.enemy[1],
                            self.questionPos,self.animalmove5,2300,255,
                            animal_group5,self.animaly5)
                    if self.animalanimation5 == -1:
                        drawanimal2(screen,self.enemy[2],self.questionPos,
                            self.animalmove5,2300,255,animal_group5,self.animaly5)
                    collideanimalfloor5 = pygame.sprite.spritecollide(animal_group5.sprites()[0],
                                            stepon_group, False)
                    if collideanimalfloor5 == []:
                        self.animaly5 += 10
                        self.animalchange5 = 0
                    if self.animalanimation5 != -1:
                        self.animalanimation5 += 1
                ###
                if self.screenmove <= -1690:            
                    self.screenswitch6 = True 
                if self.animalswitch6 == False and self.screenswitch6 == True :
                    collideanimal6 = pygame.sprite.spritecollide(player_group.sprites()[0],
                                animal_group6, False)
                    if self.jumpchange <= -0.0305:
                        self.jumpacceleration = 0.0003
                        self.jumpchange = 0.03
                    if self.mushroom == False:
                        for thing in collideanimal6:
                            if self.animalpause6 == False:
                                if (player_group.sprites()[0].info()[1] <= thing.info()[1]
                                    and player_group.sprites()[0].info()[1] + 16 >= thing.info()[1] 
                                    and self.jumponoff == True):
                                    self.mariomovey = (thing.info()[1] - 16)/self.height
                                    self.jumpacceleration = -0.0003
                                    self.score += 100
                                    self.jumpchange = -0.03
                                    self.animalanimation6 = -1 
                                    self.animalpause6 = True
                                else:
                                    if self.mushroomawayanim != True and self.deathanimation == False:
                                        self.lives -= 1
                                        self.deathx = self.mariomovex
                                        self.deathanimation = True
                    if self.mushroom == True:
                        for thing in collideanimal6:
                            if self.animalpause6 == False:
                                if (player_group.sprites()[0].info()[1] <= thing.info()[1]
                                    and player_group.sprites()[0].info()[1] + 32 >= thing.info()[1] 
                                    and self.jumponoff == True):
                                    self.mariomovey = (thing.info()[1] - 32)/self.height
                                    self.jumpacceleration = -0.0003
                                    self.score += 100
                                    self.jumpchange = -0.03
                                    self.animalanimation6 = -1 
                                    self.animalpause6 = True
                                else:
                                    if self.mushroomawayanim == False:
                                        self.mushroomawayanim = True
                                        self.storemariomonstery = self.mariomovey
                    if self.animalpause6 == True:
                        self.animalpausecount6 += 1 
                    if self.animalpausecount6 >= 10:
                        self.animalswitch6 = True
                    if self.animalanimation6 != -1:
                        self.animalmove6 -= self.animalchange6
                    if self.animalanimation6 >= 4: 
                        self.animalanimation6 = 0 
                    if self.animalanimation6%2 == 0 and self.animalanimation6 >= 0:
                        drawanimal2(screen,self.enemy[0],
                                self.questionPos,self.animalmove6,
                                2330,255,animal_group6,self.animaly6)
                    if self.animalanimation6%2 != 0 and self.animalanimation6 >= 0:
                        drawanimal2(screen,self.enemy[1],self.questionPos,
                                    self.animalmove6,2330,255,animal_group6,
                                    self.animaly6)
                    if self.animalanimation6 == -1:
                        drawanimal2(screen,self.enemy[2],self.questionPos,
                                    self.animalmove6,2330,255,animal_group6,
                                    self.animaly6)
                    collideanimalfloor6 = pygame.sprite.spritecollide(animal_group6.sprites()[0],
                                        stepon_group, False)
                    if collideanimalfloor6 == []:
                        self.animaly6 += 10
                        self.animalchange6 = 0
                    if self.animalanimation6 != -1:
                        self.animalanimation6 += 1
                        ########
                if self.screenmove <= -1800:                
                    self.screenswitch7 = True 
                if self.animalswitch7 == False and self.screenswitch7 == True :
                    collideanimal7 = pygame.sprite.spritecollide(player_group.sprites()[0],
                                animal_group7, False)
                    if self.jumpchange <= -0.0305:
                        self.jumpacceleration = 0.0003
                        self.jumpchange = 0.03
                    if self.mushroom == False:
                        for thing in collideanimal7:
                            if self.animalpause7 == False:
                                if (player_group.sprites()[0].info()[1] <= thing.info()[1]
                                    and player_group.sprites()[0].info()[1] + 16 >= thing.info()[1] 
                                    and self.jumponoff == True):
                                    self.mariomovey = (thing.info()[1] - 16)/self.height
                                    self.jumpacceleration = -0.0003
                                    self.score += 100
                                    self.jumpchange = -0.03
                                    self.animalanimation7 = -1 
                                    self.animalpause7 = True
                                else:
                                    if self.mushroomawayanim != True and self.deathanimation == False:
                                        self.lives -= 1
                                        self.deathx = self.mariomovex
                                        self.deathanimation = True
                    if self.mushroom == True:
                        for thing in collideanimal7:
                            if self.animalpause7 == False:
                                if (player_group.sprites()[0].info()[1] <= thing.info()[1]
                                    and player_group.sprites()[0].info()[1] + 32 >= thing.info()[1] 
                                    and self.jumponoff == True):
                                    self.mariomovey = (thing.info()[1] - 32)/self.height
                                    self.jumpacceleration = -0.0003
                                    self.score += 100
                                    self.jumpchange = -0.03
                                    self.animalanimation7 = -1 
                                    self.animalpause7 = True
                                else:
                                    if self.mushroomawayanim == False:
                                        self.mushroomawayanim = True
                                        self.storemariomonstery = self.mariomovey
                    if self.animalpause7 == True:
                        self.animalpausecount7 += 1 
                    if self.animalpausecount7 >= 10:
                        self.animalswitch7 = True
                    if self.animalanimation7 != -1:
                        self.animalmove7 -= self.animalchange7
                    if self.animalanimation7 >= 4: 
                        self.animalanimation7 = 0 
                    if self.animalanimation7%2 == 0 and self.animalanimation7 >= 0:
                        drawanimal2(screen,self.enemy[0],self.questionPos,
                                    self.animalmove7,2600,255,animal_group7,
                                    self.animaly7)
                    if self.animalanimation7%2 != 0 and self.animalanimation7 >= 0:
                        drawanimal2(screen,self.enemy[1],self.questionPos,
                                    self.animalmove7,2600,255,animal_group7,
                                    self.animaly7)
                    if self.animalanimation7 == -1:
                        drawanimal2(screen,self.enemy[2],self.questionPos,
                                    self.animalmove7,2600,255,animal_group7,
                                    self.animaly7)
                    collideanimalfloor7 = pygame.sprite.spritecollide(animal_group7.sprites()[0],
                                        stepon_group, False)
                    if collideanimalfloor7 == []:
                        self.animaly7 += 10
                        self.animalchange7 = 0
                    if self.animalanimation7 != -1:
                        self.animalanimation7 += 1
                        ######
                if self.screenmove <= -1800:           
                    self.screenswitch8 = True 
                if self.animalswitch8 == False and self.screenswitch8 == True :
                    collideanimal8 = pygame.sprite.spritecollide(player_group.sprites()[0], 
                                    animal_group8, False)
                    if self.jumpchange <= -0.0305:
                        self.jumpacceleration = 0.0003
                        self.jumpchange = 0.03
                    if self.mushroom == False:
                        for thing in collideanimal8:
                            if self.animalpause8 == False:
                                if (player_group.sprites()[0].info()[1] <= thing.info()[1]
                                    and player_group.sprites()[0].info()[1] + 16 >= thing.info()[1] 
                                    and self.jumponoff == True):
                                    self.mariomovey = (thing.info()[1] - 16)/self.height
                                    self.jumpacceleration = -0.0003
                                    self.score += 100
                                    self.jumpchange = -0.03
                                    self.animalanimation8 = -1 
                                    self.animalpause8 = True
                                else:
                                    if self.mushroomawayanim != True and self.deathanimation == False:
                                        self.lives -= 1
                                        self.deathx = self.mariomovex
                                        self.deathanimation = True
                    if self.mushroom == True:
                        for thing in collideanimal8:
                            if self.animalpause8 == False:
                                if (player_group.sprites()[0].info()[1] <= thing.info()[1]
                                    and player_group.sprites()[0].info()[1] + 32>= thing.info()[1] 
                                    and self.jumponoff == True):
                                    self.mariomovey = (thing.info()[1] - 32)/self.height
                                    self.jumpacceleration = -0.0003
                                    self.score += 100
                                    self.jumpchange = -0.03
                                    self.animalanimation8 = -1 
                                    self.animalpause8 = True
                                else:
                                    if self.mushroomawayanim == False:
                                        self.mushroomawayanim = True
                                        self.storemariomonstery = self.mariomovey
                    if self.animalpause8 == True:
                        self.animalpausecount8 += 1 
                    if self.animalpausecount8 >= 10:
                        self.animalswitch8 = True
                    if self.animalanimation8 != -1:
                        self.animalmove8 -= self.animalchange8
                    if self.animalanimation8 >= 4: 
                        self.animalanimation8 = 0 
                    if self.animalanimation8%2 == 0 and self.animalanimation8 >= 0:
                        drawanimal2(screen,self.enemy[0],self.questionPos,
                                self.animalmove8,2630,255,animal_group8,
                                self.animaly8)
                    if self.animalanimation8%2 != 0 and self.animalanimation8 >= 0:
                        drawanimal2(screen,self.enemy[1],self.questionPos,
                                self.animalmove8,2630,255,animal_group8,
                                self.animaly8)
                    if self.animalanimation8 == -1:
                        drawanimal2(screen,self.enemy[2],
                                self.questionPos,self.animalmove8,
                                2630,255,animal_group8,self.animaly8)
                    collideanimalfloor8 = pygame.sprite.spritecollide(animal_group8.sprites()[0],
                                    stepon_group, False)
                    if collideanimalfloor8 == []:
                        self.animaly8 += 10
                        self.animalchange8 = 0
                    if self.animalanimation8 != -1:
                        self.animalanimation8 += 1
                        ####
                if self.screenmove <= -1800:     
                    self.screenswitch9 = True 
                if self.animalswitch9 == False and self.screenswitch9 == True : 
                    collideanimal9 = pygame.sprite.spritecollide(player_group.sprites()[0], 
                                animal_group9, False)
                    if self.jumpchange <= -0.0305:
                        self.jumpacceleration = 0.0003
                        self.jumpchange = 0.03
                    if self.mushroom == False:
                        for thing in collideanimal9:
                            if self.animalpause9 == False:
                                if (player_group.sprites()[0].info()[1] <= thing.info()[1]
                                    and player_group.sprites()[0].info()[1] + 16 >= thing.info()[1]
                                    and self.jumponoff == True):
                                    self.mariomovey = (thing.info()[1] - 16)/self.height
                                    self.jumpacceleration = -0.0003
                                    self.score += 100
                                    self.jumpchange = -0.03
                                    self.animalanimation9 = -1 
                                    self.animalpause9 = True
                                else:
                                    if self.mushroomawayanim != True and self.deathanimation == False:
                                        self.lives -= 1
                                        self.deathx = self.mariomovex
                                        self.deathanimation = True
                    if self.mushroom == True:
                        for thing in collideanimal9:
                            if self.animalpause9 == False:
                                if (player_group.sprites()[0].info()[1] <= thing.info()[1]
                                    and player_group.sprites()[0].info()[1] + 32 >= thing.info()[1] 
                                    and self.jumponoff == True):
                                    self.mariomovey = (thing.info()[1] - 32)/self.height
                                    self.jumpacceleration = -0.0003
                                    self.score += 100
                                    self.jumpchange = -0.03
                                    self.animalanimation9 = -1 
                                    self.animalpause9 = True
                                else:
                                    if self.mushroomawayanim == False:
                                        self.mushroomawayanim = True
                                        self.storemariomonstery = self.mariomovey
                    if self.animalpause9 == True:
                        self.animalpausecount9 += 1 
                    if self.animalpausecount9 >= 10:
                        self.animalswitch9 = True
                    if self.animalanimation9 != -1:
                        self.animalmove9 -= self.animalchange9
                    if self.animalanimation9 >= 4: 
                        self.animalanimation9 = 0 
                    if self.animalanimation9%2 == 0 and self.animalanimation9 >= 0:
                        drawanimal2(screen,self.enemy[0],self.questionPos,
                                    self.animalmove9,2660,255,animal_group9,
                                    self.animaly9)
                    if self.animalanimation9%2 != 0 and self.animalanimation9 >= 0:
                        drawanimal2(screen,self.enemy[1],self.questionPos,
                                    self.animalmove9,2660,255,animal_group9,
                                    self.animaly9)
                    if self.animalanimation9 == -1:
                        drawanimal2(screen,self.enemy[2],self.questionPos,
                                    self.animalmove9,2660,255,animal_group9,
                                    self.animaly9)
                    collideanimalfloor9 = pygame.sprite.spritecollide(animal_group9.sprites()[0],
                                    stepon_group, False)
                    if collideanimalfloor9 == []:
                        self.animaly9 += 10
                        self.animalchange9 = 0
                    if self.animalanimation9 != -1:
                        self.animalanimation9 += 1
                        #####
                if self.screenmove <= -1800:         
                    self.screenswitch10 = True 
                if self.animalswitch10 == False and self.screenswitch10 == True :
                    collideanimal10 = pygame.sprite.spritecollide(player_group.sprites()[0], 
                                    animal_group10, False)
                    if self.jumpchange <= -0.0305:
                        self.jumpacceleration = 0.0003
                        self.jumpchange = 0.03
                    if self.mushroom == False:
                        for thing in collideanimal10:
                            if self.animalpause10 == False:
                                if (player_group.sprites()[0].info()[1] <= thing.info()[1]
                                    and player_group.sprites()[0].info()[1] + 16 >= thing.info()[1] 
                                    and self.jumponoff == True):
                                    self.mariomovey = (thing.info()[1] - 16)/self.height
                                    self.jumpacceleration = -0.0003
                                    self.score += 100
                                    self.jumpchange = -0.03
                                    self.animalanimation10 = -1 
                                    self.animalpause10 = True
                                else:
                                    if self.mushroomawayanim != True and self.deathanimation == False:
                                        self.lives -= 1
                                        self.deathx = self.mariomovex
                                        self.deathanimation = True
                    if self.mushroom == True:
                        for thing in collideanimal10:
                            if self.animalpause10 == False:
                                if (player_group.sprites()[0].info()[1] <= thing.info()[1]
                                    and player_group.sprites()[0].info()[1] + 16 >= thing.info()[1] 
                                    and self.jumponoff == True):
                                    self.mariomovey = (thing.info()[1] - 16)/self.height
                                    self.score += 100
                                    self.jumpacceleration = -0.0003
                                    self.jumpchange = -0.03
                                    self.animalanimation10 = -1 
                                    self.animalpause10 = True
                                else:
                                    if self.mushroomawayanim == False:
                                        self.mushroomawayanim = True
                                        self.storemariomonstery = self.mariomovey
                    if self.animalpause10 == True:
                        self.animalpausecount10 += 1 
                    if self.animalpausecount10 >= 10:
                        self.animalswitch10 = True
                    if self.animalanimation10 != -1:
                        self.animalmove10 -= self.animalchange10
                    if self.animalanimation10 >= 4: 
                        self.animalanimation10 = 0 
                    if self.animalanimation10%2 == 0 and self.animalanimation10 >= 0:
                        drawanimal2(screen,self.enemy[0],self.questionPos,
                                    self.animalmove10,2690,255,animal_group10,
                                    self.animaly10)
                    if self.animalanimation10%2 != 0 and self.animalanimation10 >= 0:
                        drawanimal2(screen,self.enemy[1],self.questionPos,
                                    self.animalmove10,2690,255,animal_group10,
                                    self.animaly10)
                    if self.animalanimation10 == -1:
                        drawanimal2(screen,self.enemy[2],self.questionPos,
                                    self.animalmove10,2690,255,animal_group10,
                                    self.animaly10)
                    collideanimalfloor10 = pygame.sprite.spritecollide(animal_group10.sprites()[0],
                                    stepon_group, False)
                    if collideanimalfloor10 == []:
                        self.animaly10 += 10
                        self.animalchange10 = 0
                    if self.animalanimation10 != -1:
                        self.animalanimation10 += 1
                ###
                if self.screenmove <= -3100:
                    self.screenswitch11 = True 
                if self.animalswitch11 == False and self.screenswitch11 == True :
                    collideanimal11 = pygame.sprite.spritecollide(player_group.sprites()[0], 
                                    animal_group11, False)
                    if self.jumpchange <= -0.0305:
                        self.jumpacceleration = 0.0003
                        self.jumpchange = 0.03
                    if self.mushroom == False:
                        for thing in collideanimal11:
                            if self.animalpause11 == False:
                                if (player_group.sprites()[0].info()[1] <= thing.info()[1]
                                    and player_group.sprites()[0].info()[1] + 16 >= thing.info()[1] 
                                    and self.jumponoff == True):
                                    self.mariomovey = (thing.info()[1] - 16)/self.height
                                    self.score += 100
                                    self.jumpacceleration = -0.0003
                                    self.jumpchange = -0.03
                                    self.animalanimation11 = -1 
                                    self.animalpause11 = True
                                else:
                                    if self.mushroomawayanim != True and self.deathanimation == False:
                                        self.lives -= 1
                                        self.deathx = self.mariomovex
                                        self.deathanimation = True
                    if self.mushroom == True:
                        for thing in collideanimal11:
                            if self.animalpause11 == False:
                                if (player_group.sprites()[0].info()[1] <= thing.info()[1]
                                    and player_group.sprites()[0].info()[1] + 32 >= thing.info()[1] 
                                    and self.jumponoff == True):
                                    self.mariomovey = (thing.info()[1] - 32)/self.height
                                    self.score += 100
                                    self.jumpacceleration = -0.0003
                                    self.jumpchange = -0.03
                                    self.animalanimation11 = -1 
                                    self.animalpause11 = True
                                else:
                                    if self.mushroomawayanim == False:
                                        self.mushroomawayanim = True
                                        self.storemariomonstery = self.mariomovey          
                    if self.animalpause11 == True:
                        self.animalpausecount11 += 1 
                    if self.animalpausecount11 >= 10:
                        animal_group11.empty()
                        self.animalswitch11 = True
                    if self.animalanimation11 != -1:
                        self.animalmove11 -= self.animalchange11
                    for thing in animal_group11: 
                        if pygame.sprite.spritecollide(thing,tube_group, False):
                            if self.animalchange11 > 0:
                                self.animalmove11 += 7
                                self.animalmove12 += 7
                            if self.animalchange11 < 0:
                                self.animalmove11 -= 7
                                self.animalmove12 -= 7
                            self.animalchange11 = -self.animalchange11
                            self.animalchange12 = -self.animalchange12
                    if self.animalanimation11 >= 4: 
                        self.animalanimation11 = 0 
                    if self.animalanimation11%2 == 0 and self.animalanimation11>= 0:
                        drawanimal1(screen,self.enemy[0],self.questionPos,
                                    self.animalmove11,3790,255,animal_group11)
                    if self.animalanimation11%2 != 0 and self.animalanimation11 >= 0:
                        drawanimal1(screen,self.enemy[1],self.questionPos,
                                    self.animalmove11,3790,255,animal_group11)
                    if self.animalanimation11 == -1:
                        drawanimal1(screen,self.enemy[2],self.questionPos,
                                    self.animalmove11,3790,255,animal_group11)
                    if self.animalanimation11 != -1:
                        self.animalanimation11 += 1 
            #####
                if self.screenmove <= -3100: 
                    self.screenswitch12 = True 
                if self.animalswitch12 == False and self.screenswitch12 == True :
                    collideanimal12 = pygame.sprite.spritecollide(player_group.sprites()[0], 
                                animal_group12, False)
                    if self.jumpchange <= -0.0305:
                        self.jumpacceleration = 0.0003
                        self.jumpchange = 0.03
                    if self.mushroom == False:
                        for thing in collideanimal12:
                            if self.animalpause12 == False:
                                if (player_group.sprites()[0].info()[1] <= thing.info()[1]
                                    and player_group.sprites()[0].info()[1] + 16 >= thing.info()[1] 
                                    and self.jumponoff == True):
                                    self.mariomovey = (thing.info()[1] - 16)/self.height
                                    self.score += 100
                                    self.jumpacceleration = -0.0003
                                    self.jumpchange = -0.03
                                    self.animalanimation12 = -1 
                                    self.animalpause12 = True
                                else:
                                    if self.mushroomawayanim != True and self.deathanimation == False:
                                        self.lives -= 1
                                        self.deathx = self.mariomovex
                                        self.deathanimation = True
                    if self.mushroom == True:
                        for thing in collideanimal12:
                            if self.animalpause12 == False:
                                if (player_group.sprites()[0].info()[1] <= thing.info()[1]
                                    and player_group.sprites()[0].info()[1] + 16 >= thing.info()[1] 
                                    and self.jumponoff == True):
                                    self.mariomovey = (thing.info()[1] - 16)/self.height
                                    self.score += 100
                                    self.jumpacceleration = -0.0003
                                    self.jumpchange = -0.03
                                    self.animalanimation12 = -1 
                                    self.animalpause12 = True
                                else:
                                    if self.mushroomawayanim == False:
                                        self.mushroomawayanim = True
                                        self.storemariomonstery = self.mariomovey 
                    if self.animalpause12 == True:
                        self.animalpausecount12 += 1 
                    if self.animalpausecount12 >= 10:
                        animal_group12.empty()
                        self.animalswitch12 = True
                    if self.animalanimation12 != -1:
                        self.animalmove12 -= self.animalchange12
                    for thing in animal_group12: 
                        if pygame.sprite.spritecollide(thing,tube_group, False):
                            if self.animalchange12 < 0:
                                self.animalmove12 -= 7
                                self.animalmove11 -= 7
                            if self.animalchange12 > 0:
                                self.animalmove12 += 7
                                self.animalmove11 += 7
                            self.animalchange11 = -self.animalchange11
                            self.animalchange12 = -self.animalchange12
                    if self.animalanimation12 >= 4: 
                        self.animalanimation12 = 0 
                    if self.animalanimation12%2 == 0 and self.animalanimation12>= 0:
                        drawanimal1(screen,self.enemy[0],self.questionPos,
                                    self.animalmove12,3760,255,animal_group12)
                    if self.animalanimation12%2 != 0 and self.animalanimation12 >= 0:
                        drawanimal1(screen,self.enemy[1],self.questionPos,
                                    self.animalmove12,3760,255,animal_group12)
                    if self.animalanimation12 == -1:
                        drawanimal1(screen,self.enemy[2],self.questionPos,
                                    self.animalmove12,3760,255,animal_group12)
                    if self.animalanimation12 != -1:
                        self.animalanimation12 += 1 
                ####moving#############
                if ((t == []) and self.tubemark == True and 
                    self.mushroomtransfanim == False 
                    and self.mushroomawayanim == False):
                    self.tubemark = False
                    if self.moveleft == True:
                        self.screenchange = 4
                        self.questionChange = 4
                    if self.moveright == True:
                        self.screenchange = -4 
                        self.questionChange = -4
                if self.screenmove < -4120: 
                    self.screenchange,self.questionChange = 0,0 
                if self.screenmove > -2: self.screenchange,self.questionChange = 0,0
                if (self.moveleft == False and self.moveright == False and 
                    self.marioanimationmove >= 2 and self.marioanimationmove <= 8 
                    and self.mushroomtransfanim == False 
                    and self.mushroomawayanim == False):
                    self.marioanimationmove = 0 
                if ((self.moveleft == True or self.moveright == True) 
                    and self.marioanimationmove < 0 and 
                    self.mushroomtransfanim == False and self.mushroomawayanim == False):
                    self.marioanimationmove = 0 
                if (self.moveleft == True or self.moveright == True and 
                    self.mushroomtransfanim == False and self.mushroomawayanim == False):
                    self.marioanimationmove += 1
                    if self.moveleft == True:
                        if self.mariomovex <= 0.2:
                            self.mariochangex = 0 
                        else:
                            self.mariochangex = 0.005
                        for thing in collidequestion: 
                            #debug jump off on one side and then appear in the other 
                            if thing not in t:
                                if ((abs(thing.info()[0] - player_group.sprites()[0].info()[0]) <= 15) 
                                    and self.sidewaypump == False 
                                    and 0 <= player_group.sprites()[0].info()[1] - thing.info()[1]):
                                    self.mariomovex = (thing.info()[0] + 17)/self.width
                                    self.mariochangex = 0 
                                    self.screenchange = 0
                                    self.questionChange = 0 
                                    self.justmark = True 
                                    self.olddir = "left"
                                    self.moveleft = False 
                                    self.justmark = True 
                                    break
                            if thing in t:
                                if ((thing.info()[0] <= player_group.sprites()[0].info()[0] <= thing.info()[0] + 40) 
                                    and self.sidewaypump == False 
                                    and 0 <= player_group.sprites()[0].info()[1] - thing.info()[1]):
                                    self.mariomovex = (thing.info()[0] + 38)/self.width
                                    self.mariochangex = 0 
                                    self.screenchange = 0
                                    self.questionChange = 0 
                                    self.justmark = True 
                                    self.olddir = "left"
                                    self.tubemark = True 
                                    break
                        self.mariomovex = round(self.mariomovex - self.mariochangex,4) 
                    if self.moveright == True:
                        if self.mariomovex >= 0.8:
                            self.mariochangex = 0 
                        else: 
                            self.mariochangex = 0.005
                        for thing in collidequestion:
                            if ((abs(thing.info()[0] - player_group.sprites()[0].info()[0]) <= 15) 
                                and self.sidewaypump == False
                                and 0 <= player_group.sprites()[0].info()[1] - thing.info()[1]):
                                self.mariochangex = 0 
                                if thing not in t:
                                    self.mariomovex = (thing.info()[0] - 18)/self.width
                                else: self.mariomovex = (thing.info()[0] - 13)/self.width
                                self.screenchange = 0
                                self.questionChange = 0 
                                self.justmark = True
                                self.olddir = "right" 
                                if thing not in t:
                                    self.moveright = False 
                                self.tubemark = True 
                                break
                        self.mariomovex = round(self.mariomovex + self.mariochangex,4)
                    if self.marioanimationmove > 4:
                        self.marioanimationmove = 2
        #####
                if self.differentplatform == True:
                    if collidequestion == [] and self.jumponoff == False:
                        if self.ultimatestorey == 120:
                            self.jumppeak = 0.5-0.34
                        if self.ultimatestorey == 188:
                            self.jumppeak = 0.5
                        self.standingy = ((0.844*300)+ 15)/300
                        self.jumpacceleration = 0.00003
                        self.jumpchange = 0.03
                        self.differentplatform = False
                        self.jumpkeyreleaseabove, self.jumpkeyreleasebelow = False, False 
                        self.jumponoff = True
                        self.forcedown = False
    ######death###
                if (steponcollide != [] and self.mushroomtransfanim == False 
                    and self.mushroomawayanim == False):
                    self.jumppeak = 0.5
                    self.forcedown = False 
                if (self.jumponoff == True and self.mushroomtransfanim == False 
                    and self.mushroomawayanim == False):
                    self.gamecount2 = 0 
                if (collidequestion == [] and steponcollide == [] 
                    and self.jumponoff == False):
                    self.gamecount = 0 
                self.gamecount += 1
                if (self.gamecount == 1 and self.mushroomtransfanim == False 
                    and self.mushroomawayanim == False):
                    self.gamecount2 += 1 
                for thing in steponcollide:
                    if (collidequestion == [] and
                        ((player_group.sprites()[0].info()[0] > thing.info()[0] 
                        and player_group.sprites()[0].info()[0] > thing.info()[0] + 17) or 
                        (player_group.sprites()[0].info()[0] < thing.info()[0] 
                        and player_group.sprites()[0].info()[0] < thing.info()[0] - 17)) and 
                        self.jumponoff == False and (self.gamecount > 10 or self.gamecount2 > 4) 
                        and self.mushroomtransfanim == False 
                        and self.mushroomawayanim == False):
                        self.jumpacceleration = 0.003
                        self.jumpchange = 0.03
                if (collidequestion == [] and steponcollide == [] and 
                    self.jumponoff == False and (self.gamecount > 10 
                    or self.gamecount2 > 1) 
                    and self.mushroomtransfanim == False 
                    and self.mushroomawayanim == False):
                    self.jumpacceleration = 0.003
                    self.jumpchange = 0.03
                if (self.mariomovey*self.height + 8 > 0.894 *self.height 
                    and self.deathanimation == False):
                    self.lives -= 1
                    self.deathanimation = True 
                    self.deathx = self.mariomovex
                if self.deathanimation == True:
                    self.jumponoff = None
                    deathnow = death(self.mariotinyright[5], 
                            self.deathx*self.width, self.deathy, self.deathmove) 
                    self.deathmove += self.deathychange
                    self.deathychange += self.deathacceleration
                    if deathnow.info()[1] <= self.height*0.6:
                        self.deathychange = 5
                        self.deathacceleration = 2
                    if deathnow.info()[1] >= 0.894*self.height + 10:
                        self.deathanimation = False 
                        if self.lives == 0:
                            self.collectscorescreen = True
                            self.playing = False
                            self.deathy = self.height*0.7
                        if self.lives > 0:
                            self.deathmode = True 
                            self.playing = False
                            self.deathy = self.height*0.7
                    death_group.empty()
                    death_group.add(deathnow)
                    death_group.draw(screen)
                #####
                flag_group.empty()
                flag_group.add(flag(self.flagimg, 4236.5, 50, self.questionPos,0)) 
                flag_group.draw(screen)
                pole_group.empty()
                pole_group.add(pole(2, 195, (0,190,0), 4250,50, self.questionPos))
                pole_group.draw(screen)
                if (pygame.sprite.spritecollide(player_group.sprites()[0], 
                    pole_group,False) != []):
                    self.endingscreenchange = self.screenmove
                    self.score += self.mariomovey*self.height*10
                    self.endgame = True 
                    self.playing = False 
    ##############
                if (self.jumponoff == False and self.mushroomtransfanim == False 
                    and self.mushroomawayanim == False):
                    mariomoveanimation(screen,self.mariobigleft,self.mariobigright,
                                    self.mariotinyleft,self.mariotinyright,
                                    self.marioanimationmove,self.width,self.height,
                                    self.mariomovex,self.mushroom,
                                    self.moveleft,self.moveright,
                                    self.olddir,self.mariomovey)
                if (self.jumponoff == True and self.mushroomtransfanim == False 
                and self.mushroomawayanim == False):
                    mariojumpanimation(screen,self.mariobigleft,self.mariobigright,
                                        self.mariotinyleft,self.mariotinyright,
                                        self.mushroom,self.moveleft,self.moveright,
                                        self.mariomovex,
                                        self.mariomovey,self.width,
                                        self.height,self.olddir)
                if self.marioanimationmove <= 0 and self.screenchange == 0:
                    self.marioanimationmove -= 1
                if self.mushroomawayanim == True:
                    self.moveleft = False
                    self.moveright = False
                    self.jumpchange = 0 
                    self.mariochangex = 0 
                    self.mariomovey = self.storemariomonstery
                    if self.mushroomtranscount >= 0 and self.mushroomtranscount <= 2:
                        screen.blit(self.mariobigright[15], 
                                (self.mariomovex*self.width, 
                                self.mariomovey*self.height)) 
                    if self.mushroomtranscount >= 3 and self.mushroomtranscount <= 5:
                        screen.blit(self.mariobigright[6], 
                                (self.mariomovex*self.width, 
                                self.mariomovey*self.height)) 
                    if self.mushroomtranscount >= 6 and self.mushroomtranscount <= 8:
                        screen.blit(self.mariotinyright[6], 
                                (self.mariomovex*self.width, 
                                self.mariomovey*self.height)) 
                    if self.mushroomtranscount >= 9 and self.mushroomtranscount <= 11:
                        screen.blit(self.mariobigright[15], 
                                (self.mariomovex*self.width, 
                                self.mariomovey*self.height)) 
                    if self.mushroomtranscount >= 12 and self.mushroomtranscount <= 14:
                        screen.blit(self.mariobigright[6], 
                                (self.mariomovex*self.width, 
                                self.mariomovey*self.height)) 
                    if self.mushroomtranscount >= 15 and self.mushroomtranscount <= 17:
                        screen.blit(self.mariobigright[15], 
                                (self.mariomovex*self.width, 
                                self.mariomovey*self.height)) 
                    if self.mushroomtranscount >= 18 and self.mushroomtranscount <= 20:
                        screen.blit(self.mariotinyright[6], 
                                (self.mariomovex*self.width, 
                                self.mariomovey*self.height)) 
                    self.mushroomtranscount += 1 
                    if self.mushroomtranscount == 21:
                        self.mariomovey += (16/self.height)
                        self.mushroomtranscount = 0 
                        self.mushroomawayanim = False
                        self.storemariomonstery = None 
                        self.mushroom = False 
                ###key#########
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.ultimateplaying = False 
                    if event.type == pygame.KEYDOWN:
                        if (event.key == pygame.K_UP and self.jumponoff == False 
                            and self.mushroomtransfanim == False 
                            and self.mushroomawayanim == False):
                            self.jumponoff = True
                            self.jumpchange = -0.03
                            self.jumpacceleration = -0.00003
                            self.storeoldy = self.mariomovey 
                        if event.key == pygame.K_RIGHT:
                            if (self.screenmove > -4120 and (self.justmark == False 
                                or player_group.sprites()[0].info()[1] <188 
                                or player_group.sprites()[0].info()[1] <120) 
                                and self.tubemark == False 
                                and self.mushroomtransfanim == False
                                and self.mushroomawayanim == False): 
                                if self.jumponoff != True:
                                    self.screenchange = -4
                                    self.questionChange = -4
                                if self.jumponoff == True:
                                    self.screenchange = -2
                                    self.questionChange = -2
                            self.moveright = True
                        if event.key == pygame.K_LEFT:
                            if (self.screenmove < -2 and (self.justmark == False 
                            or player_group.sprites()[0].info()[1] <188 
                            or player_group.sprites()[0].info()[1] <120) 
                            and (self.tubemark == False) 
                            and self.mushroomtransfanim == False 
                            and self.mushroomawayanim == False): 
                                if self.jumponoff != True:
                                    self.screenchange = 4
                                    self.questionChange = 4
                                if self.jumponoff == True:
                                    self.screenchange = 2 
                                    self.questionChange = 2
                            self.moveleft = True 
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT: 
                            self.screenchange = 0
                            self.questionChange = 0
                            self.marioanimationmove = 0 
                            if self.moveright == True:
                                self.olddir = "right"
                            if self.moveleft == True:
                                self.olddir = "left" 
                            self.moveright = self.moveleft = False 
                        if self.forcedown == False:
                            if event.key == pygame.K_UP and self.mariomovey >= self.jumppeak + 0.15:
                                self.jumpkeyreleasebelow = True 
                            if event.key == pygame.K_UP and self.mariomovey < self.jumppeak + 0.15:
                                self.jumpkeyreleaseabove = True 
                pygame.display.flip()
            while self.endgame == True and self.playing == False and self.intro == False:
                clock.tick(self.fps)
                screen.blit(self.background, (self.endingscreenchange, 0))
                drawstairs(screen,self.stairimg, self.questionPos) 
                self.flagmariomovey += self.flagmarioychange 
                self.flagmariomovex += self.flagmarioxchange
                self.flagy += self.flagychange 
                if self.mushroom == False and self.yoloswitch == False:
                    mario = flagmario(self.mariotinyright[8], 
                            self.mariomovex*self.width, self.mariomovey*self.height, 
                            self.flagmariomovex, self.flagmariomovey,0)
                if self.mushroom == True and self.yoloswitch == False:
                    mario = flagmario(self.mariobigright[8], 
                            self.mariomovex*self.width, self.mariomovey*self.height, 
                            self.flagmariomovex, self.flagmariomovey,0)
                if ((self.flagmariomovey + self.mariomovey*self.height) > self.height*0.75 
                    and self.yoloswitch == False):
                    self.questionPos -= 2
                    self.endingscreenchange -= 2
                    self.flagmarioychange = 0 
                    self.flagmarioxchange = -2 
                    if self.questionPos < -4120 and self.endingscreenchange < -4120:
                        self.questionPos = -4120
                        self.endingscreenchange = -4120
                        self.yoloswitch = True 
                if (50 + self.flagy >= self.height*0.70):
                    self.flagychange = 0 
                if (self.questionPos == -4120 and self.endingscreenchange == -4120 
                    and self.yoloswitch == True and self.flagwait <= 20):
                    self.flagmarioxchange = 0 
                    if self.mushroom == False:
                        mario = flagmario(self.mariotinyleft[7], 
                                self.mariomovex*self.width+16, self.mariomovey*self.height, 
                                self.flagmariomovex, self.flagmariomovey,0)
                    if self.mushroom == True:
                        mario = flagmario(self.mariobigleft[8], 
                                self.mariomovex*self.width+16, self.mariomovey*self.height, 
                                self.flagmariomovex, self.flagmariomovey,0)
                    self.flagwait += 1
                if self.flagwait == 21:
                    self.flagmariomovex += 4
                    if self.mushroom == False:
                        self.flagmariomovey += 22
                    else: self.flagmariomovey += 14
                    self.flagwait += 1 
                if self.flagwait == 22 and self.yoloswitch == True:
                    self.flagmarioxchange = 1
                    if self.flagwalkanimation >= 0 and self.flagwalkanimation  <= 3: 
                        if self.mushroom == False:
                            mario = flagmario(self.mariotinyright[0], 
                                    self.mariomovex*self.width+16, 
                                    self.mariomovey*self.height, 
                                    self.flagmariomovex, self.flagmariomovey,0)
                        if self.mushroom == True:
                            mario = flagmario(self.mariobigright[0], 
                                    self.mariomovex*self.width+16, 
                                    self.mariomovey*self.height, 
                                    self.flagmariomovex, self.flagmariomovey,0)
                    if self.flagwalkanimation >= 4 and self.flagwalkanimation  <= 7: 
                        if self.mushroom == False:
                            mario = flagmario(self.mariotinyright[1], 
                                    self.mariomovex*self.width+16, 
                                    self.mariomovey*self.height, 
                                    self.flagmariomovex, self.flagmariomovey,0)
                        if self.mushroom == True:
                            mario = flagmario(self.mariobigright[1], 
                                    self.mariomovex*self.width+16, 
                                    self.mariomovey*self.height, 
                                    self.flagmariomovex, self.flagmariomovey,0)
                    if self.flagwalkanimation >= 8 and self.flagwalkanimation  <= 11: 
                        if self.mushroom == False:
                            mario = flagmario(self.mariotinyright[2], 
                                    self.mariomovex*self.width+16, 
                                    self.mariomovey*self.height, 
                                    self.flagmariomovex, self.flagmariomovey,0)
                        if self.mushroom == True:
                            mario = flagmario(self.mariobigright[2], 
                                    self.mariomovex*self.width+16, 
                                    self.mariomovey*self.height, 
                                    self.flagmariomovex, self.flagmariomovey,0)
                    self.flagwalkanimation += 1
                    if self.flagwalkanimation == 12:
                        self.flagwalkanimation = 0 
                flag_group.empty()
                flag_group.add(flag(self.flagimg, 4236.5, 50, self.questionPos,self.flagy)) 
                flag_group.draw(screen)
                pole_group.empty()
                pole_group.add(pole(2, 195, (0,190,0), 4250,50, self.questionPos))
                pole_group.draw(screen)
                if player_group.sprites()[0].info()[0] <= 0.64 and self.yoloswitch == True:
                    pole_group.draw(screen)
                player_group.empty()
                player_group.add(mario)
                if player_group.sprites()[0].info()[0] >= 0.66 * self.width and self.yoloswitch == True:
                    self.collectscorescreen = True 
                    self.endgame = False 
                if self.yoloswitch == True:
                    if player_group.sprites()[0].info()[0] <= 0.64 * self.width:
                        player_group.draw(screen)
                else: player_group.draw(screen)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.playing = False 
                        self.endgame = False 
                        self.collectscorescreen = False 
                        self.intro = False 
                pygame.display.flip()
            while self.endgame == False and self.collectscorescreen == True:
                clock.tick(self.fps)
                screen.fill((0,0,0))
                message("Time " + str(self.time), white, 50, "arialnarrow", screen, (120,70))
                message("SCORE " + str(self.score), white, 40,"arialnarrow", screen, (120,150))
                if self.time < 0:
                    self.time = 0
                if self.time > 0:
                    self.time -= 5
                    self.score = int(self.score +5)
                if self.time == 0:
                    self.restartgame = True
                    self.collectscorescreen = False 
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.ultimateplaying = False 
                pygame.display.flip()
            while self.restartgame == True:
                clock.tick(self.fps)
                screen.fill((0,0,0))
                if self.endgame3 == False:
                    message("Congrats, whether or not you passed, you can choose to play again by pressing k",white, 12,"arialnarrow", screen, (5,150))
                if self.endgame2 == True:
                    message("You Think You Get a Second Chance in Life Just by Pressing a Button?",white, 12,"arialnarrow", screen, (5,160))
                    message("If k doesn't work, try j",white, 15,"arialnarrow", screen, (30,170))
                if self.endgame3 == True:
                    self.bbbcount += 1 
                    message("Too Young, Too Simple",white, 15,"arialnarrow", screen, (30,170))
                if self.bbbcount > 30:
                    self.ultimateplaying = False 
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.ultimateplaying = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_k:
                            self.endgame2 = True 
                        if event.key == pygame.K_j and self.endgame2 == True:
                            self.endgame2 = False 
                            self.endgame3 = True  
                pygame.display.flip()
            while self.deathmode == True and self.playing == False:
                clock.tick(self.fps)
                screen.fill((0,0,0))
                self.heartanimationtime += 1 
                together = pygame.image.load("/Users/EugeneLi/Desktop/tp/together.png")
                togetherrect = together.get_rect()
                broken = pygame.image.load("/Users/EugeneLi/Desktop/tp/broken.png")
                brokenrect = broken.get_rect()
                self.heartx = 150
                message("Press f to continue before you lose another life in the dark",white, 15,"arialnarrow", screen, (30,170))
                if self.heartanimationtime <= 30:
                    for i in range(self.lives +1):
                        togetherrect.x = self.heartx
                        togetherrect.y = 150
                        screen.blit(together,togetherrect)
                        self.heartx += 30
                if self.heartanimationtime >= 31:
                    self.heartx = 150
                    for i in range(self.lives):
                        togetherrect.x = self.heartx
                        togetherrect.y = 150
                        screen.blit(together,togetherrect)
                        self.heartx += 30
                    for i in range(3-self.lives):
                        brokenrect.x = self.heartx
                        brokenrect.y = 150 
                        screen.blit(broken,(brokenrect))
                        self.heartx += 30
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.ultimateplaying = False 
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_f:
                            self.heartanimationtime = 0 
                            self.playing = True 
                            self.intro = False
                            self.endgame = False
                            self.restartgame = False
                            self.deathmode = False
                            self.collectscorescreen = False
                pygame.display.flip()
            while self.help == True and self.playing == False:
                clock.tick(self.fps)
                arrowimg = pygame.image.load(self.arrowimg) 
                arowrect = arrowimg.get_rect()
                arowrect.x = 70
                arowrect.y = 100
                helpimg = pygame.image.load(self.helpback)
                helprect = helpimg.get_rect() 
                helprect.x = 0
                helprect.y = 0
                animalimg = self.enemy[0] 
                animalrect = animalimg.get_rect()
                animalrect.x = 76
                animalrect.y = 190
                screen.blit(helpimg, helprect)
                screen.blit(arrowimg, arowrect)
                screen.blit(animalimg, animalrect)
                message("Press left to move left, right",(255,0,0), 15,
                            "arialnarrow", screen, (105,100))
                message("to move right, and up to jump",(255,0,0), 15,
                            "arialnarrow", screen, (105,110))
                message("Avoid these if you wish to LIVE!",(255,0,0), 
                            15,"arialnarrow", screen, (100,190))
                if self.Trueback == False:
                    message("Press b to Back",(255,0,0), 15,"arialnarrow", screen, (70,230))
                if self.Trueback == True:
                    message("You Think You can Back just by Pressing b?",
                            (255,0,0), 15,"arialnarrow", screen, (70,230))
                    message("Try Pressing f",(255,0,0), 15,"arialnarrow", 
                                screen, (70,250))
                message("WARNING!!!!!! THIS MAY LOOK LIKE A SIMPLE MARIO GAME BUT IT IS NOT", 
                        (255,0,0), 10, "arialnarrow", screen, (30, 270))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.ultimateplaying = False 
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_b:
                            self.Trueback = True
                        if event.key == pygame.K_f:
                            self.playing = False
                            self.intro = True
                            self.endgame = False
                            self.restartgame = False
                            self.deathmode = False
                            self.collectscorescreen = False
                            self.help = False 
                pygame.display.flip()
        pygame.quit()
game = PygameGame()
game.run()
