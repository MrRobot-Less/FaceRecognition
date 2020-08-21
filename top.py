import pygame, math, sys


largura,altura = 500,500
win = pygame.display.set_mode((largura,altura))

cx,cy = 250,250

ang = 0 
pontos = 360
pos=[]

k = 1
r = 200

def escala(id, pontos, k):
    return id - (pontos)
    



for i in range(pontos):
    x1 = cx + math.cos(ang) * r
    y1 = cy + math.sin(ang) * r
    x1,y1 = int(x1), int(y1)
    pygame.draw.circle(win, (255,255,255), (x1,y1), 2,2)
    pos.append([x1,y1])
    ang += math.pi*2/pontos

while True:
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    if pygame.mouse.get_pos()[0] <= 200:
        k -= 0.05
        win.fill((0,0,0))
    elif pygame.mouse.get_pos()[0] >= 300:
        k += 0.05
        win.fill((0,0,0))
    else:
        k = k
    for x,y in pos:
        pygame.draw.circle(win, (255,255,255), (x,y), 2,2)
    for i in range(pontos):
        id = i * k
        while id >= pontos:
            id = (id - pontos)
            
            #print(id)
        id = int(id)
        pygame.draw.line(win, (255,255,255), pos[i], pos[id])
    pygame.display.flip()
    
