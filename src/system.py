from vars import Vars
import ctypes
import os
import subprocess
import cairosvg
import platform

class System:

    # For KDE
    ALTERN = False

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
    def change_wallpaper_linux(chemin):
        desktop = os.environ.get("XDG_CURRENT_DESKTOP", "").lower()

        if "gnome" in desktop:
            pass

        elif "kde" in desktop:

            System.ALTERN = not System.ALTERN

            if System.ALTERN:
                if os.path.exists(Vars.FILENAME + "_temp.png"):
                    os.remove(Vars.FILENAME + "_temp.png")
                os.rename(Vars.FILENAME + ".png", Vars.FILENAME + "_temp.png")
                chemin = os.path.abspath(Vars.FILENAME + "_temp.png")

            script = f"""
            var allDesktops = desktops();
            for (var i = 0; i < allDesktops.length; i++) {{
                var d = allDesktops[i];
                d.wallpaperPlugin = "org.kde.image";
                d.currentConfigGroup = Array("Wallpaper", "org.kde.image", "General");
                d.writeConfig("Image", "file://{chemin}");
            }}
            """
            
            qdbus_cmd = "qdbus-qt6" if subprocess.run(["which", "qdbus-qt6"], capture_output=True).returncode == 0 else "qdbus"

            try:
                subprocess.run([
                    qdbus_cmd, 
                    "org.kde.plasmashell", 
                    "/PlasmaShell", 
                    "org.kde.PlasmaShell.evaluateScript", 
                    ''.join(script.split('\n'))
                ], check=True)
            except Exception as e:
                print(f"Erreur : {e}")
            os.system(f"qdbus org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript '{script}'")

        else:
            os.system(f"feh --bg-fill {chemin}")

    @staticmethod
    def convert_to_png():

        if os.path.exists(r"C:\Program Files\Inkscape\bin\inkscape.exe"):
            
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
        
