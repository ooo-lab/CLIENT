import math
import time
import os
import random

def cosmic_dance():
    width = 80
    height = 24
    phase = 0
    stars = [(random.randint(0, width), random.randint(0, height)) for _ in range(20)]
    
    while True:
        print('\033[H')  
        screen = [[' ' for _ in range(width)] for _ in range(height)]
        
        for x in range(width):
            y = int(height/2 + 5 * math.sin(x * 0.2 + phase))
            if 0 <= y < height:
                hue = (x * 15 + phase * 50) % 360
                color = f'\033[38;2;{int(255*abs(math.sin(hue/50)))};{int(255*abs(math.cos(hue/50)))};255m'
                screen[y][x] = color + '∼\033[0m'
        

        for i, (sx, sy) in enumerate(stars):
            x = int(sx + math.sin(phase + i) * 3)
            y = int(sy + math.cos(phase + i * 0.5) * 2)
            if 0 <= x < width and 0 <= y < height:
                color = f'\033[38;2;255;255;{int(255*abs(math.sin(phase + i)))}m'
                screen[y][x] = color + '★\033[0m'
        

        planet_x = int(width/2 + 10 * math.cos(phase * 0.3))
        planet_y = int(height/2 + 5 * math.sin(phase * 0.5))
        if 0 <= planet_x < width and 0 <= planet_y < height:
            color = f'\033[38;2;255;{int(200*abs(math.sin(phase)))};100m'
            screen[planet_y][planet_x] = color + '◉\033[0m'
        

        for row in screen:
            print(''.join(row))
        
        phase += 0.1
        time.sleep(0.05)

print('\033[2J') 
try:
    cosmic_dance()
except KeyboardInterrupt:
    print("\nАнимация завершена!")
