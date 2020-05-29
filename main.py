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
        
        
        
    







