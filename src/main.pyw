from system import System
from generator import Generator
import time

def main():
    while True:
        System.changer_fond_ecran(Generator.generer_image())
        break
        time.sleep(60)

if __name__ == "__main__":
    main()
