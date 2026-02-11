from dotenv import dotenv_values
import pyautogui

class Vars:
    config = {**dotenv_values(".env")}

    # config variables
    SHAPE = config.get("SHAPE", "triangle")
    FILENAME = config.get("FILENAME", "bg")
    COTE = int(config.get("COTE", 50))
    REPARTITION = int(config.get("REPARTITION", 15))
    PROB_COL = float(config.get("PROB_COL", 0.2))
    PROB_HUE = float(config.get("PROB_HUE", 0.13))

    # Variables
    COLORS = [i for i in range(0, 360, 30)]

    # calculated variables
    IMG_W, IMG_H = pyautogui.size()