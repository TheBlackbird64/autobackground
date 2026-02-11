# AutoBackground 

Ce projet est un changeur de fond d'écran du bureau. 
Le fond proposé est un fond géométrique à base de formes générés, testez par vous-même pour voir le résultat.

Toutes les minutes le fond est régénéré et change de couleur jusqu'à remplir tout l'écran en 1h, et le cycle recommence. 

## Utiliser le projet

```bash
./setup.bat
```

Ensuite vous pouvez modifier les paramètres dans le .env qui a été créé:

```.env
FILENAME=bg         # Nom du fichier généré
COTE=50             # Coté d'une forme
REPARTITION=15      # Repartition des triangles de la couleur inverse (plus la répartition est petite plus il y aura des triangles de couleur inverse dans un coté)
SHAPE=triangle      # forme (triangle, square, hexagon)
PROB_GREY1=0.2      # Probabilité qu'une forme soit plus/moins saturée (moins blanche/noire)
PROB_GREY2=0.2      # Si une forme est plus/moins saturée, probabilité d'accentuer
PROB_HUE1=0.07      # Probabilité qu'une forme soit de couleur, avec une saturation de 50
PROB_HUE2=0.07      # Si une forme est de couleur, probabilité 
PROB_HUE_COEF_BLACK_SIDE=0.5    # PROB_HUE1 * PROB_HUE_COEF_BLACK_SIDE est la probabilité qu'une forme de couleur apparaisse dans le coté noir. 1 pour avoir la même probabilité que sur le blanc (meme à 0 il peut y avoir des formes de couleur car une forme blanche peut devenir de couleur meme si elle est du coté noir)
```

Pour Linux, le fonctionnement du changement de fond d'écran diffère en fonction du bureau installé. Seul celui pour kde est implémenté pour le moment. 
Pour l'utiliser (gestionnaire de paquet arch): 

sudo pacman -S qt6-declarative  # Pour Plasma 6 (version actuelle)
sudo pacman -S qt5-tools        # Si vous êtes encore sur Plasma 5