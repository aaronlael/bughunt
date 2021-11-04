import pygame
import bugsearch

pygame.init()
font = pygame.font.SysFont('Arial', 25)

def newgame():
    game = bugsearch.addbug(False)
    return game

def drawGrid(game):    
    x, y = 0,0
    rects = []
    for q in range(20):
        rects.append([])
        for z in range(20):
            rects[q].append(pygame.Rect(x,y,25,25))
            x += 25
        x = 0
        y += 25
    x, y = 0, 0
    for q in range(20):
        for z in range(20):
            pygame.draw.rect(screen, (0, 0, 0), rects[q][z], 1)
            screen.blit(font.render(game['game'][q][z], True, (0,0,0)), (x + 5,y -2))
            x += 25
        x = 0
        y += 25
    return rects


# Set up the drawing window
screen = pygame.display.set_mode([800, 800])
game = newgame()
# Run until the user asks to quit
running = True
gamedrawn = False
selected = []
while running:

    if not gamedrawn:
        screen.fill((255, 255, 255))
        rects = drawGrid(game)
        gamedrawn = True
        print(game['solution'])


    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                for rl in rects:
                    for r in rl:
                        if r.collidepoint(pygame.mouse.get_pos()):
                            pygame.draw.rect(screen, (255,255,0), r, 2)
                            selected.append(r)
                            selected = sorted(selected, key=lambda x: [x[1], x[0]])
                            if len(selected) > 1:
                                row = int(selected[0].y / 25)
                                col = int(selected[0].x / 25)
                                for key in game['solution'].keys():
                                    if game['solution'][key]['start'] == [row, col]:
                                        erow = int(selected[-1].y / 25)
                                        ecol = int(selected[-1].x / 25)
                                        if game['solution'][key]['end'] == [erow, ecol]:
                                            for rect in selected:
                                                pygame.draw.rect(screen, (0,255,0), rect, 2)
                                            selected = []
            elif event.button == 3:
                for rl in rects:
                    for r in rl:
                        if r.collidepoint(pygame.mouse.get_pos()):
                            pygame.draw.rect(screen, (0,0,0), r, 1)
                            if r in selected:
                                selected.remove(r)
        
                                        
                        





    pygame.display.flip()

# Done! Time to quit.
pygame.quit()



