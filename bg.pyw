from svgwrite import *
from datetime import datetime
from dotenv import dotenv_values
import ctypes
import os
import random
import pyautogui
import math
import colorsys
import time
import subprocess

config = {
    **dotenv_values(".env")
}

# Variables
COLORS = [i for i in range(0, 360, 30)]

FILENAME = config.get("FILENAME", "bg")
COTE = int(config.get("COTE", 50))
REPARTITION = int(config.get("REPARTITION", 15))

# Variables calculés
IMG_W, IMG_H = pyautogui.size()
h = (COTE**2 - (COTE/2)**2)**0.5 # hauteur


def changer_fond_ecran(chemin_image):
    
    chemin_absolu = os.path.abspath(chemin_image)
    
    if not os.path.exists(chemin_absolu):
        print("Erreur : fichier non trouvé.")
        return

    if not ctypes.windll.user32.SystemParametersInfoW(20, 0, chemin_absolu, 3):
        print("Erreur lors du changement de fond d'écran.")


def generer_image():
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    
    draw = Drawing(FILENAME + ".svg", size=(IMG_W, IMG_H))
    draw.add(draw.rect(insert=(0, 0), size=(IMG_W, IMG_H), fill="#FFFFFF"))
    
    start = 0
    angle = 1000
    decalage = (minute/59)*(IMG_W + 1000)
    pt1_ligne = (IMG_W - start - decalage, 0)
    pt2_ligne = (IMG_W - start + angle - decalage, IMG_H)
    
    def dist(x, y):
        x1, y1 = pt1_ligne
        x2, y2 = pt2_ligne
        num = abs((x2 - x1)*(y1 - y) - (x1 - x)*(y2 - y1))
        den = math.hypot(x2 - x1, y2 - y1)
        return num / den
    
    def position_relative(x, y):
        x1, y1 = pt1_ligne
        x2, y2 = pt2_ligne
        return (x2 - x1)*(y - y1) - (y2 - y1)*(x - x1)
    
    def hsv_to_rgb(h, s, v):
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        return int(r * 255), int(g * 255), int(b * 255)
    
    def color(x, y):
        side = False
        prob_col = 0.2
        prob_hue = 0.13
        prob_side = round(dist(x, y)/REPARTITION)+1
        
        if random.randint(0, prob_side) == 0:
            side = True
        if position_relative(x, y) < 0:
            side = not side
        if hour % 2 == 0:
            side = not side
        
        s = 0
        if random.random() < prob_col:
            s += 50
        elif random.random() < prob_col*2:
            s += 100
        
        
        if side:
            grey = round((s/100)*10 + 10)
        else:
            grey = round(245 - (s/100)*10)
        r, g, b = grey, grey, grey
        
        if not side:
            if random.random() < prob_hue:
                hue = COLORS[hour % 12]
                r, g, b = hsv_to_rgb(hue/360, s/100, 1)
        
        
        return f"rgb({r}, {g}, {b})"
    
    
    x = 0
    while x < IMG_W + COTE:
        y = 0
        while y < IMG_H + h:
            start_x = x-COTE/2 if round(y/h) % 2 == 0 else x
            
            draw.add(draw.polygon([(start_x, y), (start_x+COTE+1, y), (start_x+COTE/2, y+h+1)], fill=color(x, y)))
            draw.add(draw.polygon([(start_x, y-1), (start_x+COTE/2+1, y+h+1), (start_x-COTE/2-1, y+h+1)], fill=color(x, y)))
            
            y += h
        x += COTE
    
    draw.save()
    convert_to_png()
    return FILENAME + ".png"

def convert_to_png():
    subprocess.run(
    [
        r"C:\Program Files\Inkscape\bin\inkscape",
        "bg.svg",
        "--export-type=png",
        "--export-filename=bg.png"
    ],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
    creationflags=subprocess.CREATE_NO_WINDOW
    )


# declencheur, chaque minute -> update
def main():
    while True:
        changer_fond_ecran(generer_image())
        time.sleep(60)

if __name__ == "__main__":
    main()
