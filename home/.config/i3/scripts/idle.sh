#!/usr/bin/env bash

# Exportation de la variable DISPLAY primaire
export PRIMARY_DISPLAY="$(xrandr | awk '/ primary/{print $1}')"

# Exécution de xidlehook
xidlehook \
  `# Ne pas verrouiller si une application est en plein écran` \
  --not-when-fullscreen \
  `# Ne pas verrouiller s'il y a du son en cours` \
  --not-when-audio \
  `# Diminuer la luminosité de l'écran après 150 secondes, restaurer si l'utilisateur devient actif` \
  --timer 150 \
  'xrandr --output "$PRIMARY_DISPLAY" --brightness .1' \
  'xrandr --output "$PRIMARY_DISPLAY" --brightness 1' \
  `# Verrouiller l'écran et restaurer la luminosité après 300 secondes supplémentaires` \
  --timer 300 \
  'xrandr --output "$PRIMARY_DISPLAY" --brightness 1; sh ~/.config/i3/scripts/lock.sh' \
  '' \
  `# Éteindre l'écran après 330 secondes de plus` \
  --timer 330 \
  'xset dpms force off' \
  'xset dpms force on' \
  `# Suspendre le système après 1800 secondes supplémentaires` \
  --timer 1800 \
  'systemctl suspend' \
  ''
