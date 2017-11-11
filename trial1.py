import os,sys
import pygame as pg #lazy but responsible (avoid namespace flooding)

class Character:
    def __init__(self,rect):
        self.rect = pg.Rect(rect)
        self.click = False
        self.image = pg.Surface(self.rect.size).convert()
        self.image.fill((255,0,0))
    def update(self,surface):
        if self.click:
            self.rect.center = pg.mouse.get_pos()
        x = self.rect.topleft
        y = self.rect.bottomleft
        a = [x, y]
        surface.blit(self.image,self.rect)
        return a

def main(Surface,Player):
    white = (255, 255, 255)
    game_event_loop(Player)
    Surface.fill(white)
    t = Player.update(Surface)
    print t


def game_event_loop(Player):
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            if Player.rect.collidepoint(event.pos):
                Player.click = True
        elif event.type == pg.MOUSEBUTTONUP:
            Player.click = False
        elif event.type == pg.QUIT:
            pg.quit(); sys.exit()

if __name__ == "__main__":
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pg.init()
    Screen = pg.display.set_mode((1000,600))
    MyClock = pg.time.Clock()
    MyPlayer = Character((0,0,1,150))
    MyPlayer.rect.center = Screen.get_rect().center
    while 1:
        main(Screen,MyPlayer)
        pg.display.update()
        MyClock.tick(60)