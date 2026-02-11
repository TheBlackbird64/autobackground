from dotenv import dotenv_values
import pyautogui

class Vars:
    config = {**dotenv_values(".env")}

    # config variables
    SHAPE = config.get("SHAPE", "triangle")
    FILENAME = 'generated/' + config.get("FILENAME", "bg")
    COTE = int(config.get("COTE", 50))
    REPARTITION = int(config.get("REPARTITION", 15))
    PROB_GREY1 = float(config.get("PROB_GREY1", 0.2))
    PROB_GREY2 = float(config.get("PROB_GREY2", 0.2))
    PROB_HUE1 = float(config.get("PROB_HUE1", 0.13))
    PROB_HUE2 = float(config.get("PROB_HUE2", 0.13))
    PROB_HUE_COEF_BLACK_SIDE = float(config.get("PROB_HUE_COEF_BLACK_SIDE", 0.5))

    # Variables
    COLORS = [i for i in range(0, 360, 30)]

    # calculated variables
    IMG_W, IMG_H = pyautogui.size()