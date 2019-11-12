import pygame
pygame.init()
pygame.display.set_icon(pygame.image.load("images/love.ico"))
pygame.display.set_caption("Okonogi Clicker")
face = pygame.image.load("images/bonapetit.png")
divider = pygame.Rect((800, 0), (1, 900))
okonogi = pygame.Rect((240, 255), (320, 390))
ciconiatxt = pygame.font.Font("font/ciconia.ttf", 80)
counter = pygame.Rect(360, 750, 80, 80)




def quitcheck(leave):
    if leave.type == pygame.QUIT:
        return False
    if leave.type == pygame.KEYDOWN and pygame.key.name(leave.key) == 'escape':
        return False
    else:
        return True


def startscreen():
    win = pygame.display.set_mode(size=(1600, 900))
    face.set_colorkey(0)
    win.fill(color=(144, 152, 163))
    pygame.draw.rect(win, 0, divider)
    pygame.draw.rect(win, (144, 152, 163), okonogi)
    win.blit(face, (240, 255))
    pygame.display.update()
    return win



def okonogicounter(okonogis, window):
    okonogis += 1
    pygame.draw.rect(window, (144, 152, 163), counter)
    count = ciconiatxt.render(str(okonogis), True, (0, 0, 0))
    window.blit(count, counter)
    pygame.display.update()
    pygame.event.clear()
    return okonogis














