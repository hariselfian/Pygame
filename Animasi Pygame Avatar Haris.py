import pygame,  sys

pygame.init()

screen = pygame.display.set_mode([200, 200])

Y = pygame.Color("yellow")
W = pygame.Color("white")
B = pygame.Color("black")
O = pygame.Color("orange")
R = pygame.Color("red")

frame1 = [
    [ B, B, Y, Y, Y, O, B, B ],
    [ B, Y, Y, Y, Y, Y, O, B ],
    [ Y, Y, B, Y, Y, B, Y, O ],
    [ Y, Y, B, Y, Y, B, Y, O ],
    [ Y, Y, Y, Y, Y, Y, Y, O ],
    [ Y, B, W, W, W, W, B, O ],
    [ B, Y, B, B, B, B, O, B ],
    [ B, B, Y, Y, Y, O, B, B ]
  ]

frame2 = [
    [ B, B, Y, Y, Y, O, B, B ],
    [ B, Y, Y, Y, Y, Y, O, B ],
    [ Y, R, Y, Y, R, Y, O, O ],
    [ Y, R, Y, Y, R, Y, O, O ],
    [ Y, Y, Y, Y, Y, Y, O, O ],
    [ Y, Y, W, W, W, R, O, O ],
    [ B, Y, R, R, R, O, O, B ],
    [ B, B, Y, Y, Y, O, B, B ]
  ]

frame3 = [
    [ B, B, O, Y, Y, Y, B, B ],
    [ B, O, Y, Y, Y, Y, Y, B ],
    [ O, O, Y, R, Y, Y, R, Y ],
    [ O, O, Y, R, Y, Y, R, Y ],
    [ O, O, Y, Y, Y, Y, Y, Y ],
    [ O, O, R, W, W, W, Y, Y ],
    [ B, O, O, B, B, B, Y, B ],
    [ B, B, O, Y, Y, Y, B, B ]
  ]

frame4 = [
    [ B, B, Y, Y, Y, O, B, B ],
    [ B, Y, B, Y, Y, B, O, B ],
    [ Y, Y, B, Y, Y, B, Y, O ],
    [ Y, Y, Y, Y, Y, Y, Y, O ],
    [ Y, B, W, W, W, W, B, O ],
    [ Y, Y, B, B, B, B, Y, O ],
    [ B, Y, Y, Y, Y, Y, O, B ],
    [ B, B, Y, Y, Y, O, B, B ],
  ]

frame5 = [
    [ B, B, Y, Y, Y, O, B, B ],
    [ B, Y, Y, Y, Y, Y, O, B ],
    [ Y, Y, Y, Y, Y, Y, Y, O ],
    [ Y, Y, B, Y, Y, B, Y, O ],
    [ Y, Y, B, Y, Y, B, Y, O ],
    [ Y, Y, Y, Y, Y, Y, Y, O ],
    [ B, Y, B, W, W, B, Y, B ],
    [ B, B, Y, Y, Y, Y, B, B ],
  ]

def draw_frame(surface, data):
    for y, row in enumerate(data):
      for x, colour in enumerate(row):
        rect = pygame.Rect(x*25, y*25, 25, 25)
        screen.fill(colour, rect=rect)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    draw_frame(screen, frame1)
    pygame.display.update()
    pygame.time.wait(500)
    draw_frame(screen, frame2)
    pygame.display.update()
    pygame.time.wait(500)
    draw_frame(screen, frame3)
    pygame.display.update()
    pygame.time.wait(500)
    draw_frame(screen, frame4)
    pygame.display.update()
    pygame.time.wait(500)
    draw_frame(screen, frame5)
    pygame.display.update()
    pygame.time.wait(500)
