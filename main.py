import  pygame
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


if __name__ == "__main__":
    screen = pygame.display.set_mode(Background.size)
    pygame.display.set_caption ("Snake")
    BackGround = Background("assets/images/grass-image.jpg",[0,0])
    bgMusic = pygame.mixer.music
    bgMusic.load("assets/sounds/cheerfulstart.mp3")
    bgMusic.play(loops=5,start = 0.0)



    running = True
    while running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running=False
        screen.fill((255,255,255))
        screen.blit(BackGround.image,BackGround.rect)
        pygame.display.flip()
        
        
        
    







