#!/bin/bash

# ----------------------------------------------
# Descritpion : Polybar style changer
# Autor : Berthose Fin (Thos)
# Date : 2023-04-06
# ----------------------------------------------

DIR="$HOME/.config/polybar"
STYLE=$(sed -n '4s/STYLE=//p' "$DIR/launch.sh")

# Liste des styles disponibles
styles=("default" "default_b" "blocks" "docky" "forest" "grayblocks" "material")

# Convertir le tableau en une chaîne de caractères pour rofi
styles_string=$(printf "%s\n" "${styles[@]}")

# Demander à l'utilisateur de sélectionner un style via rofi
selected_style=$(echo -e "$styles_string" | rofi -dmenu -i -p 'Select Polybar Style')

# Vérifier si un style a été sélectionné
if [[ -n "$selected_style" ]]; then
    if [[ " ${styles[@]} " =~ " $selected_style " ]]; then
        sed -i "s/$STYLE/$selected_style/g" "$DIR/launch.sh"
        sh "$DIR/launch.sh"
    else
        echo "Invalid selection."
        exit 1
    fi
else
    echo "No style selected."
    exit 1
fi