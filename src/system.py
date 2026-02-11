from vars import Vars
import ctypes
import os
import subprocess


class System:

    @staticmethod
    def changer_fond_ecran(chemin_image):
        
        chemin_absolu = os.path.abspath(chemin_image)
        
        if not os.path.exists(chemin_absolu):
            print("Erreur : fichier non trouvé.")
            return

        if not ctypes.windll.user32.SystemParametersInfoW(20, 0, chemin_absolu, 3):
            print("Erreur lors du changement de fond d'écran.")

    @staticmethod
    def convert_to_png():
        subprocess.run(
        [
            r"C:\Program Files\Inkscape\bin\inkscape",
            f"{Vars.FILENAME}.svg",
            "--export-type=png",
            f"--export-filename={Vars.FILENAME}.png"
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=subprocess.CREATE_NO_WINDOW
    )
