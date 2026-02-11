from svgwrite import *
from datetime import datetime
from system import System
from vars import Vars
import random
import math
import colorsys


class Generator:

    @staticmethod
    def get_shape():

        # Lazy loading
        if Vars.SHAPE == "triangle":
            from shapes import Triangle
            return Triangle
        
        if Vars.SHAPE == "square":
            from shapes import Square
            return Square
        
        if Vars.SHAPE == "hexagon":
            from shapes import Hexagon
            return Hexagon

    @staticmethod
    def generer_image():
        now = datetime.now()
        hour = 12#now.hour
        minute = 30#now.minute
        
        draw = Drawing(Vars.FILENAME + ".svg", size=(Vars.IMG_W, Vars.IMG_H))
        draw.add(draw.rect(insert=(0, 0), size=(Vars.IMG_W, Vars.IMG_H), fill="#FFFFFF"))
        
        start = 0
        angle = 1000
        decalage = (minute/59)*(Vars.IMG_W + 1000)
        pt1_ligne = (Vars.IMG_W - start - decalage, 0)
        pt2_ligne = (Vars.IMG_W - start + angle - decalage, Vars.IMG_H)
        
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
            prob_side = round(dist(x, y)/Vars.REPARTITION)+1
            
            if random.randint(0, prob_side) == 0:
                side = True
            if position_relative(x, y) < 0:
                side = not side
            if hour % 2 == 0:
                side = not side
            
            s = 0
            if random.random() < Vars.PROB_COL:
                s += 50
            elif random.random() < Vars.PROB_COL*2:
                s += 100
            
            
            if side:
                grey = round((s/100)*10 + 10)
            else:
                grey = round(245 - (s/100)*10)
            r, g, b = grey, grey, grey
            
            if not side:
                if random.random() < Vars.PROB_HUE:
                    hue = Vars.COLORS[hour % 12]
                    r, g, b = hsv_to_rgb(hue/360, s/100, 1)
                    print(r, g, b)
            
            
            return f"rgb({r}, {g}, {b})"
        
        
        shape = Generator.get_shape()
        shape.draw_screen(draw, color)
        
        draw.save()
        System.convert_to_png()
        return Vars.FILENAME + ".png"
    
