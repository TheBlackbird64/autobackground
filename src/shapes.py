from vars import Vars

class Shapes:

    def draw_screen(draw, callback):
        raise NotImplementedError("This method should be implemented by subclasses.")
    

class Triangle(Shapes):

    @staticmethod
    def draw_screen(draw, function_color):
        h = (Vars.COTE**2 - (Vars.COTE/2)**2)**0.5 # height
        x = 0
        while x < Vars.IMG_W + Vars.COTE:
            y = 0
            while y < Vars.IMG_H + h:
                start_x = x-Vars.COTE/2 if round(y/h) % 2 == 0 else x
                
                draw.add(draw.polygon([(start_x, y), (start_x+Vars.COTE+1, y), (start_x+Vars.COTE/2, y+h+1)], fill=function_color(x, y)))
                draw.add(draw.polygon([(start_x, y-1), (start_x+Vars.COTE/2+1, y+h+1), (start_x-Vars.COTE/2-1, y+h+1)], fill=function_color(x, y)))
                
                y += h
            x += Vars.COTE


class Square(Shapes):

    @staticmethod
    def draw_screen(draw, function_color):
        x = 0
        while x < Vars.IMG_W + Vars.COTE:
            y = 0
            while y < Vars.IMG_H + Vars.COTE:
                draw.add(draw.polygon([(x, y), (x+Vars.COTE, y), (x+Vars.COTE, y+Vars.COTE), (x, y+Vars.COTE)], fill=function_color(x, y)))
                
                y += Vars.COTE
            x += Vars.COTE


class Hexagon(Shapes):

    @staticmethod
    def draw_screen(draw, function_color):
        h = (Vars.COTE**2 - (Vars.COTE/2)**2)**0.5 # height
        x = 0
        while x < Vars.IMG_W + Vars.COTE:
            y = 0
            while y < Vars.IMG_H + h:
                start_x = x-Vars.COTE/2 if round(y/h) % 2 == 0 else x
                
                draw.add(draw.polygon([(start_x, y), (start_x+Vars.COTE+1, y), (start_x+Vars.COTE/2, y+h+1)], fill=function_color(x, y)))
                draw.add(draw.polygon([(start_x, y-1), (start_x+Vars.COTE/2+1, y+h+1), (start_x-Vars.COTE/2-1, y+h+1)], fill=function_color(x, y)))
                
                y += h
            x += Vars.COTE