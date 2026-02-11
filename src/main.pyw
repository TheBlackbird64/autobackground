from system import System
from generator import Generator
from vars import Vars
import time
import os

def main():
    if not os.path.exists(Vars.DIRNAME):
        os.makedirs(Vars.DIRNAME)
    
    while True:
        System.changer_fond_ecran(Generator.generer_image())
        time.sleep(60)

if __name__ == "__main__":
    main()
