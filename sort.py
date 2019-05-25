from pygame import *
import random, gui
init()

SCREEN_W, SCREEN_H = 1200,400
screen = display.set_mode((SCREEN_W, SCREEN_H))
clock = time.Clock()

BLACK = 0,0,0
WHITE = 255,255,255
GREEN = 0,255,0 # sorted colour
RED = 255,0,0 # comparison colour

numValues = 20

barW = SCREEN_W/numValues
barH = SCREEN_H/numValues

# x position depends on index in value list, index is index of this bar in bars
class ValueBar: 
    def __init__(self, value=0, index=0):
        self.value = value
        self.index = index
        
        self.x, self.h = index*barW, barH*value
    def draw(self):
        self.h = barH*self.value
        y = SCREEN_H - self.h
        
        if finished:
            colour = GREEN
        elif self.index == i:
            colour = RED
        else:
            colour = WHITE
        
        draw.rect(screen, colour, (self.x,y,barW, self.h))

values = [i for i in range (1,numValues+1)]
random.shuffle(values)
bars = [ValueBar(values[i],i) for i in range (numValues)]
i = 0 # index
cutoff = 0

def bubbleSort(): # one iteration of bubble sort
    global i, numComparisons, cutoff
    if i >= numValues-cutoff-1:
        cutoff += 1
        i = 0

    if values[i] > values[i+1]: # swap
        numComparisons += 1
        values[i], values[i+1] = values[i+1], values[i]
    i += 1

def update():
    global finished
    if values == sorted(values):
        finished = True
    
    if not finished:
        bubbleSort()
    
    for x in range (numValues):
        bars[x].value = values[x]
        
    comparisonsText.update(str(numComparisons))

finished = False # sorting complete?
frameCounter = 0
simSpeed = 20 # gens per second

numComparisons = 0
comparisonsText = gui.SimpleText((0,0,100,100), str(numComparisons), 18, WHITE)

run = True
while run:
    screen.fill(BLACK)
    frameCounter += simSpeed
    
    if frameCounter >= 60:
        print(frameCounter//60)
        for x in range (int(frameCounter//60)):
            update()
            frameCounter = 0
    
    for bar in bars:
        bar.draw()
        
    comparisonsText.draw()
    
    for e in event.get():
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 4:
                simSpeed *= 2
            elif e.button == 5:
                simSpeed /= 2
            elif e.button == 3:
                simSpeed = 20
                
            if simSpeed < 5:
                simSpeed = 5
                
        if e.type == QUIT:
            run = False
    display.update()
    clock.tick(60)