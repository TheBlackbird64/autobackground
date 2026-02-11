from vars import Vars
import ctypes
import os
import subprocess
import cairosvg
import platform

class System:

    @staticmethod
    def changer_fond_ecran(chemin_image):
        
        chemin_absolu = os.path.abspath(chemin_image)
        
        if not os.path.exists(chemin_absolu):
            print("Erreur : fichier non trouvé.")
            return


        os_name = platform.system()

        if os_name == "Windows":
            if not ctypes.windll.user32.SystemParametersInfoW(20, 0, chemin_absolu, 3):
                print("Erreur lors du changement de fond d'écran.")
        
        elif os_name == "Linux":
            System.change_wallpaper_linux(chemin_absolu)

        elif os_name == "Darwin":
            pass

        else:
            print(f"Système d'exploitation non supporté : {os_name}")


    # Linux

    @staticmethod
    def change_wallpaper_linux(path):
        desktop = os.environ.get("XDG_CURRENT_DESKTOP", "").lower()

        if "gnome" in desktop:
            pass

        elif "kde" in desktop:
            script = f"""
            var allDesktops = desktops();
            for (var i = 0; i < allDesktops.length; i++) {{
                d = allDesktops[i];
                d.wallpaperPlugin = "org.kde.image";
                d.currentConfigGroup = Array("Wallpaper", "org.kde.image", "General");
                d.writeConfig("Image", "file://{path}");
            }}
            """
            os.system(f"qdbus org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript '{script}'")

        else:
            os.system(f"feh --bg-fill {path}")

    @staticmethod
    def convert_to_png():

        if os.path.exists("C:\Program Files\Inkscape\bin\inkscape.exe"):
            
            subprocess.run(
            [
                r"C:/Program Files/Inkscape/bin/inkscape",
                f"{Vars.FILENAME}.svg",
                "--export-type=png",
                f"--export-filename={Vars.FILENAME}.png"
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            creationflags=subprocess.CREATE_NO_WINDOW
            )

        else:
            cairosvg.svg2png(url=f"{Vars.FILENAME}.svg", write_to=f"{Vars.FILENAME}.png")
        
