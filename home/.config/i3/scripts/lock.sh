#!/bin/bash

# Configuration
BLUR_LEVEL="5x3"             # Niveau de flou
IMAGE_PATH="/tmp/i3lock.png" # Chemin de l'image temporaire

# Capturer l'écran
scrot "$IMAGE_PATH"

# Appliquer le flou à l'image
magick "$IMAGE_PATH" -blur "$BLUR_LEVEL" "$IMAGE_PATH"

# Récupérer les couleurs de Pywal
source "${HOME}/.cache/wal/colors.sh"

# Couleurs personnalisées pour i3lock
TEXT_COLOR="$foreground"
RING_COLOR="$color8"
WRONG_COLOR="$color1"
VERIFYING_COLOR="$color4"

# Verrouiller l'écran avec i3lock
i3lock \
  -i "$IMAGE_PATH" \
  --inside-color=00000000 \
  --ring-color="$RING_COLOR" \
  --line-color=00000000 \
  --separator-color=00000000 \
  --insidever-color=00000000 \
  --ringver-color="$VERIFYING_COLOR" \
  --insidewrong-color=00000000 \
  --ringwrong-color="$WRONG_COLOR" \
  --time-color="$TEXT_COLOR" \
  --date-color="$TEXT_COLOR" \
  --verif-color="$TEXT_COLOR" \
  --wrong-color="$TEXT_COLOR" \
  --keyhl-color="$VERIFYING_COLOR" \
  --bshl-color="$WRONG_COLOR" \
  --layout-color="$TEXT_COLOR" \
  --screen 1 \
  --blur 5 \
  --clock \
  --indicator \
  --time-str="%H:%M:%S" \
  --date-str="%a %d %b %Y"

# Nettoyage de l'image temporaire
rm "$IMAGE_PATH"
