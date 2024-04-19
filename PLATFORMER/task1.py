from pygame import*
from level import level
import time
SIZE=(1280,720)
win=display.set_mode(SIZE)
display.set_caption("Blockada")

while isGame:
    for e in event.get():
        if e.type==QUIT:
            isGame=False
    display.update()