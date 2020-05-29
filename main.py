import  pygame
import pygame_menu
pygame.init()

class Background(pygame.sprite.Sprite):
    height = 600
    width = 600
    size = (width,height)  
    def __init__(self,image_name,location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top=  location

class StartMenu():
    def __init__(self,width,height,text,theme):
        self.width = width
        self.height = height
        self.text = text
        self.theme = theme
    def start_game(self):
        pass
    def quit_game(self):
        pygame_menu.events.EXIT
    def show_credits(self):
        pass    

    
class Snake(pygame.sprite.Sprite):
    pass
    




class Food(pygame.sprite.Sprite):
    def __init__(self,image,location):
        pygame.sprite.Sprite.__init__(self)
        

if __name__ == "__main__":
    screen = pygame.display.set_mode(Background.size)
    #Set game title
    pygame.display.set_caption ("Snake")

    #Create background image object
    BackGround = Background("assets/images/grass-image.jpg",[0,0])
    bgMusic = pygame.mixer.music

    #load background music
    bgMusic.load("assets/sounds/cheerfulstart.mp3") 
    bgMusic.play(loops=5,start = 0.0)
    
    #display menu
    start_menu = StartMenu(300, 400, "Welcome to Snake", pygame_menu.themes.THEME_BLUE)

    menu = pygame_menu.Menu(start_menu.width, start_menu.height, start_menu.text,theme=start_menu.theme)
    menu.add_button('Play Game',start_menu.start_game) 
    menu.add_button('Quit Game',start_menu.quit_game) 
    menu.add_button('Credits',start_menu.show_credits)
    menu.mainloop(screen)




    running = True
    while running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running=False
        #Init bg color(white)
        screen.fill((255,255,255))
        #draw bg image on top of bg color
        screen.blit(BackGround.image,BackGround.rect)
        pygame.display.flip()
        
        
        
        
    







